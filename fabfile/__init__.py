from invoke import Collection
from . import env
from . import git
from . import pre_deploy
from . import deploy

ns = Collection()
ns.add_collection(env)
ns.add_collection(git)
ns.add_collection(deploy)
ns.add_collection(pre_deploy)
