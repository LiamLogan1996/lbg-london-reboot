# lbg-london-reboot
Hackathon Codebase for LBG London Hackathon

Going through the steps to set up Django:

Create a virtual environment: mkvirtualenv "name of virtual environment"

Once cloned from repo, try pip install the requirements.txt via: pip install -r requirements.txt. You may need to change
directory.

Change directory to lbgLondonReboot, the same directory with manage.py, then run python manage.py runserver.

You should be given an IP, click on IP, you should see a basic HTML example.

Populating the database:

python manage.py makemigrations
python manage.py migrate
python populate_products.py
python manage.py createsuperuser
enter username, email (fake) and password.
python manage.py runserver, add "/admin" to local host in web browser. 
login and check products has been populated. 
Try enter a salary and inflation on the home page.