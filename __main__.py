import os
import json
import sys

assert len(sys.argv) == 3, 'You need to precise two arguments:\
     first the architecture name, second the project path.'

architecture_path = os.path.join(os.path.split(sys.argv[0])[0], 'structures')
architecture_name = sys.argv[1].split('.')[0] + '.json'
path = sys.argv[2]


def create(value, path, name):

    if isinstance(value, str):
        os.system(f'touch ' + os.path.join(path, value))
        return

    if isinstance(value, dict):
        if not os.path.isdir(os.path.join(path, name)):
            os.system(f'mkdir ' + os.path.join(path, name))
        for key in value.keys():
            create(value[key], os.path.join(path, name), key)


project_path, project_name = os.path.split(path)
project_path = os.path.abspath(project_path)

with open(os.path.join(architecture_path, architecture_name)) as f:
    data = json.load(f)
    print(f'Creating project {project_name}...')
    create(data, project_path, project_name)
    print(f'Project created successfully in {project_path}!')