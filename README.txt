
Installation Commands Used
    python3 -m venv venv
    source venv/bin/activate
    pip install psycopg2-binary
    pip install flask-sqlalchemy
    pip install flask-debugtoolbar
    pip3 freeze > requirements.txt
    touch .gitignore

Start postgresql in Ubuntu
    sudo apt-get install postgresql
    sudo service postgresql status
    sudo service postgresql start