from api.urls import router
from django.core.management.base import BaseCommand
import requests
import logging
import threading
import queue
from time import sleep
logger = logging.getLogger('urltest')


def run(master, name):
    """runner for threads"""
    while not master.my_queue.empty():
        url = master.my_queue.get()
        master.response_handler(url)
    print("Finished thread number %s" % name)


class Command(BaseCommand):
    """
    Command class responsible for checking urls.
    """

    help = "urltest <host> [options]. Checking http_response for every link from router.registry"

    def test_urls(self, base_url):
        """

        :param base_url: url given as arguments from console
        :return: 0 if success, 2 if found any dead links
        """
        self.all_urls = 0
        self.broken_urls_counter = 0
        self.broken_urls = {}
        self.accepted_codes = (100, 101, 102, 200, 201, 202, 203, 204, 205, 206, 207,
                          208, 226, 300, 301, 302, 303, 304, 305, 306, 307, 308)
        model_to_check = self.options['model']
        self.my_queue = queue.Queue()
        for registry_element in router.registry:
            viewset_name = registry_element[0]
            if model_to_check != 'all':
                if viewset_name != model_to_check:
                    continue
            viewset = registry_element[1]
            queryset = viewset.get_queryset(viewset)
            self.my_queue.put(base_url+viewset_name + "/")
            for item in queryset:
                item = str(item.id)
                url = base_url + viewset_name + "/" + item + "/"
                self.my_queue.put(url)
        # we are using five threads
        for x in range(5):
            threading.Thread(target=run, args=(self, x)).start()
        while not self.my_queue.empty():
            sleep(1)
        logger.info("All urls: %s" % self.all_urls)
        logger.info("Broken urls: %s" % self.broken_urls_counter)
        if len(self.broken_urls) > 0:
            for key in self.broken_urls.keys():
                logger.error("%s %s %s" % (key, "\t", self.broken_urls[key]))
            exit(2)
        else:
            print("All links seems fine.")
            exit(0)

    def response_handler(self, url=""):
        """
        Check response for given url (created from params)
        :param base_url: url given as argument from console
        :param viewset: current viewset
        :param item: current item from viewset
        :return: if -q option were given it returns 2 in case of any dead links
        """
        try:
            status_code = requests.get(url).status_code
        except requests.exceptions.ConnectionError as error:
            logger.critical(error)
            exit(2)
        self.all_urls += 1
        logger.debug("Testing url: %s, status code: %s" % (url, status_code))
        if status_code not in self.accepted_codes:
            status_code = self.recheck(url)
            if not status_code:
                return
            self.broken_urls[url] = status_code
            self.broken_urls_counter += 1
            if self.options['quick']:
                logger.info("Tested urls: %s" % self.all_urls)
                logger.info("Dead urls: %s" % self.broken_urls_counter)
                logger.error(self.broken_urls)
                exit(2)

    def recheck(self, url):
        counter = 0
        while counter < self.options['tries'][0]:
            try:
                status_code = requests.get(url).status_code
            except requests.exceptions.ConnectionError as error:
                logger.critical(error)
            logger.info("Re-checking: %s %s" % (url, status_code))
            if status_code in self.accepted_codes:
                return False
            counter += 1
        return status_code

    def add_arguments(self, parser):
        parser.add_argument('-q',
                            '--quick',
                            action='store_true',
                            dest='quick',
                            default=False,
                            help='Passing this option will make urltest return after FIRST dead link')
        parser.add_argument('-u', '--url',
                            nargs=1,
                            dest='url',
                            default=['http://localhost:8000/'],
                            help="Url for testing. Format: http://URL/. Default: http://localhost:8000/")
        parser.add_argument('-t', '--tries',
                            nargs=1,
                            dest='tries',
                            default=[10],
                            type=int,
                            help="Provides a way to customize how many tries each link will be recheck in case of any errors. After "\
                            "that link will be considered dead. "
                            )
        parser.add_argument('-m', '--model',
                            dest='model',
                            default='all',
                            help="Possible values: %s" % self.create_model_list())

    def handle(self, *args, **options):
        """
        :param options: takes <url> and [options]
        """
        self.options = options
        self.test_urls(options['url'][0])

    @staticmethod
    def create_model_list():
        """creates string with all models in router.registry"""
        model_list = ""
        for registry_elementy in router.registry:
            model_list += registry_elementy[0] + ", "
        return model_list