all: build push
	echo "All done"

build:
	jekyll build
	chmod +x _site/cgi-bin/*.cgi

push:
	rsync -rp _site/* peregoy@lawrenceyoga.com:/home/peregoy/lawrenceyoga.com
	rsync -p _site/.htaccess peregoy@lawrenceyoga.com:/home/peregoy/lawrenceyoga.com

