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

### Vagrant (1.5+ required)
1. Copy settings.py.template as settings.py and make sure to input your SQL details in approperiate place. I 
highly advise against running db on the same, tiny, vagrant box.
1. Command to buid and provision the box is `vagrant up`
2. When it is done the service should be reachable at your localhost on port 9191, if it isn't - it will be on
the virtual boxes IP (depends on how is network configured on your end).

#### Optional - import the data (skip if you already have populated database) 
4. Populate the database with commands  `vagrant ssh -c "python3 /opt/elite-backend/manage.py migrate"` and 
`vagrant ssh -c "python3 /opt/elite-backend/manage.py refreshdata"`. This WILL take a while, how longexactly depends 
primarily on performance of your SQL server (very insert-heavy operation).

### Manual installation (for those hailing from 20th century)

1. Install python dependencies by running `pip install -r requirements.txt`. 
2. Copy settings.py.template as settings.py and make sure to input your SQL details in approperiate place.
3. Run database migration with command `python manage.py migrate`
4. Populate the database with command `python manage.py refreshdata`. This WILL take a while, how long
exactly depends primarily on performance of your SQL server (this is very insert-heavy operation).
5. Optionally you can also run tests, to do so use command `python manage.py test`
    
# Running and usage

Once everything is set up and shining, then all left to do is to type `python manage.py runserver` and it's alive!
When you steer to the bound ip and port, you will find that at /api there is a neat web-interface that allows
for easy browsing of the API structure and data. You can also manipulate it from django admin (/admin).

Master branch points at latest release point. If you want most recent version then feel free to pull from dev branch,
which is copied over to master when milestone is reached.

## Commands

### urltest

`manage.py urltest [options]` is command for testing all generated urls (including dynamically generated). Options:

* `-q` - allows for quick testing urls. Command will return exit-code 2 after first encounter dead url
* `-t` - allows to specify how many times potentially broken url will be re-checked before considered dead.
* `-m` - allows to choose model from which urls for testing will be generated
    
# Issues? Grievances? Complains? Feature requests? Ideas? 
Please leave them at github or contact me by email.

# Credits
I always give credit where it's due, so it's worth to mention couple projects.
* [Frontier Development] (http://frontier.co.uk/) - for making Elite: Dangerous
* [Elide dangerous wiki] (http://elite-dangerous.wikia.com/wiki/Elite_Dangerous_Wiki) - for collecting this mountain
of data
* [E:D Shipyard] (http://www.edshipyard.com/) - for collecting all the module stats, even the hidden ones!
* [eddb] (http://eddb.io/) - for the easy-to-access export of their data which we so happily use :)
* [Leffe] (http://www.leffe.com/en) - do I have to say more?
