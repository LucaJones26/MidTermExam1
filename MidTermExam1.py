a = 6
a = a - 2
print(a*2)
a = a*2
print(a+1)
a = a//3

print((2+3)*6/2)

import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)


def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

def reverse_num(n):
    n_str = str(n)
    n_list = list(n_string)
    n_list.reverse()
    return int(reverse_str)

num = 5485839837501070045005400701057389385845
print(reverse_num)


"6593036601359343374664733439531066303956"
"7489617719749244646336564429479177169847"
"8025833559061079503003059701609553385208"


my_list = [1, 2, 3]
print("original_list:", my_list)

my_list[0] = 10 #modifying the list
print("modified_list", my_list)

my_list.append(4)
print("list after appending", my_list)
# Shows Lists are mutable

my_string = "hello"
print("n/0riginal string:", my_string)
try:
    my_string:[0] = "H"
except TypeError as E: #E as in error
    print("Error:", e)

new_string = my_string[1:] + "H"
print("new_string:", my_string)




import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
modified_numbers = []

for num in random_numbers:
    if num % 2 == 0:
        modified_numbers.append(num * 2)
    else:
        continue

print(modified_numbers)



def is_valid_url(url):
    if not (url.startswith("http://") or url.startwith("https://")):
        return False
    if "." not in url:
        return False
    if url.rfind(".") == len(url - 1):
        return False
    return True





