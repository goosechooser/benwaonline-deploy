'''
tasks related to deploying new content
'''
from invoke import task

@task
def update_staticfile(c, fname, new_name):
    return c.run('mv {} {}'.format(fname, new_name))