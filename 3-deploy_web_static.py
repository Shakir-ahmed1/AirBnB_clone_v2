#!/usr/bin/python3
# Import Fabric's API module
""" generates archive from web_static folder """
from datetime import datetime
from fabric.api import local, put, env, run
from os.path import exists
archive_name = "web_static_{}.tgz".format(
    datetime.now().strftime("%Y%m%d%H%M%S"))

env.hosts = ['3.85.54.219', '3.85.136.250']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    local("mkdir -p versions")
    result = local("tar -cvzf versions/{} web_static".format(archive_name))
    if result.succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None


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
    t6 = run("rm -rf /data/web_static/current")
    if t6.failed:
        return False
    t7 = run(
        "ln -s /data/web_static/releases/{} /data/web_static/current".format(folder_name))
    if t7.failed:
        return False
    return True


def deploy():
    """ packs and deploys the archive"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
