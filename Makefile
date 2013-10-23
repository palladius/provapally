
deploy:
	@echo Deploying provapally..
	appcfg.py -R --oauth2 update .
auth:
	echo You might want to delete this: rm ~/.appcfg_oauth2_tokens 
deploy-first-time:
	appcfg.py -R update .
#--runtime=whatevs -R --oauth2 update .
deploy-locally:
	~/google_appengine/dev_appserver.py --port 8082 .
deploy-openid-palladius:
	echo Deploying to a different app_id from specified on YAML which I configured for OpenId:
	appcfg.py -R --oauth2  update -A s~openid-palladius .
logs:
	appcfg.py --oauth2 request_logs --application provapally --version v0-0-003 var/logs/logs-`data`.txt
