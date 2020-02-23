import os
import json
import yaml
import argparse


def convert_to_yaml(inputFile, filename, outputDirectory):
    if os.path.isdir(outputDirectory):
        yamlFilePath = outputDirectory + \
            os.path.sep + "{}.yml".format(filename)
    with open(inputFile, 'r') as file:
        content = yaml.safe_dump(json.load(file), default_flow_style=False)
        with open(yamlFilePath, 'w') as yamlfile:
            yamlfile.write(content)
            yamlfile.close()
        file.close()


def convert_to_json(inputFile, filename, outputDirectory):
    if os.path.isdir(outputDirectory):
        jsonFilePath = outputDirectory + \
            os.path.sep + "{}.json".format(filename)
    with open(inputFile, 'r') as file:
        content = json.dumps(yaml.load(file, Loader=yaml.FullLoader))
        with open(jsonFilePath, 'w') as jsonfile:
            jsonfile.write(content)
            jsonfile.close()
        file.close()


def main():
    """
    Main method
    """
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", type=str,
                        help="type of the file format {json|yaml}", default="json")
    parser.add_argument("-n", "--name", type=str,
                        help="name of the output file", default="test")
    parser.add_argument("-f", "--file", type=str,
                        help="Absolute path of the file")
    parser.add_argument("-o", "--output", type=str,
                        help="Absolute path of the destination directory", default=str(os.getcwd()))
    args = parser.parse_args()

    if args.type == "json" and args.file.endswith('json'):
        convert_to_yaml(args.file, args.name, args.output)
    elif args.type == "yaml" and (args.file.endswith('yml') or args.file.endswith('yaml')):
        convert_to_json(args.file, args.name, args.output)
    else:
        print("Invalid File format")


if __name__ == "__main__":
    main()
