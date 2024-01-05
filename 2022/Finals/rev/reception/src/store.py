"""
Key Value Store in Pure Python!
"""


class Store:
    """
    In memory key value store, using the ultra fast dictionary object in Python
    C.R.U.D.
    """

    def __init__(self) -> None:
        self.store = {}

    def create(self, key, value) -> bool:
        """
        C: Inserts value into key
        """
        if key in self.store:
            return False
        self.store[key] = value
        return True

    def read(self, key):
        """
        R: Fetches value from key
        """
        if key in self.store:
            return self.store[key]
        return None

    def update(self, key, value) -> bool:
        """
        U: Updates value for key
        """
        # if not self.store[key]:
        #     return False
        self.store[key] = value
        return True

    def delete(self, key) -> bool:
        """
        D: Deletes key (and value) *poof*
        """
        value = self.store.pop(key, None)
        if value is None:
            return False
        return True

    def size(self) -> int:
        """
        Returns the size of the key-value store
        """
        return len(self.store)
