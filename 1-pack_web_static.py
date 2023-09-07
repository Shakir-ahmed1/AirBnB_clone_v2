#!/usr/bin/python3
""" compreses the files in web_static into .tgz archive """
import os
import tarfile
from datetime import datetime

def do_pack():
    """ packs the web_static folder into .tgz archive"""
    n = datetime.now()
    y, m, d = n.year, n.month, n.day
    h, mn, s = n.hour, n.minute, n.second
    output_path = "web_static_{}{:02d}{:02d}{:02d}{:02d}{:02d}.tgz".format(
                   y,m,d,h,mn,s)
    with tarfile.open(output_path, "w:gz") as tar:
        for root, dirs, files in os.walk("web_static"):
            for file in files:
                tar.add(os.path.join(root, file), arcname=file)
            for dir in dirs:
                tar.add(os.path.join(root, dir), arcname=dir)
