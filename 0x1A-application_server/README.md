# 0x1A. Application server

## Background Context

Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project, you will add this piece to your infrastructure, plug it into your Nginx, and make it serve your Airbnb clone project.

## Resources

- (Application server vs web server)[https://www.nginx.com/resources/glossary/application-server-vs-web-server/]
- (How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04)[https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04]
- (Running Gunicorn)[https://docs.gunicorn.org/en/latest/run.html]
- (Be careful with the way Flask manages slash in route - strict_slashes)[https://werkzeug.palletsprojects.com/en/3.0.x/en/0.14.x/routing/]
- (Upstart documentation)[https://doc.ubuntu-fr.org/upstart]
## Requirements

- A README.md file, at the root of the folder of the project, is mandatory.
- Everything Python-related must be done using python3.
- All config files must have comments.

### Bash Scripts
- All your files will be interpreted on Ubuntu 16.04 LTS.
- All your files should end with a new line.
- All your Bash script files must be executable.
- Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error.
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash.
- The second line of all your Bash scripts should be a comment explaining what is the script doing.

### Tasks

#### 0. Set up development with Python

Requirements:

- Make sure that task #3 of your SSH project is completed for web-01. The checker will connect to your servers.
- Install the net-tools package on your server: sudo apt install -y net-tools
- Git clone your AirBnB_clone_v2 on your web-01 server.
- Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000.
- Your Flask application object must be named app (This will allow us to run and check your code).

#### 1. Set up production with Gunicorn

Requirements:

- Install Gunicorn and any other libraries required by your application.
- The Flask application object should be called app. (This will allow us to run and check your code).
- You will serve the same content from the same route as in the previous task.
- You can verify that it’s working by binding a Gunicorn instance to localhost listening on port 5000 with your application object as the entry point.

#### 2. Serve a page with Nginx

Requirements:

- Nginx must serve this page both locally and on its public IP on port 80.
- Nginx should proxy requests to the process listening on port 5000.
- Include your Nginx config file as 2-app_server-nginx_config.

#### 3. Add a route with query parameters

Requirements:

- Nginx must serve this page both locally and on its public IP on port 80.
- Nginx should proxy requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to a Gunicorn instance listening on port 5001.
- Include your Nginx config file as 3-app_server-nginx_config.

#### 4. Let's do this for your API

Requirements:

- Git clone your AirBnB_clone_v3.
- Setup Nginx so that the route /api/ points to a Gunicorn instance listening on port 5002.
- Nginx must serve this page both locally and on its public IP on port 80.
- To test your setup you should bind Gunicorn to api/v1/app.py.
- Upload your Nginx config file as 4-app_server-nginx_config.
#### 5. Serve your AirBnB clone

Requirements:

- Git clone your AirBnB_clone_v4.
- Your Gunicorn instance should serve content from web_dynamic/2-hbnb.py on port 5003.
- Setup Nginx so that the route / points to your Gunicorn instance.
- Setup Nginx so that it properly serves the static assets found in web_dynamic/static/ (essential for your page to render properly).
- For your website to be fully functional, reconfigure web_dynamic/static/scripts/2-hbnb.js to the correct IP.
- Nginx must serve this page both locally and on its public IP and port 5003.
- Make sure to pull up your Developer Tools on your favorite browser to verify that you have no errors.
- Upload your Nginx config as 5-app_server-nginx_config.

#### 6. Deploy it!

Requirements:

- Write a systemd script which starts a Gunicorn process to serve the same content as the previous task (web_dynamic/2-hbnb.py).
- The Gunicorn process should spawn 3 worker processes.
- The process should log errors in /tmp/airbnb-error.log.
- The process should log access in /tmp/airbnb-access.log.
- The process should be bound to port 5003.
- Your systemd script should be stored in the appropriate directory on web-01.
- Make sure that you start the systemd service and leave it running.
- Upload gunicorn.service to GitHub.

#### 7. No service interruption

Requirements:

- Write a simple Bash script to reload Gunicorn in a graceful way.
- The script should tell the master Gunicorn to renew all the workers.
- Test it using the command $ sudo reboot to reboot your server (not shutdown!!).

### Conclusion
This project aims to set up a robust web infrastructure using Nginx and Gunicorn, ensuring the seamless deployment of a dynamic web application with minimal downtime. Follow the instructions in each task carefully to achieve the desired configuration.
