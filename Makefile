check:
	black --check git_signatures setup.py
	mypy git_signatures setup.py
	flake8 --count git_signatures setup.py
	pylint git_signatures setup.py

build:
	docker build --pull -t mloncode/git-signatures .

sync:
	@python -c 'import pkgutil; import sys; sys.exit(0 if pkgutil.find_loader("piptools") else 1)' \
		|| echo "Please install pip-tools to use make sync"
	pip-compile setup.py
	pip-compile dev-requirements.in
	pip-sync requirements.txt dev-requirements.txt

.PHONY: build check sync
