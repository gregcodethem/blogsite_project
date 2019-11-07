import sys, os
cwd = os.getcwd()
INTERP = cwd+"/env/bin/python"
#INTERP is present twice so that the new python interpreter
#knows the actual executable path 
if sys.executable != INTERP: 
    os.execl(INTERP, INTERP, *sys.argv)

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/blogsite_project/blogsite')  #You must add your project here

sys.path.insert(0, cwd + '/env/bin')
sys.path.insert(0, cwd + '/env/lib/python3.6/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "blogsite.settings.production"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#if sys.hexversion < 0x2060000: os.execl("/home/shellgreg/.envs/lucidcooking/bin/python", "python3.6", *sys.argv)
