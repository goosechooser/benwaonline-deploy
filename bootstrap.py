import sys
from fabric import Connection
from fabfile import utils, git

def cleanup(c, config):
    c.run('rm -rf {}'.format(config['base-dir']))

def setup(c, config):
    result = c.run('mkdir {}'.format(config['base-dir']))
    print(utils.lazy_log(result))

    with c.cd(config['base-dir']):
        git.init_bare(c, config['git-dir'])
        result = c.run('mkdir {}'.format(config['work-tree']))
        print(utils.lazy_log(result))

        with c.cd(config['git-dir']):
            result = c.run('git remote add origin {}'.format(config['git-url']))
            git.fetch(c)
            git.checkout(c, config['branch'], git_dir=config['base-dir'] + config['git-dir'], work_tree=config['base-dir'] + config['work-tree'])

        with c.cd(config['work-tree']):
            c.run('mkdir {}'.format(config['staging-dir']))
            c.run('cp {} {}'.format(config['envfile'], config['staging-dir'] + config['envfile']))

    print('Complete')

if __name__ == '__main__':
    hostname = sys.argv[1]
    config = utils.load_config('{}.yaml'.format(hostname))
    c = Connection(hostname)
    cleanup(c, config)
    print('bootstrapping {}'.format(hostname))
    setup(c, config)
