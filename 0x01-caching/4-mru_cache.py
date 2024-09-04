#!/usr/bin/env python3
"""MRUCache module
Provides a caching mechanism using a Most Recently Used (MRU) strategy.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache defines a caching system using the Most Recently Used (MRU) policy.

    Methods:
        put(key, item):
            Adds a key-value pair to the cache, evicting the most recently used entry if necessary.
        get(key):
            Retrieves the value associated with a given key from the cache and marks it as recently used.
    """
    
    def __init__(self):
        """
        Initialize the MRU cache by calling the initializer of the parent class
        and setting up a list to track the usage order of keys.
        """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Add a key-value pair to the cache.

        If the cache exceeds its maximum capacity (BaseCaching.MAX_ITEMS), 
        it removes the most recently used entry (the last entry in the usage list) 
        to make space for the new entry.

        Args:
            key: The key under which to store the item.
            item: The item to store in the cache.
        """
        if key is not None and item is not None:
            # Remove the most recently used entry if the cache size limit is reached
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                mru_key = self.usage[-1]
                print("DISCARD: {}".format(mru_key))  # Inform which key is being discarded
                del self.cache_data[mru_key]
                del self.usage[-1]

            # Remove the key from the usage list if it already exists
            if key in self.usage:
                self.usage.remove(key)

            # Add or update the cache with the new key-value pair
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value associated with a key from the cache.

        If the key exists in the cache, it is marked as recently used 
        (i.e., moved to the end of the usage list).

        Args:
            key: The key whose value should be retrieved.

        Returns:
            The value associated with the given key, or None if the key is not
            present in the cache or if the key is None.
        """
        if key is not None and key in self.cache_data:
            # Move the accessed key to the end of the usage list
            self.usage.remove(key)
            self.usage.append(key)
            return self.cache_data[key]
        return None

