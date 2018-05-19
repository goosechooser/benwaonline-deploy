'''
tasks related to deploying new content
'''
from invoke import task
from . import git

@task
def move_file(c, fname, new_name):
    return c.run('mv {} {}'.format(fname, new_name))

@task
def backup(c, f, folder=False):
    r = '-r' if folder else ''
    return c.run('cp {r} {f} {f}.bak'.format(f=f, r=r))

@task
def move_static_contents(c, here, there):
    return c.run('cp -r {}/. {}'.format(here, there))