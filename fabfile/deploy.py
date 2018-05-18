'''
tasks related to deploying new content
'''
from invoke import task
from . import git

@task
def move_file(c, fname, new_name):
    return c.run('mv {} {}'.format(fname, new_name))

@task
def push_to_prod(c):
    pass
