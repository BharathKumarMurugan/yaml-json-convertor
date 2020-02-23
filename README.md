# Convert YAML to JSON and vise versa

This python script converts **YAML to JSON** and **JSON to YAML**.

## Usage

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
