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

#create symbolic link. if exists recreate it
if [ -e /data/web_static/current ]; then
         rm /data/web_static/current;
fi
ln -sf /data/web_static/releases/test/ /data/web_static/current;

#give ownership
sudo chown -hR ubuntu:ubuntu /data

# nginx conf: serving shakir.tech/hbnb_static from /data/web_static/current
sudo sed -i "38i \\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
