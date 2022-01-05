import yaml

def yaml_loader(filepath):
    with open(filepath, 'r') as file_descriptor:
#add condition to validate yaml
        data = yaml.load(file_descriptor)
    return data