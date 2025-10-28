start:
	python -m main
makemigrations: 
	alembic revision --autogenerate -m "$(m)"
migrate:
	alembic upgrade head