"""Import."""
from database import session, Backup, _Loc
import click
import os
import hashlib

# backup

# click
@click.command()

# -n
@click.option('-n', default = None, help = 'backup name.')

# -l
@click.option('-l', default = None, help = 'backup path.')

def cli(n, l):
    """
    backup with 7zip and python
    Frederico Sales <fredericosales@globo.com>.
    Use:
    bck -n backupname -l path/folder/.../folder
    """
    _date = datetime.now
    _now = _date().strftime("_%d-%m-%Y_%H:%m.7z")

    if n != None and l != None:
        _bck = n + _now
        cmd = "7z a " + _bck + " " + l
        os.system(cmd)

        # md5sum
        md5sum = "md5sum " + _bck
        os.system(md5sum)

        # move backup to url
        _bck_path = config.get("BACKUP", "BACKUP_PATH")
        _mv = "mv " + os.getcwd() + "/" + _bck + " " + _bck_path

        # md5sum to db
        _file = _bck_path + "/" + _bck
        md = open(_file, 'rb').read()
        check = hashlib.md5(md).hexdigest()

        _bck_ = Backup(name = _bck, path= l, md5 = chech)
        session.add(_bck_)
        session.commit()
        session.close()

        click.echo('backup ends successfully.')
    else:
        click.echo('catastrophic failure.')
