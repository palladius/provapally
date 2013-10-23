
deploy:
	@echo Deploying provapally..
	appcfg.py -R --oauth2 update .
deploy-first-time:
	appcfg.py -R update .
#--runtime=whatevs -R --oauth2 update .
deploy-locally:
	~/google_appengine/dev_appserver.py --port 8082 .
deploy-openid-palladius:
	echo Deploying to a different app_id from specified on YAML which I configured for OpenId:
	appcfg.py -R  update -A s~openid-palladius .
