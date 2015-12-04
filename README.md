### Installation

Creating the Virtual Environment

    $ virtualenv --python=python2.7 --no-site-packages env
    $ source env/bin/activate

Install requirements

    $ pip install -r requirements.txt

Make migrations

    $ cd compfirm/
    $ ./manage.py migrate
