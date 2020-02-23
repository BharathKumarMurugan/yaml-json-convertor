# Convert YAML to JSON and vise versa

This python script converts **YAML to JSON** and **JSON to YAML**.

## Arguments:

`-h, --help      show this help message and exit <br/>
-i, --input     input file format - {json|yaml} <br/>
-f, --file      input absolute file path to convert`

## Positional Arguments:

`-f, --file      input absolute file path to convert <br/>
-i, --input     input file format - {json|yaml}`

## Examples:

* Display help message:
`python convert.py -h`

* Convert *JSON to YAML*:
`python convert.py -f /path/to/json/file -i json`

* Convert *YAML to JSON*:
`python convert.py -f /path/to/yaml/file -i yaml`
