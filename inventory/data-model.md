# Data model

There are several files which contains the data model:

+ The file [data.py](data.py) contains the common data por all the items and for hardware and software item.
+ The file [modules/familiy.py](modules/family.py) creates a python directory for the family (dictionary key):
  ```json
  {
    "description": {
      "boxed": false,
      "family": "MSX",
      "subfamily": "MSX",
      "manufacturer": "",
      "mint": false,
      "model": "",
      "sealed": false,
      "serial": "",
      "working": true
    },
    "id": "d5f46542-b7d7-4364-b383-c58609c48f90",
    "type": "hardware",
    "specs": {
      "cpubits": "8",
      "cpuvendor": "Zilog",
      "cpumodel": "Z80A",
      "cpuspeed": "3.58 MHz",
      "ram": "64 KB",
      "vram": "16 KB",
      "rom": "32 KB"
    },
    "pictures": [
      "picture1.png",
      "picture2.png"
    ],
    "comments": [
      "comment 1",
      "comment 2"
    ]
  }
  ```
+ To create the family data there is a python file for each family in **modules** directory. These files creates the data for the family, a default data which is created and populated when the inventory is created. After the individual inventory is created this data can be modified in the yaml to match the item data.

## Adding new family data

To add data to the existing families add data to the specific file.

To add a new family add a file with the family data.