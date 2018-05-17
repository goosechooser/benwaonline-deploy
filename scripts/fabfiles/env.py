'''
tasks related to envfiles/envs
'''
from invoke import task
from pathlib import PurePosixPath

@task
def get(c, envfile, env):
    cmd = 'cat {envfile} | grep \'{env}\' | sed -e \'s/{env}=//\''.format(envfile=envfile, env=env)
    return c.run(cmd).stdout.strip()

def _gen_regex(env, value):
    return '\({env}\)\(=\)\(.*\)/\\1\\2{value}/'.format(env=env, value=value)

@task
def replace_env(c, envfile, regex):
    return c.run('sed -i -e \'s/{regex}\' {envfile}'.format(regex=regex, envfile=envfile))

@task
def set(c, envfile, env, value):
    r = _gen_regex(env, value)
    print('updated {}={} in {}'.format(env, value, envfile))
    return replace_env(c, envfile, r)


