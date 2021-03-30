#!/usr/bin/python


""" retroinventoy - script to create hardware inventory

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
import yaml
import io

def main():
    # Program description
    descr = 'Create  hardware inventory from a directory.'

    # Initiate the parser with a description
    parser = argparse.ArgumentParser(description=descr)

    # arguments definition
    parser.add_argument("--filename", "-f", help="filename to store the inventory", required=True)
    parser.add_argument("--threads", "-t", help="number of threads", default=1)  

    # parsing arguments
    args = parser.parse_args()
    data = ''
    with open(args.filename, 'r') as stream:
      try:
        data = yaml.safe_load(stream)
      except yaml.YAMLError as exc:
        print(exc)

    print(data)

    # Write YAML file
    with io.open('data.yaml', 'w', encoding='utf8') as outfile:
      yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)

if __name__ == "__main__":
    main()