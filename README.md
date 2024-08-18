# To Run application

## Start and SSH into Vagrant VM 

```
vagrant up
vagrant ssh servidorWeb
```

## Run the webApp

```
cd /home/vagrant/frontend
export FLASK_APP=run.py
/usr/local/bin/flask run --host=0.0.0.0 --port 5001
```

## Run the Users Microservice

```
cd /home/vagrant/microUsers
export FLASK_APP=run.py
/usr/local/bin/flask run --host=0.0.0.0 --port 5002
```

## Run the Products Microservice

```
cd /home/vagrant/microProducts
export FLASK_APP=run.py
/usr/local/bin/flask run --host=0.0.0.0 --port 5003
```

## Run the Oders Microservice

```
cd /home/vagrant/microOrders
export FLASK_APP=run.py
/usr/local/bin/flask run --host=0.0.0.0 --port 5004
```
