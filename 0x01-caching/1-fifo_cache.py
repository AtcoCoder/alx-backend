#!/usr/bin/env python3
""" 1-fifo_cache module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class
    subclass of BaseCaching class
    """
    def __init__(self):
        """initialize method"""
        super().__init__()

    def put(self, key, item):
        """assigns to the dictionary self.cache_data the item
        value for the key 'key'
        """
        if key and item:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))
            self.cache_data[key] = item

    def get(self, key):
        """returns the value in self.cache_data linked to key."""
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
