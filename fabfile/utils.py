from yaml import load

def load_config(fname):
    with open(fname, 'r') as f:
        return load(f)

# Turn this into a decorator bruh
def lazy_log(result):
    return '{.command}'.format(result)