import sys
from fabric import Connection
from fabfile import deploy, utils

if __name__ == '__main__':
    hostname = sys.argv[1]
    config = utils.load_config('{}.yaml'.format(hostname))
    c = Connection(hostname)

    print('pushing new static files to production')
    with c.cd(config['base-dir']):
        print('backing up envfile')
        deploy.backup(c, config['envfile'])
        print('backing up static')
        deploy.backup(c, 'static', folder=True)
        here = config['work-tree'] + config['staging-dir']
        deploy.move_static_contents(c, here, '.')