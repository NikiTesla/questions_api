PROJECTNAME=$(shell basename "$(PWD)")

run:
	@ echo " >>  running $(PROJECTNAME) app..."
	@ sudo docker start fastapi_test
	@ sleep 0.1
	@ uvicorn app.main:app --reload

docker:
	@ echo " >>  making docker container $(PROJECTNAME)..."
	@ sudo docker compose up

# usage make migration-up ARGS="[version]" 
migration-up:
	@ echo " >>  making migrations"
	@ sudo docker start fastapi_test
	@ sleep 0.1
	@ cat schemas/$(ARGS)_init.up.sql | sudo docker exec -i fastapi_test  psql -U postgres -d postgres

# usage make migration-down ARGS="[version]" 
migration-down:
	@ echo " >>  making migrations"
	@ sudo docker start fastapi_test
	@ sleep 0.1
	@ cat schemas/$(ARGS)_init.down.sql | sudo docker exec -i fastapi_test  psql -U postgres -d postgres