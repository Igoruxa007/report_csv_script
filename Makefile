run:
	poetry run python main.py data1.csv data2.csv data3.csv

type:
	poetry run mypy .

style:
	poetry run flake8 .

tests:
	poetry run pytest .