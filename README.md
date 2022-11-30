# lbg-london-reboot

Hackathon Codebase for LBG London Hackathon

Going through the steps to set up Django:

Create a virtual environment (Windows): mkvirtualenv --python=<python-version> reboot #Put in the version of python you're using.

Create a Virtual Env (Mac): python3 -m venv venv then run the following command to activate virtual env source venv/bin/activate

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


To boot up a database on azure:
1. Create an image using the dockerfile saved under mysql folder in this project 
2. Must follow naming conventions specified on Azures documentation (include container registry name...)
3. login to azure on command line 
4. login to container registry 
5. push your image by running docker push (name_of_image)
6. Navigate to container instances on azure
7. Create new instance using the docker image we pushed to the registry 
8. Must be atleast 4gb of memory and 2 vcpus
9. Expose port 3306 using TCP under networking and create 

To run the app on webapp
1. Update the db connection under settings 
2. Update allowed host to all by adding * in the brackets 
3. Delete code under init file as it is not needed for external db
4. Get the app and virtual env running locally using the steps above (Must make sure db container is running )
5. Login in to azure on command line 
6. Run az webapp up (specify location and resource group)
7. Once complete, navigate to the webapp console and get the url to access the app 