Virtualenv Bootstrapper
========================

When you are about to create a python program with some pip modules, you may setup virtualenv and install some pip modules within that virtualenv manually. If you use this module, you can take virtualenv automatically.

Setup
-------------

### Requirements

* python
* pip
* virtualenv

### Installation

    $ pip install vebootstrap

Usage
--------------

**Importing**

Insert following line into head of your script file, and create a `requirements.txt` in same directory as necessary.

    import vebootstrap

Running that script, it creates a virtualenv and modules will be installed automatically.

**Not Importing**

If you do not want to add a line, run following command and then virtualenv will be prepared.

    python -m vebootstrap [script file]

Example
--------------

**Case: you want to create a script using `requests` module. (http request library)**

Create a script file (eg. get\_yahoo.py)

    import vebootstrap # you must write this sentence at the first line
    import requests
    print(requests.get('http://yahoo.co.jp').content[:100])

Create a `requirements.txt`

    requests

Run a script

    python get_yahoo.py

At the first time, virtualenv will be created and modules will be installed.
And You get a first line of html of the Yahoo.

