# Description
Repo to test the RabbitMQ® official tutorial functionalities.

# Installation
```
1. git clone ...
2. docker pull rabbit:3-management
3. docker run -d -p 15672:15672 -p 5672:5672 --name test-rabbit rabbitmq:3-management
4. create venv and install requirements (python -m venv venv && pip install -r requirements.txt)
4. cd to desired module folder and play with its corresponding producer and consumer files. There are comments available explaining each command.

If wanted to go to admin dashboard go to http://localhost:15675 and login as guest/guest.
```