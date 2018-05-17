from fabric import Connection
from fabfiles import git, env, deploy

if __name__ == '__main__':

    repo = {
        'git-dir': '/home/vagrant/benwaonline-prod',
        'work-tree': '/home/vagrant/mock-prod/',
        'url': 'https://github.com/goosechooser/benwaonline.git',
        'branch': 'development'
    }

    c = Connection('vagrant')
    css = 'benwaonline/static/css/style.css'

    # update git-dir/work-tree
    with c.cd(repo['git-dir']):
        git.fetch(c, repo['url'])
        git.checkout(c, repo['branch'], git_dir=repo['git-dir'], work_tree=repo['work-tree'])

    # below is the actual deploy stuff
    with c.cd(repo['git-dir']):
        lc_file = git.last_commit(c, css)

    with c.cd(repo['work-tree']):
        current_version = env.get(c, 'envtest', 'NICE')
        if lc_file != current_version:
            env.set(c, 'envtest', 'NICE', lc_file)
        with c.cd('benwaonline/static/css'):
            deploy.update_staticfile(c, 'style.css', lc_file)