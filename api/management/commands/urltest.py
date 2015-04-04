from api.urls import router
from django.core.management.base import BaseCommand
import requests
import logging

logger = logging.getLogger('urltest')


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
        for registry_element in router.registry:
            viewset_name = registry_element[0]
            viewset = registry_element[1]
            queryset = viewset.get_queryset(viewset)
            self.response_handler(base_url, viewset_name)
            for item in queryset:
                item = "/"+str(item.id)
                self.response_handler(base_url, viewset_name, item)
        logger.debug("All urls: %s" % self.all_urls)
        logger.debug("Broken urls: %s" % self.broken_urls_counter)
        if len(self.broken_urls) > 0:
            for key in self.broken_urls.keys():
                logger.error("%s %s %s" % (key, "\t", self.broken_urls[key]))
            exit(2)
        else:
            print("All links seems fine.")
            exit(0)

    def response_handler(self, base_url, viewset="", item=""):
        """
        Check response for given url (created from params)
        :param base_url: url given as argument from console
        :param viewset: current viewset
        :param item: current item from viewset
        :return: if -q option were given it returns 2 in case of any dead links
        """
        url = "".join((base_url, viewset, item))
        status_code = requests.get(url).status_code
        self.all_urls += 1
        if status_code > 400 and status_code < 600:
            self.broken_urls[url] = status_code
            self.broken_urls_counter += 1
            if self.options['quick']:
                logger.debug("Tested urls: %s" % self.all_urls)
                logger.debug("Dead urls: %s" % self.broken_urls_counter)
                logger.error(self.broken_urls)
                exit(2)

    def add_arguments(self, parser):
        """adds options --quick and argument for host"""
        parser.add_argument('-q',
                            '--quick',
                            action='store_true',
                            dest='quick',
                            default=False,
                            help='Passing this option will make urltest return after FIRST dead link')
        parser.add_argument('host', nargs=1)

    def handle(self, *args, **options):
        """
        :param options: takes <host> and [options]
        """
        self.options = options
        self.test_urls(options['host'][0])
