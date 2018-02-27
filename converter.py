import json

inp = 'devpost-08-12-2017.json'
oup = '_' + inp

with open(inp, 'rb') as fi:
    with open(oup, 'wb') as fo:
        pages = json.loads(fi.read().decode('UTF-8'))
        for page in pages:
            urls = page['urls']
            for url in urls:
                fo.write((url + '\n').encode('UTF-8'))