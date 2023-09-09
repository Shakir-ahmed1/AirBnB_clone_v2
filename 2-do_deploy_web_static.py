#!/usr/bin/python3
""" a fabric script that deploys the current version of web_static """
from fabric.api import *


env.hosts = ['', '']
def do_deploy(archive_path):
	if not exists(archive_path):
		return False
	t1 = put(archive_path, "/tmp/")
	if t1.failed:
		return False
	file_name = archive_path.split('/')[-1]
	folder_name = file_name.split('.')[-2]
	t2 = run(f"tar -xzf /tmp/{file_name} -C "
		  "/data/web_static/releases/{folder_name}/")
	if t2.failed:
		return False
	t3 = run("rm /tmp/{file_name}")
	if t3.failed:
		return False
	t4 = run("mv /data/web_static/releases/{folder_name}/web_static/*"
		 "/data/web_static/releases/{folder_name}/")
	if t4.failed:
		return False
	t5 = run("rm -rf /data/web_static/releases/{folder_name}/web_static/")
	if t5.failed:
		return False
	t6 = run("rm -rf /data/web_static/current")
	if t6.failed:
		return False
	t7 = run("ln -s /data/web_static/releases/{folder_name}"
		 "/data/web_static/current")
	if t7.failed:
		return False
	return True
