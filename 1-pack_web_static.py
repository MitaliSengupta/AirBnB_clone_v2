#!/usr/bin/python3
"""
    Script generates a .tgz archive from web_static folder
"""


def do_pack():
    """
        Function creates a .tgz archive from all files in web_static folder
        Each archive will be stored in versions folder
        Archive name:
            web_static_<year><month><day><hour><minute><second>.tgz
        Returns:
            archive path if successful
            None if fail
    """
    from fabric.operations import local
    from datetime import datetime

    name = "./versions/web_static_{}.tgz"
    name = name.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    create = local("tar -cvzf {} web_static".format(name))
    if create.succeeded:
        return name
    else:
        return None

if __name__ == "__main__":
    do_pack()
