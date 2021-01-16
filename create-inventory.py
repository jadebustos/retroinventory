#!/usr/bin/python

""" retroinventoy - script to create inventory

This scripts scans one directory an creates a directory inventory.

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
import hashlib
import json
#import yaml
import glob
import os

# function that reads a file a returns its sha512 hash
def get_file_hash(file):
    # blocks to read from file
    BLOCK_SIZE = 65536

    # create hash object
    file_hash = hashlib.sha512()

    # reading file
    with open(file, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)

    return file_hash.hexdigest()

def main():
    # Program description
    descr = 'Create  a inventory from a directory.'

    # Initiate the parser with a description
    parser = argparse.ArgumentParser(description=descr)

    # arguments definition
    parser.add_argument("--directory", "-d", help="directory to scan", required=True)
    parser.add_argument("--extension", "-e", help="file extension to analyze", required=True)
    parser.add_argument("--filename", "-f", help="filename to store the inventory", required=True)
    parser.add_argument("--threads", "-t", help="number of threads", default=1)  

    # parsing arguments
    args = parser.parse_args()

    # get directory list
    directory_list = glob.glob(os.path.join(args.directory, "*." + args.extension))
    
    # inventory
    inventory = {}

    # creating inventory
    for item in directory_list:
        key = os.path.basename(item)
        inventory[key] = {}
        inventory[key]['path'] = item
        inventory[key]['sha512'] = get_file_hash(item)
        inventory[key]['size'] = os.path.getsize(item)

    # create yaml
    inventory_filename = os.path.join(args.directory,args.filename)
    pt = open(inventory_filename, 'w')
    #yaml.dump(inventory, pt, allow_unicode=True)
    json.dump(inventory, pt, indent=2)
    pt.close()

if __name__ == "__main__":
    main()
