run:
	python -m uvicorn app.main:app --reload

test:
	pytest -q --disable-warnings

db:
	python -m app.database.init_db

clean:
	rm -f *.db
	rm -rf __pycache__
	find . -name "__pycache__" -type d -exec rm -rf {} +
