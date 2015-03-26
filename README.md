# elite-backend
A project to provide open source way to play with Elite: Dangerous market data.
And also some rest interface so this data can be easily used by 3rd party apps.

# Live demo
Coming somewhere tomorrow or around the weekend. Will update this section once it is up ;).

# Set-up steps

## Dependencies

    * [Python 3.4 or newer] (https://www.python.org/download/releases/3.4.0/)
    * [PIP] (https://pypi.python.org/pypi/pip)
    * [GIT] (http://git-scm.com/)
    * Some form of SQL database (using SQLite is highly not recommended)
    
## Installation

    1. Checkout the repo from git
    2. Install python dependencies by running `pip install -r requirements.txt`. 
    3. Copy settings.py.template as settings.py and make sure to input your SQL details in approperiate place.
    4. Run database sync with command `python manage.py syncdb`
    5. Populate the database with command `python manage.py refreshdata`. This WILL take a while, how long
    exactly depends primarily on performance of your SQL server (this is very insert-heavy operation).
    
# Running and usage

    Once everything is set up and shining, then all left to do is to type `python manage.py runserver` and it's alive!
    When you steer to the bound ip and port, you will find that at /api there is a neat web-interface that allows
    for easy browsing of the API structure and data. You can also manipulate it from django admin (/admin).
    
# Issues? Grievances? Complains? Feature requests? Ideas? 
Please leave them at github or contact me by email.