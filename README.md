Virtualenv Bootstrapper
========================

When you are about to create a python program that depends on some packages, you may setup virtualenv and install some packages within that virtualenv manually. This module automatically creates an environment and installs packages in it.

Setup
-------------

**Requirements**

* python 2.7 or later
* pip
* virtualenv

**Installation**

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

At first, virtualenv directory will be created and required packages will be installed.
And you get a first line of html of the Yahoo.

Extra Usage
--------------

`vebootstrap` supports creating virtualenv bootstrap script. Run a following command in your scripting directory. The bootstrap script involving `requirements.txt` will be created.

    python -m vebootstrap.create_bootstrap

`--after-install` option allows you to add another process into the bootstrap script. Please see help.

    python -m vebootstrap.create_bootstrap --help

