#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals
import os
import sys

#from settings import PROJECT_ROOT, PROJECT_DIRNAME
#sys.path.append(os.path.abspath(os.path.join(PROJECT_ROOT, "..")))

if __name__ == "__main__":

    from mezzanine.utils.conf import real_project_name
    
    settings_module = "%s.settings" % real_project_name("myblog")

#% PROJECT_DIRNAME
#real_project_name("myblog")

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
