#!/usr/bin/env python
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

if 'OPENSHIFT_REPO_DIR' in os.environ:
     sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'approot'))
     virtenv = os.environ['VIRTUAL_ENV']
     os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python3.3/site-packages')
     virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
     try:
        exec(compile(open(virtualenv).read(), virtualenv, 'exec'),dict(__file__ = virtualenv))
     except IOError:
         pass

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
