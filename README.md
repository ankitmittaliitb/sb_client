sb_client
=========

#social billboard client

#1. Download virtualenv.py and put it inside the new folder

https://raw.github.com/pypa/virtualenv/1.9.X/virtualenv.py

#2. To create the virtual environment enter the following command:

python virtualenv.py flask

#3. Now run the following commands:

    i. flask/bin/pip install flask==0.9
    ii. flask/bin/pip install sqlalchemy==0.7.9
    iii. flask/bin/pip install flask-sqlalchemy==0.16
    iv. flask/bin/pip install sqlalchemy-migrate==0.7.2
    v. flask/bin/pip install pytz==2013b
    vi. flask/bin/pip install flup
    vii. flask/bin/pip install birdy

#4. Add the file app/db_fetch.py to cron do:

-> open cron using crontab -e 
->  */2 * * * * /sb_client/db_fetch.py
-> save the file.
    
    
