# Sanic & Nginx & docker-compose example
# About
Simple and easy to use skeleton-project using [Sanic] behined [nginx].


Using docker and docker-compose to orchestrate everything.

The app is based on the (great) blog-post for flask:
https://realpython.com/blog/python/dockerizing-flask-with-compose-and-machine-from-localhost-to-the-cloud/

# How to run?
  - git clone the project 
  - Start a new docker-machine:
  `docker-machine create -d virtualbox sanic;`
  - Attach to the machine:
    `eval "$(docker-machine env sanic)"`
  - Build the containers (This will take a while for the first time!):
  `docker-compose build`
  - Create and start containers:
    `docker-compose up -d`

## Ok what now?
  - Use `docker-machine ip sanic` to get the machine IP
  - Go to `MACHINE-IP/hello-world` or  `MACHINE-IP/static/index.html` and validate everything worked.
  - That's It!
  
## Features:
  - /static/* files are served using the nginx.
  - Use the .env file to override or add config values (i override the logo):
    - Just add SANIC_ prefix before var name.

### Development

Want to contribute? Great!
Feel free to open PR/Issue :)

License
----

MIT - **Free Software, Hell Yeah!**

[//]: #URLs

   [sanic]: <https://github.com/channelcat/sanic>
   [nginx]: <https://www.nginx.com/resources/wiki/>
    
