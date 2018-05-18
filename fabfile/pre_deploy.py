from invoke import task
from fabfile import git, env
from pathlib import PurePosixPath

@task
def update_repo(c, config):
    with c.cd(config['git-dir']):
        git.fetch(c, config['branch'])
        git.checkout(c, config['branch'], git_dir=config['base-dir'] + config['git-dir'], work_tree=config['base-dir'] + config['work-tree'])

def format_last_commit(f, commit):
    p = PurePosixPath(f)
    return ''.join([p.stem, '_', commit, p.suffix])

def update_file(c, config, f):
    with c.cd(config['git-dir']):
        full = config['static_path'] + f['name']
        last = git.last_commit(c, full)

    lc_file = format_last_commit(f['name'], last)

    with c.cd(config['work-tree']):
        staging_env = config['staging-dir'] + config['envfile']
        current_version = env.get(c, staging_env, f['env'])
        if lc_file != current_version:
            print('now updating {}'.format(f['name']))
            env.set(c, staging_env, f['env'], lc_file)
            c.run('cp {} {}'.format(config['static_path'] + f['name'], config['staging-dir'] + lc_file))
        else:
            print('{} already updated'.format(f['name']))
