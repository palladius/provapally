
deploy:
	@echo Deploying provapally..
	appcfg.py -R --oauth2 --application=provapally update .
deploy-first-time:
	appcfg.py -R  --application=provapally update .
#--runtime=whatevs -R --oauth2 update .
deploy-locally:
	~/google_appengine/dev_appserver.py . --port 8081