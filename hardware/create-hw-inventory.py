#!/usr/bin/python


""" retroinventoy - script to create hardware inventory
                    this script creates an empty inventory file

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License v3 for more details.
You should have received a copy of the GNU General Public License v3 along with
this program. If not, see http://www.gnu.org/licenses/gpl-3.0.txt.
"""

__author__ = "Jose Angel de Bustos Perez"
__authors__ = ["Jose Angel de Bustos Perez"]
__contact__ = "jadebustos@gmail.com"
__copyright__ = "Copyright 2021, ache4bits"
__credits__ = ["Jose Angel de Bustos Perez"]
__date__ = "2021/01/16"
__deprecated__ = False
__email__ =  "jadebustos@gmail.com"
__license__ = "GPLv3"
__maintainer__ = "Jose Angel de Bustos Perez"
__status__ = "WIP"
__version__ = "0.0.1"

import argparse
import uuid
import yaml
import io
import os

def mandatory_fields(model):

    # create random item id
    model['id'] = str(uuid.uuid4())

    # required fields (string)
    #   - manufacturer: string
    #   - model: string
    #   - serial: string
    #   - country: string
    #   - family: string (MSX|Spectrum|Amstrad| ...)
    #   - type: string (computer, mouse, ...)
    mandatory_keys_string = ['manufacturer', 'model', 'serial', 'country', 'family', 'type']

    for item in mandatory_keys_string:
        model[item] = 'string'

    # required fields (boolean)
    #   - boxed: boolean
    #   - mint: boolean (mint condition)
    #   - sealed: boolean (sealed, unboxed)
    #   - working: boolean (working condition)
    mandatory_keys_boolean = ['boxed', 'mint', 'sealed', 'working']

    for item in mandatory_keys_boolean:
        model[item] = False

    return model

def optional_fields(model):
    # optional fields
    # aditional comments
    model['comments'] = ['optional (string)', 'optional (string)']

    # add relationed items, as adapters, mouse, ...
    children1 = {}
    children1['id'] = str(uuid.uuid4())
    children1['description'] = 'children 1 description'
    children2 = {}
    children2['id'] = str(uuid.uuid4())
    children2['description'] = 'children 2 description'
    model['children'] = [ ]
    model['children'].append(children1)
    model['children'].append(children2)

    # manuals
    model['manuals'] = ['optional (manual title)', 'optional (manual title)']

    # optional fields for specs
    #   - cpuvendor: string
    #   - cpumodel: string
    #   - cpucount: string
    #   - cpubits: string
    #   - cpuspeed: string
    #   - memory: string
    #   - interface: string
    model['specs'] = {}
    mandatory_keys_specs = ['cpuvendor', 'cpumodel', 'cpubits', 'cpuspeed', 'memory', 'interface']

    for item in mandatory_keys_specs:
        model['specs'][item] = 'string'

    return model

def create_model():

    model = {}
    # add mandatory fields
    model = mandatory_fields(model)
    model = optional_fields(model)

    return model

def main():
    # Program description
    descr = 'Create  hardware inventory from a directory.'

    # Initiate the parser with a description
    parser = argparse.ArgumentParser(description=descr)

    # arguments definition
    parser.add_argument("--filename", "-f", help="filename to create the inventory file", required=True)
    parser.add_argument("--directory", "-d", help="directory where the inventory file will be created", required=True)

    # parsing arguments
    args = parser.parse_args()

    # create empty data model
    data = create_model()

    # Write YAML file
    filename = os.path.join(args.directory, args.filename)
    with io.open(filename, 'w', encoding='utf8') as outfile:
      yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)

if __name__ == "__main__":
    main()