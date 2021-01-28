import yaml
filename = 'user_settings.yaml'
with open(filename, 'r', newline='') as myfile:
    try:
        print(yaml.load(myfile))
    except yaml.YAMLError as ymlexcp:
        print(ymlexcp)
