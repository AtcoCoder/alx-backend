#!/usr/bin/env python3
"""0-basic module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class
    - subclass of BasicCaching class
    """
    def __init__(self):
        super().__init__()
    
    def put(self, key, item):
        """assign to the dictionary self.cache_date"""
        if key and item:
            self.cache_data[key] = item
    
    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
    