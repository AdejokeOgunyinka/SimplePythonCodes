class ListManager:
    """This is a context manager class that works like an iterator. It accepts list arguments and
    returns the iterator object"""
    def __init__(self, items):
        # Save the list in variable self.list
        self.list = items

    def __enter__(self):
        # Yield every item in the list
        for item in self.list:
            yield item

    def __exit__(self, exc_type, exc_val, exc_tb):
        # If there's a StopIteration exception, print its value and class
        if exc_type == StopIteration:
            print(str(exc_val))
            print(str(exc_type))
        return True
