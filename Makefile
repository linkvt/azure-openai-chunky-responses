VENV_NAME := .venv

.PHONY: venv
venv:
	@python3 -m venv $(VENV_NAME)

.PHONY: activate
activate:
	@source $(VENV_NAME)/bin/activate

.PHONY: install
install:
	@pip install -r requirements.txt

.PHONY: freeze
freeze:
	@pip freeze > requirements.txt

.PHONY: clean
clean:
	@rm -rf $(VENV_NAME)

.PHONY: default
default: venv activate install

.PHONY: run
run:
	@python3 main.py
