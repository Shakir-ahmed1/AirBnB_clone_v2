#!/usr/bin/env bash
# prepring webservers for static deployment
sudo apt-get update
sudo apt-get install -y nginx

# start nginx server
sudo service nginx start

# creating directories
mkdir /data
mkdir /data/web_static
mkdir /data/web_static/releases
mkdir /data/web_static/shared
mkdir /data/web_static/releases/test
echo -e "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
#create symbolic link. if exists recreate it
sudo unlink /data/web_static/current || true && sudo ln -s /data/web_static/releases/test/ /data/web_static/current
#give ownership
sudo chown -hR ubuntu:ubuntu /data
hbnbstatic="server_name _;\n\tlocation /hbnb_static{\n\talias \/data\/web_static\/current\n}"
# nginx conf: serving shakir.tech/hbnb_static from /data/web_static/current
sudo sed -i "s/server_name _;/$hbnbstatic/" /etc/nginx/sites-enabled/default
sudo service nginx reload
