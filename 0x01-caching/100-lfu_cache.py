#!/usr/bin/env python3
""" 100-lfu_cache module """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class
    subclass of BaseCaching class
    """
    def __init__(self):
        """initialize method"""
        super().__init__()
        self.frequently_used = {}

    def put(self, key, item):
        """assigns to the dictionary self.cache_data the item
        value for the key 'key'
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                else:
                    del self.cache_data[self.least_frequestly_used()]
                    print("DISCARD: {}".format(self.least_frequestly_used()))
                    del self.frequently_used[self.least_frequestly_used()]
            self.cache_data[key] = item
            if key in self.frequently_used:
                self.frequently_used[key] += 1
            else:
                self.frequently_used[key] = 1

    def get(self, key):
        """returns the value in self.cache_data linked to key."""
        if key and key in self.cache_data:
            if key in self.frequently_used:
                self.frequently_used[key] += 1
            else:
                self.recently_used[key] = 1
            return self.cache_data[key]
        return None

    def least_frequestly_used(self):
        """returns the least frequently used key"""
        return min(self.frequently_used, key=self.frequently_used.get)
