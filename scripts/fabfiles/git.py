'''
git related tasks
'''
from invoke import task
from pathlib import PurePosixPath

@task
def clone(c, url):
    return c.run('git clone {}'.format(url), warn=True)

@task
def init_bare(c, dir):
    c.run('mkdir {}'.format(dir))
    with c.cd(dir):
        return c.run('git init --bare')

@task
def fetch(c, url):
    return c.run('git fetch {}'.format(url), warn=True)

@task
def checkout(c, branch, work_tree=None, git_dir=None):
    work_tree = '--work-tree={}'.format(work_tree) if work_tree else ''
    git_dir = '--git-dir={}'.format(git_dir) if git_dir else ''

    return c.run('git {} {} checkout -f {}'.format(work_tree, git_dir, branch))

@task
def last_commit(c, fname):
    result = c.run('git log --abbrev-commit -- {} | head -1 | cut -d\  -f2'.format(fname))
    p = PurePosixPath(fname)
    mod_file = ''.join([p.stem, '_', result.stdout.strip(), p.suffix])

    return mod_file