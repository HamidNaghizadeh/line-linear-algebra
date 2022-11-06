from vector import Vector
from Line import Line

# Vector Examples
vector1 = Vector([1, 3])
vector2 = Vector([2, 6])

print('\nvector1 is : [1  3]')
print('vector2 is : [2  6]')

print('vector1 + vector2 = ', vector1 + vector2)
print('vector1 - vector2 = ', vector1 - vector2)

print('\nis vector1 parallel with vector2 ?\n ', vector2.is_parallel(vector1))
print('\nvector1 scalar multiplication in 2 :\n ', vector1.scalar_multiplication(2))

print()

# Line Examples
line7 = Line(Vector([2, 5]), 2)  # 2x + 5y = 2
line8 = Line(Vector([1, 3]), 6)  # x + 3y = 6
line9 = Line(Vector([4, 10]), 4)  # 4x + 10y = 4

print('\nis line7 and line8 parallel ?\n', line7.is_parallel(line8))
print('\nis line7 and line9 parallel ?\n', line7.is_parallel(line9))
print('\nis line7 and line9 equal ?\n', line7.is_equal(line9))
print()

