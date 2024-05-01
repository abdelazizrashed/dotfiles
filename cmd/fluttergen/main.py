import os
from app.src import generate_data_classes
import argparse


parser = argparse.ArgumentParser(
                    prog='gendata',
                    description='Generate flutter data class from json file',
                    )
parser.add_argument('-j', "--json-annotation", action="store_true", help="Generate Json Annotation")
args = parser.parse_args()
files =   os.listdir()
for file in files:
    if ".json" in file:
        generate_data_classes(file,args.json_annotation)


