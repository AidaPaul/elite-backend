# elite-backend
A project to provide open source way to play with Elite: Dangerous market data, ships and mod locations
and ideally create a meta-platform that will be easy to use and re-use for all developers, so they can
just focus on writing the app of their dreams, and not waste time on redoing what already was done.
If time allows I also want to write a simple website to do provide users with simple web interface to common functions
like finding commodity, traderoute, ships etc.

This of course is far road away, but certainly reachable within a reasonable timeframe. In the end, it's just data
and representing it in REST way that is easy to extend and deploy + writing integration with existing sources.

# Live demo
Live version of master branch of this code can be found at http://elite.x20x.co.uk/. Anonymous users have read access
and so far write access is restricted to registered users.

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
4. Run database migration with command `python manage.py migrate`
5. Populate the database with command `python manage.py refreshdata`. This WILL take a while, how long
exactly depends primarily on performance of your SQL server (this is very insert-heavy operation).
6. Optionally you can also run tests, to do so use command `python manage.py test`
    
# Running and usage

Once everything is set up and shining, then all left to do is to type `python manage.py runserver` and it's alive!
When you steer to the bound ip and port, you will find that at /api there is a neat web-interface that allows
for easy browsing of the API structure and data. You can also manipulate it from django admin (/admin).
    
# Issues? Grievances? Complains? Feature requests? Ideas? 
Please leave them at github or contact me by email.