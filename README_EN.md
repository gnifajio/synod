# **synod** by
_Gnifajio_ ![](https://badgen.net/badge/release/v1.1/grey) ![](https://komarev.com/ghpvc/?username=gnifajio-synod&label=views)

_Python dictionary with synonyms_

## Description

Python does not support the list type as a dictionary key, and there are more synonyms.
I solved this problem by creating my own synod data type that allows me to do this.
Below is an example of how it works.

## Installation

```sh
git clone https://github.com/gnifajio/synod.git
cd synod
python3 setup.py install
```

Or

```sh
pip install synod
```

## Usage

```python
from synod import Synod

synoded = Synod([
    [['development', 'dev'], [
        'all_inclusive', 'backend', 'frontend',
        'prototyping', 'android', 'desktop',
        '1c_dev', 'games', 'other', 'scripts',
        'voice_interfaces', 'ios', 'bots',
    ]],
    [['testing', 'tst'], [
        'sites', 'mobile', 'software',
    ]],
    [['admin', 'adm'], [
        'servers', 'network', 'databases',
        'security', 'other',
    ]]
]
)

synoded['dev'] == synoded['development']  # True
'dev' in synoded  # True
synoded.get('wtf')  # synod.EmptyValue
synoded.get('testing')  # [ 'sites', 'mobile', 'software' ]
synoded.has_key('tst')  # True
synoded.is_synonym('adm')  # True
synoded.get_main_key('adm')  # 'admin'
del synoded['dev']
synoded.has_key(dev)  # False
synoded.clear()
synoded  # {}
```

## TODO

**Add Methods:**

- `__ior__`
- `__iter__`
- `__len__`
- `__or__`
- `__reversed__`
- `__ror__`
- `__setitem__`
- `copy`
- `fromkeys`
- `keys`
- `pop`
- `popitem`
- `setdefault`
- `update`
- `values`

# New in version 1.1:

- `items` method.