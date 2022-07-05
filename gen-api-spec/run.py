#!/usr/bin/env python3

import json
import sys
from functools import cmp_to_key

f = open ('spec.json', "r")
spec = json.loads(f.read())
f.close()

def fmt_get_params(params):
    print(params)
    for p in params:
        if p['in'] == 'path':
            continue
        print('* ' + p['name'] + ': ' + p['schema']['type'])

version = spec['info']['version']
paths = sorted(list(spec['paths'].keys()))
for path in paths:
    print('## ' + path + '\n')
    pspec = spec["paths"][path]
    for method in list(pspec.keys()):
        print('### ' + method + '\n')
        print(pspec[method]['description'])
        if method == 'get':
            fmt_get_params(list(pspec[method]['parameters']))
    print('')
