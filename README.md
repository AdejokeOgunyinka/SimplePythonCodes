## ASSESSMENTS

Below are exercises that you are expected to complete and provide solutions to in the python scripts in the src folder. Happy hacking, cheers

## EXERCISE 1

(a) Using the iteration protocol, create an iterator class named `PrimeIterator` that generates prime numbers from `1` to a number `n`, where `n` is greater than 1, which stops the iteration with the appropriate exception when it gets to a number greater than `n` 

(b) Redefine the `PrimeIterator` class above using the concept of generators by defining a generator function named `prime_generator` that accomplishes the same functionality

## EXERCISE 2

Define a decorator named `get_month_decorator`, that decorates a function named `get_month` which takes an integer between `1 & 12 (inclusive)` representing the month of the year and returns the month as a string.

**Example:** Given an input integer 9, the output string will be `"September"`

The purpose of the decorator function(`get_month_decorator`) is to validate that the integer to be passed to the decorated function(`get_month`) is indeed an integer between `1 & 12 (inclusive)`, otherwise raise an `ArgumentError` exception with a nice error message. While the purpose of the decorated function (`get_month`) is simply to return the expected month string based on the valid month integer passed in as argument

## EXERCISE 3

Using the context manager protocol, create a context manager class named `ListManager`, that manages a context to be used with the `with` statement for lists. 

The context manager will yield an `iterator object` of the list passed to its constructor as an argument into the `with` block and handles any exception raised in the `with` block as a result of calling `next()` function on the yielded `iterator object` when there are no more items in the list, by printing the error message from the exception
