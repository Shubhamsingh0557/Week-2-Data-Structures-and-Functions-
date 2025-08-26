# Week-2-Data-Structures-and-Functions-

# 1. List:
  * A list is an ordered collection of items.
  * It is mutable, meaning elements can be changed.
  * It Defined using square brackets [ ].
  * They Supports indexing, slicing, appending, removing, etc.
  * Example: fruits = ['apple', 'banana', 'mango']

# 2. Tuple
  * A tuple is an ordered collection like a list, but immutable.
  * It Defined using parentheses ( ).
  * It Used when data should not change.
  * They are Faster than lists due to immutability.
  * Example: coordinates = (10, 20)

# 3. Dictionary
  * A dictionary stores data in key-value pairs.
  * It is unordered and mutable.
  * It Defined using curly braces { }.
  * The Keys must be unique and immutable.
  * Example: student = {'name': 'Amit', 'age': 21}

# 4. Set
  * A set is an unordered collection of unique elements.
  * It Defined using curly braces { } or the set() function.
  * It Automatically removes duplicates.
  * It Supports set operations like union, intersection, difference.
  * Example: numbers = {1, 2, 3, 2} → result: {1, 2, 3}

# Functions & Functional Concepts
# 5. Function
  * A function is a reusable block of code that performs a task.
  * It Defined using the def keyword.
  * It Can take parameters and return values.
  * It Helps in modular and clean code.
  * Example:
    
        def greet(name):
        return "Hello " + name

# 6. Lambda Function
  * A lambda function is a small anonymous function.
  * It Defined using the lambda keyword.
  * It is Used for short, one-line operations.
  * Syntax:
  
        lambda arguments: expression
  
  * Example: square = lambda x: x * x

# 7. Recursion
  * Recursion is when a function calls itself.
  * It is Useful for problems like factorial, Fibonacci, tree traversal.
  * It Must include a base case to avoid infinite loops.
  * Example:

        def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n - 1)

# 8. List Comprehension
  * A concise way to create lists using a single line.
  * Syntax:

        [expression for item in iterable if condition]

  * It Improves readability and performance.
  * Example:

        even = [x for x in range(10) if x % 2 == 0]
