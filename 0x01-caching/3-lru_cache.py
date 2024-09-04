#!/usr/bin/env python3
""" 3-lru_cache module """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class
    subclass of BaseCaching class
    """
    def __init__(self):
        """initialize method"""
        super().__init__()
        self.recently_used = []

    def put(self, key, item):
        """assigns to the dictionary self.cache_data the item
        value for the key 'key'
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                else:
                    del self.cache_data[self.recently_used[0]]
                    print("DISCARD: {}".format(self.recently_used[0]))
                    self.recently_used.remove(self.recently_used[0])
            self.cache_data[key] = item
            if key in self.recently_used:
                self.recently_used.remove(key)
            self.recently_used.append(key)

    def get(self, key):
        """returns the value in self.cache_data linked to key."""
        if key and key in self.cache_data:
            if key in self.recently_used:
                self.recently_used.remove(key)
            self.recently_used.append(key)
            return self.cache_data[key]
        return None
