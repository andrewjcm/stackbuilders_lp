### To run:

1) Wagtail (activate virtual env):

       pip install -r requirements.txt
       python manage.py runserver

2) Webpack (separate shell):

        cd webpack
        npm install
        npm run build
        npm run watch

The database was included in the repo since certain Wagtail settings were pre-configured.
Internationalization is determined by the end-user's browser settings (english or spanish). 
Contact info can be edited at the root home page. It is expected that this will never reach
production - no secrets suppressed. Superuser credentials are below.

Username: admin  
Password: pass
