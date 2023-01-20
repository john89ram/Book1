# You can also rename the function with an alias to make things quicker
    # However this can be hard to read for other programmers to read this without context
from pizza import make_pizza as mp

# Then you can just call the function by the alias
mp(16, 'pepperoni')
mp(12, 'mushroom', 'green peppers', 'extra cheese')