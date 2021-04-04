#!/usr/bin/python

""" inventoy - script to create an inventory
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
import sys
import io
import os

from modules.family import families

import json

def menu(subfamilies):
    option = -1
    while( option < 0 or option > len(subfamilies)):
      print("Choose subfamily:")
      for i in range(len(subfamilies)):
        print("\t%d - %s" % (i, subfamilies[i]))
      try:
        option = int(input("Option: "))
      except:
        option = -1

    return subfamilies[option]

def main():
    # Program description
    descr = 'Create  inventory file'

    # Initiate the parser with a description
    parser = argparse.ArgumentParser(description=descr)

    # arguments definition
    type = ['hardware', 'software']
    family = list(families.keys())
    parser.add_argument("--type", "-t", help="item type", action="store", choices=['hardware', 'software'], required=True)
    parser.add_argument("--family", "-f", help="item family", action="store", choices=families, required=True)
    parser.add_argument("--name", "-n", help="filename to create the inventory file", required=True)
    parser.add_argument("--directory", "-d", help="directory where the inventory file will be created", required=True)

    # parsing arguments
    args = parser.parse_args()

    # subfamily
    subfamilies = list(families[args.family].keys())

    # ask for subfamily
    option = menu(subfamilies)

    # item
    item = families[args.family][option]

    # create random uuid for item
    item['id'] = str(uuid.uuid4())
    item['type'] = args.type
    item['description']['family'] = args.family
    item['description']['subfamily'] = option
    print(json.dumps(item, indent=2))
    # Write YAML file
    filename = os.path.join(args.directory, args.name)
    with io.open(filename, 'w', encoding='utf8') as outfile:
      yaml.dump(item, outfile, default_flow_style=False, allow_unicode=True)

if __name__ == "__main__":
    main()