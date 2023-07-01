import string
list_numbers = [x for x in range(1,22)]
list_abc = list(string.ascii_lowercase)
good = dict(zip(list_numbers,list_abc))
print(good)