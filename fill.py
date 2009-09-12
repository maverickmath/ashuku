#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright muflax <mail@muflax.com>, 2009
# License: GNU GPL 3 <http://www.gnu.org/copyleft/gpl.html>

import yaml, random
from datetime import datetime
from datetime import timedelta

def main():
    data = {}
    entries = [{"sleep": "25m"},
               {"weight": "78"},
               {"日本語": "1h20m"},
               {"happiness": "+2"}]
    for i in range(1000):
        dt = timedelta(days=random.randint(0, 365), seconds=random.randint(0,60*60*24))
        d = datetime.now() - dt
        data[d.strftime("%Y-%m-%d %H:%M:%S")] = [random.choice(entries).copy()]

    print(yaml.dump(data, default_flow_style=False, allow_unicode=True).replace("'", ""))

if __name__ == "__main__":
    main()

