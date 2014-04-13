#Scaffolding - Vagrant, Python(3.4), Flask, Mongodb

## Prerequisites

### Install VirtualBox
Download from: [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)

### Install Vagrant 1.5.x
http://www.vagrantup.com/downloads.html

### Install Vagrant plugins
* Omnibus: `vagrant plugin install vagrant-omnibus`
* Berkshelf: `vagrant plugin install vagrant-berkshelf --plugin-version 2.0.0.rc2`


## Setup
The following steps will help you setup a development environment.

```
### boot up vagrant 
$ vagrant up

### ssh into vagrant
$ vagrant ssh

### go to source directory
$ cd /vagrant

### create virtual environment (make sure you delete the old venv directory if there is one)
$ pyvenv-3.4 --without-pip venv

### activate virtual environment
$ source venv/bin/activate

### download and install pip
$ wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
$ python3.4 get-pip.py

### install packages
$ pip3.4 install -r requirements.txt

### run app
$ python3.4 manage.py runserver
```

At this point, you are all set.

There is a local mongo instance installed on the vagrant environment.

You can perform regular mongo comment through shell after you ssh into vagrant.


## Usage
### Vagrant
* Boot the VM: `vagrant up`.
* SSH into the VM: `vagrant ssh`

### Source directory
`cd /vagrant`

### Activate virtual environment
`source venv/bin/activate`

### Run app 
You can run the app using one of the following commands
```
### through manage.py
python3.4 manage.py runserver

### running directly
python3.4 app.py
```

### Interact with the app
In vagrant:
```
### open a terminal, ssh into vagrant
$ vagrant ssh

### curl against localhost
$ curl -v -X GET "http://localhost:5000/"

### you shall see JSON response back
```
On your local machine
```
### open a terminal
### curl against vagrant ip
$ curl -v -X GET "http://192.168.33.10:5000/"

### you shall see the same JSON response
```

### Install new python package
```
### install package
$ pip3.4 install <package-name>

### compare with existing requirements
$ pip3.4 freeze -r requirements.txt

### If you see anything listed below 
###     $ ## The following requirements were added by pip --freeze:
### please add them into requirements.txt with format:
###     - Why we need it
###     - License
###     - Upstream url
```


## Background Notes
Here are some background info if you are interested.

- Berkshelf is a package management system. Provides a consistent environment for projects by tracking and installing the exact packages and versions that are needed.

- Chef is an automation platform that transforms infrastructure into code. It Manage a Cookbook or an Application's Cookbook dependencies

- vagrant-omnibus is a Vagrant plugin that ensures the desired version of Chef is installed via the platform-specific Omnibus packages

- vagrant-berkshelf is a Vagrant plugin to add Berkshelf integration to the Chef provisioners.
