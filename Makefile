.PHONY: idb seed flask-init-db run

# init DB
init-db: idb
idb: dropcreatedb flask-init-db seed

flask-init-db:
	flask init-db

dropcreatedb:
	dropdb fullgraph_alchemist
	createdb fullgraph_alchemist

seed:
	%(PYTHON) flask seed

run:
	FLASK_ENV=development flask run --reload --without-threads