
build:
	docker build -t xx .

update:
	docker run -v $$(pwd):$$(pwd) -w $$(pwd) xx python update.py

git_setup:
	git config user.email "rbx-openapi-archive@github.com"
	git config user.name "Bot"

autocommit:
	git add * && git commit -m "$$(date +"Update %d-%m-%d %H:%M")" || exit 0;
