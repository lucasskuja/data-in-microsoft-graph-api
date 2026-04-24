.PHONY: install test run clean

install:
	pip install -r requirements.txt

test:
	pytest tests/

run:
	python src/main.py

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache