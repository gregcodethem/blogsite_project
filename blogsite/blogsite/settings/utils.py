import os


def identifies_production_or_local(base_url):
    dir_list = base_url.split('/')

    if dir_list[1] == 'Users':
        return 'local'
    else:
        return 'production'


def static_root(base_url):
    if identifies_production_or_local(base_url) is 'production':
        web_base_url = os.path.dirname(os.path.dirname(base_url))
        static_root = os.path.join(
            web_base_url,
            'public',
            'static',
        )
    else:
    	pass
