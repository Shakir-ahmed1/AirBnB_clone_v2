#!/usr/bin/python3
""" a fabric script that deploys the current version of web_static """
from fabric.api import *
from os.path import exists

env.hosts = ['3.85.54.219', '3.85.136.250']


def do_deploy(archive_path):
    """ deployes the given archive """
    if not exists(archive_path):
        return False
    t1 = put(archive_path, "/tmp/")
    if t1.failed:
        return False
    file_name = archive_path.split('/')[-1]
    folder_name = file_name.split('.')[-2]
    run("mkdir -p /data/web_static/releases/{}".format(folder_name))
    t2 = run(
        "tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(file_name, folder_name))
    if t2.failed:
        return False
    t3 = run("rm /tmp/{}".format(file_name))
    if t3.failed:
        return False
    t4 = run("mv /data/web_static/releases/{}/web_static/*  /data/web_static/releases/{}".format(folder_name, folder_name))
    t5 = run("rm -r  /data/web_static/releases/{}/web_static".format(folder_name))
    t6 = run("rm -rf /data/web_static/current")
    if t6.failed:
        return False
    t7 = run(
        "ln -sf /data/web_static/releases/{} /data/web_static/current".format(folder_name))
    if t7.failed:
        return False
    t8 = run("service nginx restart")
    return True
