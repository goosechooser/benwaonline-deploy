import sys
from fabric import Connection
from fabfile import pre_deploy, utils

if __name__ == '__main__':
    hostname = sys.argv[1]
    config = utils.load_config('{}.yaml'.format(hostname))
    c = Connection(hostname)

    print('updating,,,')
    with c.cd(config['base-dir']):
        pre_deploy.update_repo(c, config)

        for f in config['static_files']:
            pre_deploy.update_file(c, config, f)

    print('done updating static files')
