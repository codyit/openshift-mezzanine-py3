Mezzanine 3.1.9 and Python 3 on OpenShift
=========================================

Installation
------------

Create application and cd into the created dir
(replace mezzanine with the name of your app)
(optionally append -s to the app create command to enable auto scaling)

    rhc app create mezzanine python-3.3 postgresql-9.2
    cd mezzanine
    
Pull the adjustements

    git remote add openshift-mezzanine-py3 -m master git://github.com/codyit/openshift-mezzanine-py3.git
    git pull -s recursive -X theirs openshift-mezzanine-py3 master
        
Customize your settings

    /setup.py
        - Name
        - Email
        - etc..
    /wsgi/approot/settings.py
        - Allowed hosts
        - Timezone
        - etc..
    /wsgi/approot/urls.py
        - Setting the homepage, read the comments
    /.openshift/action_hooks/build (if you don't like en_US.UTF8)
        - export LC_ALL=

Commit changes

    git add -A
    git commit -m "Initial mezzanine deploy"
    
Push to openshift 

    git push
    
Then run this to create the initial tables and superuser. Follow the prompt, say no to demo page creation because of a bug.

    rhc ssh blog 
    source $VIRTUAL_ENV/bin/activate
    python $OPENSHIFT_REPO_DIR/wsgi/approot/manage.py createdb
    python $OPENSHIFT_REPO_DIR/wsgi/approot/manage.py collectstatic --noinput


What's in it
------------
Fixed a few niches, updated things to match the latest openshift changes.
Should deploy smoothly onto freshly created app.

If you use mysql it should work too, please test it and let me know if there is any problem.
