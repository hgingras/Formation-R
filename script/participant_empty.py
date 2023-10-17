#!/usr/bin python3

import json
import os
import argparse

def to_empty(cell):
    code_cell = cell['cell_type'] == 'code'
    to_empty = 'empty' in cell['metadata'].get('tags', [])
    return code_cell and to_empty

def main(args):
    for file in args.FILES:
        content = json.load(file)

        for cell in filter(to_empty, content['cells']):
                cell['source'] = []

        outname = file.name if args.inplace else + 'new-' + file.name
        with open(outname, 'w', encoding="UTF-8") as out:
            json.dump(content, out, indent=1, ensure_ascii=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("FILES", nargs='+', type=argparse.FileType('r'))
    parser.add_argument("-i", "--inplace", action='store_true')

    main(parser.parse_args())
