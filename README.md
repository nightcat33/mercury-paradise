# Mercury Paradise #

A repo for backend development

Development setup guide
-----------------------
To bring the project online:
```
docker-compose up
```
To "ssh" into one of the containers:
```
docker-compose exec <container name> bash
```
To remove all containers:
```
docker-compose rm
```

Generate Documentation For Python
---------------------------------
To Generate documentation for python

```
cd mercury-paradise/server-flask/docs
sphinx-apidoc -f -o source ../src
cd mercury-paradise/server-flask/docs
make clean
make html
```
 
