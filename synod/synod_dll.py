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


class synod:
    def __init__(self, iterable):
        if isinstance(iterable, dict):
            self.__dict = iterable
        elif isinstance(iterable, list):
            self.__dict = dict(map(lambda x: [HList(x[0]) if type(x[0]) == list else x[0], x[1]], iterable))
        else:
            raise ValueError(
                f'''iterable may be dict or list istance, not {str(type(index)).split(" ", 1)[1].split("'")[1]}''')
    
    class _Item:
        def __init__(self, key, value):
            self.key = key
            self.value = value
        
        def __getitem__(self, index):
            match bool(index):
                case False:
                    return self.key
                case True:
                    return self.value
                case _:
                    raise ValueError(f'''index may be {
        f"""int istance, not { str(type(index)).split(" ", 1)[1].split("'")[1]}"""
        if not isinstance(index, int) else
        'int gt 0 and lt 2'}''')
    
    def __contains__(self, key):
        if self.get(key) == EmptyValue:
            return False
        return True
    
    def get(self, key, default=EmptyValue):
        try:
            return self._get_item(key)[1]
        except ValueError:
            return default
    
    def _get_item(self, key):
        for k, v in self.__dict.items():
            if (isinstance(k, list) and key in k) or k == key:
                return self._Item(k, v)
        raise ValueError(f'key {repr(key)} not found')
    
    def has_key(self, key):
        return key in self
        
    def is_synonym(self, key):
        if self.has_key(key):
            if isinstance(self._get_item(key).key, list):
                return True
            return False
        raise ValueError(f'key {repr(key)} not found')
        
    
    def get_main_key(self, key):
        if self.has_key(key):
            if self.is_synonym(key):
                return self._get_item(key).key[0]
            return key
        raise ValueError(f'key {repr(key)} not found')
    
    def clear(self):
        self.__dict = {}
    
    def __delitem__(self, key):
        try:
            del self.__dict[key]
        except:
            del self.__dict[self._get_item(key).key]
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __repr__(self):
        return str(self.__dict)

