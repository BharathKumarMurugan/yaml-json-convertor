# Convert YAML to JSON and vise versa

This python script converts **YAML to JSON** and **JSON to YAML**.

## Usage
<pre>
usage: convert.py [-h] [-t TYPE] [-n NAME] [-f FILE] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -t TYPE, --type TYPE  type of the file format {json|yaml}
  -n NAME, --name NAME  name of the output file
  -f FILE, --file FILE  Absolute path of the file
  -o OUTPUT, --output OUTPUT
                        Absolute path of the destination directory
</pre>

* Display help message:
`python convert.py -h`

* Convert *JSON to YAML*:
`python convert.py -t json -n myfile -f /path/to/json/file -o /path/to/save`

* Convert *YAML to JSON*:
`python convert.py -t yaml -n myfile -f /path/to/yaml/file -o /path/to/save`
