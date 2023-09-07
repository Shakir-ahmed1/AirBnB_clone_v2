#!/usr/bin/python3
# Import Fabric's API module
""" generates archive from web_static folder """
from datetime import datetime
from fabric.api import *
archive_name = "web_static_{}.tgz".format(
    datetime.now().strftime("%Y%m%d%H%M%S"))


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
