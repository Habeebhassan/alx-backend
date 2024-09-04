#!/usr/bin/env python3
"""BasicCache module
Provides a simple caching mechanism
using key-value pairs.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A basic caching system that stores 
    key-value pairs in memory.

    Methods:
        put(key, item):
            Adds a key-value pair to the cache.
        get(key):
            Retrieves the value associated with a 
            given key from the cache.
    """

    def __init__(self):
        """
        Initialize the cache by calling the
        initializer of the parent class.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add a key-value pair to the cache.
        If either `key` or `item` is None
        the method does nothing.

        Args:
            key: The key under which to store the item.
            item: The item to store in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value associated with 
        a key from the cache.

        Args:
            key: The key whose value should 
            be retrieved.

        Returns:
            The value associated with the
            given key, or None if the key is not
            present in the cache or if the key is None.
        """
        return self.cache_data.get(key)
