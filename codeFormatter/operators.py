# Simple operands with different operators
# unary operators
aa = x+y
ab = x - y
ac = x*y + 1
# non-unary operators
a=x**y
b = config.base**5.2
c = config.base ** runtime.config.exponent
d =  2**5
e = 2 **~ 5

# Complex operands
f = 2**get_exponent()
g = get_x(        )    ** get_y()
h = config['base']    ** 2


# Long operands
# simple
# unary
i = this_is_a_really_long_variable_name_to_use * this_is_a_really_long_variable_name_to_use
# binary
i = this_is_a_really_long_variable_name_to_use ** this_is_a_really_long_variable_name_to_use

# complex
# unary
i = this_is_a_really_long_variable_name_to_use() * this_is_a_really_long_variable_name_to_use()
# binary
i = this_is_a_really_long_variable_name_to_use() ** this_is_a_really_long_variable_name_to_use()