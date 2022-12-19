from typing import Any


class EmptyValue:
    pass


class HList(list):
    def __hash__(self):
        return hash(f'HList<{str(self)}')

    def __gt__(self, other):
        return str(str(self)) > str(other)

    def __lt__(self, other):
        return str(str(self)) < str(other)

    def __ge__(self, other):
        return str(str(self)) >= str(other)

    def __le__(self, other):
        return str(str(self)) <= str(other)


class Synod:
    def __init__(self, iterable: dict | list):
        if isinstance(iterable, dict):
            self.__dict = iterable
        elif isinstance(iterable, list):
            self.__dict = {
                HList(k) if type(k) == list else k: v
                for k, v in iterable
            }
        else:
            raise ValueError(f'''iterable may be dict or list instance, not {type(iterable).__name__}''')

    class _Item:
        def __init__(self, key: Any, value: Any):
            self.key = key
            self.value = value

        def __getitem__(self, index: int):
            if index == 0:
                return self.key
            elif index == 1:
                return self.value
            else:
                raise ValueError(f'index may be int' + ((', not ' + type(index.__name__))
                                                        if not isinstance(index, int) else " gt 0 and lt 2"))

    def __contains__(self, key):
        if self.get(key) == EmptyValue:
            return False
        return True

    def get(self, key, default=EmptyValue):
        try:
            return self._get_item(key)[1]
        except ValueError:
            return default

    def _get_item(self, key: Any) -> _Item:
        for k, v in self.__dict.items():
            if (isinstance(k, list) and key in k) or k == key:
                return self._Item(k, v)
        raise ValueError(f'key {repr(key)} not found')

    def has_key(self, key: Any) -> bool:
        return key in self

    def is_synonym(self, key):
        if key in self:
            if isinstance(self._get_item(key).key, list):
                return True
            return False
        raise ValueError(f'key {repr(key)} not found')

    def get_main_key(self, key):
        if key in self:
            if self.is_synonym(key):
                return self._get_item(key).key[0]
            return key
        raise ValueError(f'key {repr(key)} not found')

    def clear(self):
        self.__dict = {}

    def items(self):
        return self.__dict.items()

    def __delitem__(self, key):
        try:
            del self.__dict[key]
        except KeyError:
            del self.__dict[self._get_item(key).key]

    def __getitem__(self, key):
        return self.get(key)

    def __repr__(self):
        return str(self.__dict)
