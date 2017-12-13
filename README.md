```
i am still pushing changes to this repo.
```
# memehunter
A meme retrieval engine - rest api built with django, DRF
Frontend with react and redux, hosted on netlify.

See [`./requirements.txt`](https://github.com/geekodour/memehunter/blob/master/requirements.txt) for all dependencies.

# Stack Used
 - Django 2.0
 - Django Rest Framework
 - MongoDB, Sqlite3
 - BS4, requests
 - gensim

# Quick start
Download the GoogleNews Word2Vec Slim from [here](https://github.com/eyaler/word2vec-slim), extract and put it by this `./README.md` in the root directory.

Create a virtualenv and install the dependencies using `pip install -r requirements.txt`

Create a environment variable using `export DJANGO_SETTINGS_MODULE=config.settings.local`

Now run the following:
```
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py fetchinitialmemes
$ ./manage.py indexdbfields
$ ./manage.py runserver
```
the `fetchinitialmemes` command will take a while because It will be fetching the memes from the sources.

To access the api after running runserver:
- All memes endpoint: http://localhost:8000/api/memes/
- Single memes endpoint: http://localhost:8000/api/memes/MEME_ID
- Search memes endpoint: http://localhost:8000/api/search/?q=office

# The Idea
Memes are fetched from various sources(currently **reddit** and **giphy** but other sources like **facebook/instagram** can be added easily)
the fetching part lives in `./memes/tasks/fetchmemes.py`.
All the fetching classes inherit from the base fetching class `BaseMemeFetcher` in `./memes/tasks/fetchmemes.py`

#### Django admin commands
- **fetchinitialmemes**: These`(./memes/tasks/fetchmemes.py)` fetch instances are called by a custom django admin command called **fetchinitialmemes** which lives in `./memes/management/commands/fetchinitialmemes.py`.User can specify how many memes should be fetched initially from each source.  These fetch instances were designed so that they can be ran after a specific period of iterval using celery (not implemented because of time constraints) So fetch and process 1000 memes initially and store processed information in the database. That's what **fetchinitialmemes** does.
- **indexdbfields**: This django admin command indexes the mongoDB


### Meme Retrival Process
There is only one enpoint for the search and it takes only a query parameter named `q`, so user needs to pass the query to `q`

Example:
```
http://localhost:8000/api/search/?q=happy,memes
```

