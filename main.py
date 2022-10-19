# a == b : equal to (must be double equals)
# a != b : not equal to
# a > b : greater than
# a < b : less than
# a <= b  : less than or equal to
# a >= b : greater than or equal to

# Boolean Values are true or false

# num_1 = 5 
# num_2 = 6
# greater = num_1 > num_2
# print (greater)

num_1 = 11
num_2 = int(input("Enter a number: "))

if num_2 > num_1:
  print (f"Greater than {num_1}")
elif num_2 == num_1:
  print (f"Equal to {num_1}")
else:
  print(f"Less than {num_1}")