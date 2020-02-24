#!/usr/bin/env python3
# frank.villaro@infomaniak.com - DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE, etc.

import dataset
import uuid

db = dataset.connect('sqlite:////db/db.sqlite')

t = db['cluster']

t.insert({'xuid': uuid.uuid4().hex, 'name': ''})
t.insert({'xuid': uuid.uuid4().hex, 'name': ''})

# vim: set ts=4 sw=4 et:

