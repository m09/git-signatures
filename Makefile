check:
	black --check git_signatures setup.py
	mypy git_signatures setup.py
	flake8 --count git_signatures setup.py
	pylint git_signatures setup.py

build:
	docker build --pull -t mloncode/git-signatures .

.PHONY: build check
