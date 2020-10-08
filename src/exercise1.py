# Exercise 1a
class PrimeIterator:
    """This is an iterator class that generates prime numbers from 1 to a number,n, where n is greater than 1"""

    def __init__(self, n):
        # Making sure that n is always greater than 1
        if n > 1:
            # save n in self.number
            self.number = n
            # Begin the index from -1,so that when the parser enters the __next__ method, 1 would be added to give 0
            self.index = -1
        else:  # if n<1,raise value error
            raise ValueError("Please enter a number greater than 1")

    def __iter__(self):
        return self  # Return self in the __iter__ method

    def __next__(self):
        self.index += 1
        # Create the list of prime numbers using list comprehension
        self.list = [a for a in range(2, self.number+1) if all(a % b != 0 for b in range(2, a))]
        # If index becomes greater than the length of the list of prime numbers, raise StopIteration
        if self.index >= len(self.list):
            raise StopIteration("You have reached the last prime number.")
        # Else, return the item at that index
        else:
            return self.list[self.index]


# Exercise 1b
def prime_generator(n):
    """This is a generator function that also generates prime numbers from 1 to number, n."""

    if n > 1:  # Making sure that n is always greater than 1
        # Create the prime numbers list with list comprehension
        prime_num_list = [a for a in range(2, n + 1) if all(a % b != 0 for b in range(2, a))]
        # Yield the prime number at the index,i, in the range of the length of the list
        for i in range(len(prime_num_list)):
            yield prime_num_list[i]
    else:
        raise ValueError("Please enter a number greater than 1")
