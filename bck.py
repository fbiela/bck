#!/usr/bin/env python
#-*- coding: utf-8 -*- 
#

import hashlib
import os
import sqlite3
from datetime import date, datetime, time

# import
import click


@click.command()

# opcao -n
@click.option('-n', default = None, help = 'Para nomear o backup.')

# opcao -l
@click.option('-l', default = None, help = 'Para definir o caminho da pasta.')


# functions
def cli(n, l):
    """ backup with 7zip and python. Frederico Sales <fredericosales@globo.com>."""

    """ connect to sqlite3 db """
    path = "/home/frederico/public/db/bck/bck.db"
    conn = sqlite3.connect(path)
    c = conn.cursor()

    """ backup  """
    data = datetime.now()
    agora = data.strftime("_%d-%m-%Y_%H:%m.7z")

    if n != None and l != None:
        backup = n + agora
        cmd = "7z a " + backup + " "  +  l

        # faz o backup
        os.system(cmd)

        # md5sum apos backup
        soma = "md5sum " + backup
        os.system(soma)

        # move bck para pasta de backup
        mpath = "mv " + os.getcwd() + "/" + backup + " $HOME/public/backup"
        os.system(mpath)

        # checka md5 para o db
        arquivo = "/home/frederico/public/backup/" + backup
        md = open(arquivo, 'rb').read()
        check = hashlib.md5(md).hexdigest()

        SQL = [data.strftime("%d-%m-%Y %H:%m"), backup, l, check]
        c.execute("INSERT INTO backup (data, name, path, md5) VALUES (?, ?, ?, ?)", SQL)
        conn.commit()
        c.close()
        click.echo('Backup realizado com sucesso.')
    else:
        click.echo("Erro: faltam argumentos verifique se utilizou: 'bck -n nome -l caminho'")


if __name__ == "__main__":
    cli()
