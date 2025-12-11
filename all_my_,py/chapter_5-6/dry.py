

value = [1,3]
# this fuktion returns the smalest value 
print(min(value))

# this fuktion returns the largest value 
print(max(value))

# this fuktion prints the value
print(value)

# this fukion lets us inpt somthing into are programm
input("input somthing ")

# this is the new fuktion it is filter() it filters a sequens based on a difrend fuktions
numbers = [1, 2, 3, 4, 5, 6]

def is_even(n):
    return n % 2 == 0

result = filter(is_even, numbers)
print(list(result))
