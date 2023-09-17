#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

# Install Nginx if it not already installed
sudo apt-get update
sudo apt-get -y install nginx
mkdir /data
mkdir /data/web_static
mkdir /data/web_static/releases
mkdir /data/web_static/shared
mkdir /data/web_static/releases/test

# Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
echo -e "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
sudo chown -R ubuntu:ubuntu /data/

# Use alias inside your Nginx configuration
sudo sed -i "38i \\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
