PROJECTNAME=$(shell basename "$(PWD)")

all: docker run
	@ echo " >> creating all from $(PROJECTNAME)..."

run:
	@ echo " >>  running $(PROJECTNAME) app..."
	@ pip install -r requirements.txt
	@ sudo docker start questions
	@ sleep 0.1
	@ uvicorn app.main:app --reload

docker:
	@ echo " >>  making docker container $(PROJECTNAME)..."
	@ sudo docker compose up -d

# usage make migration-up ARGS="[version]" 
migration-up:
	@ echo " >>  making migrations"
	@ sudo docker start questions
	@ sleep 0.1
	@ cat schemas/$(ARGS)_init.up.sql | sudo docker exec -i questions  psql -U postgres -d postgres

# usage make migration-down ARGS="[version]" 
migration-down:
	@ echo " >>  making migrations"
	@ sudo docker start questions
	@ sleep 0.1
	@ cat schemas/$(ARGS)_init.down.sql | sudo docker exec -i questions  psql -U postgres -d postgres