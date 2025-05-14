run:
	poetry run python main.py data1.csv data2.csv data3.csv --report payout

type:
	poetry run mypy .

style:
	poetry run flake8 .

.PHONY: tests

tests:
	poetry run pytest . -vv
