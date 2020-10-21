test:
	TESTING=true pytest --cov=. && flake8

test-local:
	pytest -s --cov=. && flake8

dev-server:
	python -m app.main app/main.py

