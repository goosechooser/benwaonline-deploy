'''
git related tasks
'''
from invoke import task
from pathlib import PurePosixPath

@task
def clone(c, url, dir):
    result = c.run('git clone {} {}'.format(url, dir), warn=True)
    return result

@task
def init_bare(c, dir):
    c.run('mkdir {}'.format(dir))
    with c.cd(dir):
        return c.run('git init --bare')

@task
def pull(c, url, work_tree=None, git_dir=None):
    work_tree = '--work-tree={}'.format(work_tree) if work_tree else ''
    git_dir = '--git-dir={}'.format(git_dir) if git_dir else ''

    return c.run('git {} {} pull {}'.format(work_tree, git_dir, url))

@task
def fetch(c, branch=None):
    branch = branch if branch else ''
    return c.run('git fetch origin {}'.format(branch), warn=True)

@task
def checkout(c, branch, work_tree=None, git_dir=None):
    work_tree = '--work-tree={}'.format(work_tree) if work_tree else ''
    git_dir = '--git-dir={}'.format(git_dir) if git_dir else ''

    return c.run('git {} {} checkout -f {}'.format(work_tree, git_dir, branch))

@task
def last_commit(c, fname):
    result = c.run('git log --abbrev-commit -- {} | head -1 | cut -d\  -f2'.format(fname))
    return result.stdout.strip()