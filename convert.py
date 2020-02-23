import os
import json
import yaml
import sys
import getopt

def convert_to_yaml(inputFile):
    yamlFilePath = os.path.dirname(
        os.path.abspath(__file__)) + os.path.sep + "test.yml"
    with open(inputFile, 'r') as file:
        content = yaml.safe_dump(json.load(file), default_flow_style=False)
        with open(yamlFilePath, 'w') as yamlfile:
            yamlfile.write(content)
            yamlfile.close()
        file.close()


def convert_to_json(inputFile):
    jsonFilePath = os.path.dirname(os.path.abspath(
        __file__)) + os.path.sep + "test.json"
    with open(inputFile, 'r') as file:
        content = json.dumps(yaml.load(file, Loader=yaml.FullLoader))
        with open(jsonFilePath, 'w') as jsonfile:
            jsonfile.write(content)
            jsonfile.close()
        file.close()


def foo_help():
    bar = """
    arguments:
    ----------
    -h, --help      show this help message and exit
    -i, --input     input file format - {json|yaml}
    -f, --file      input absolute file path to convert

    positional arguments:
    ---------------------
    -f, --file      input absolute file path to convert
    -i, --input     input file format - {json|yaml}

    examples:
    ---------
    display this help message:
    python convert.py -h

    convert json file to yaml:
    python convert.py -f /path/to/json/file -i json

    convert yaml to json:
    python convert.py -f /path/to/yaml/file -i yaml
    """
    print(bar)


if __name__ == "__main__":
    cmdArg = sys.argv
    argumentsList = cmdArg[1:]
    unixOptions = "hi:f:"
    gnuOptions = ["help", "input=", "file"]
    try:
        arguments, values = getopt.getopt(
            argumentsList, unixOptions, gnuOptions)
    except getopt.error as err:
        print(str(err))
        sys.exit(1)

    for cArg, cVal in arguments:
        if cArg in ("-h", "--help"):
            foo_help()
            exit(0)
        elif cArg in ("-f", "--file"):
            if os.path.isfile(cVal):
                inputFile = cVal
            else:
                print("File does not exists")
                exit(1)
        elif cArg in ("-i", "--input"):
            if cVal == "json":
                convert_to_yaml(inputFile)
                exit(0)
            if cVal == "yaml":
                convert_to_json(inputFile)
                exit(0)
