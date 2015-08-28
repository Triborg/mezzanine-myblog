"""
WSGI config for myblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
from __future__ import unicode_literals

import os, sys    
sys.path.append('/home/oreh/myblog/myblog')

from django.core.wsgi import get_wsgi_application
#from mezzanine.utils.conf import real_project_name


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
settings_module = "myblog.settings" 
#% PROJECT_ROOT.split(os.sep)[-1]

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "%s.settings" % settings_module)
                      
#real_project_name("myblog"))

application = get_wsgi_application()
