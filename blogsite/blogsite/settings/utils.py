

def identifies_production_or_local(base_url):
	dir_list = base_url.split('/')
	
	if dir_list[1] == 'Users':
		return 'local'
	else:
		return 'production'