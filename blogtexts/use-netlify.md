Following this repo:


https://github.com/tomdyson/wagtail-netlify



To install netlify: follow instructions at: https://docs.netlify.com/cli/get-started/#installation

check node version is suitable,
higher than 8 at time of writing:

node -v

npm install netlify-cli -g

Add wagtailnetlify to your INSTALLED_APPS.

Run the migrations: ./manage.py migrate wagtailnetlify.

add to settings:
NETLIFY_PATH = '/usr/local/bin/netlify'