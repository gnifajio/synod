# **synod** by _Gnifajio_ ![](https://badgen.net/badge/release/v1.0/grey) ![](https://komarev.com/ghpvc/?username=gnifajio-synod&label=views)

_Python словарь с синонимами_

## Описание

Python не поддерживает тип list как ключ словаря, а там более синонимы.
Я решил эту проблему, создав собственный тип данных synod, позволяющий делать это.
Ниже будет пример как это работает.

## Установка

```sh
git clone https://github.com/gnifajio/synod.git
cd synod
python3 setup.py install
```

## Использование

```python
from synod import synod
synoded = synod([
        [['development', 'dev'], [
            'all_inclusive',    'backend', 'frontend',
            'prototyping',      'android', 'desktop',     
            '1c_dev', 'games',  'other',   'scripts',
            'voice_interfaces', 'ios',     'bots',
        ]],
        [['testing', 'tst'], [
            'sites', 'mobile', 'software',
        ]],
        [['admin', 'adm'], [
            'servers', 'network', 'databases',
            'security', 'other' ,
        ]]
        ]
    )

synoded['dev'] == synoded['development'] # True
'dev' in synoded # True
synoded.get('wtf') # synod.EmptyValue
synoded.get('testing') # [ 'sites', 'mobile', 'software' ]
synoded.has_key('tst') # True
synoded.is_synonym('adm') # True
synoded.get_main_key('adm') # 'admin'
del synoded['dev']
synoded.has_key(dev) # False
synoded.clear()
synoded # {}
```

## TODO

**Добавить методы:**
- `__ior__`
- `__iter__`
- `__len__`
- `__or__`
- `__reversed__`
- `__ror__`
- `__setitem__`
- `copy`
- `fromkeys`
- `items`
- `keys`
- `pop`
- `popitem`
- `setdefault`
- `update`
- `values`