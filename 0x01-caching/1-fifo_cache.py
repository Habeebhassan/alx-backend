#!/usr/bin/env python3
"""FIFOCache module
Provides a caching mechanism using a First-In, First-Out (FIFO) strategy.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache defines a caching system using the First-In, First-Out (FIFO) policy.

    Methods:
        put(key, item):
            Adds a key-value pair to the cache following the FIFO strategy.
        get(key):
            Retrieves the value associated with a given key from the cache.
    """

    def __init__(self):
        """
        Initialize the FIFO cache by calling the initializer of the parent class
        and setting up an order list to track the insertion order of keys.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add a key-value pair to the cache.

        If the cache exceeds its maximum capacity (BaseCaching.MAX_ITEMS), 
        it removes the oldest entry (the first inserted key-value pair) following
        the FIFO policy.

        Args:
            key: The key under which to store the item.
            item: The item to store in the cache.
        """
        if key is not None and item is not None:
            # Remove the oldest entry if the cache size limit is reached
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))  # Inform which key is being discarded
                del self.cache_data[self.order[0]]
                del self.order[0]
            
            # Add or update the cache with the new key-value pair
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Retrieve the value associated with a key from the cache.

        Args:
            key: The key whose value should be retrieved.

        Returns:
            The value associated with the given key, or None if the key is not
            present in the cache or if the key is None.
        """
        return self.cache_data.get(key)
