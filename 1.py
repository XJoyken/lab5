import re
from re import search

#1 problem
string = "abbbbbb"
pattern = r"ab*"
match = re.search(pattern, string)
if match:
    print("This string has an 'a' followed by zero or more 'b''s.")
else:
    print("This string has no an 'a' followed by zero or more 'b''s.")

#2 problem
string = "abbbb"
pattern = r"ab{2,3}"
match = re.search(pattern, string)
if match:
    print("This string has an 'a' followed by two to three 'b'")
else:
    print("This string has no an 'a' followed by two to three 'b'")

#3 problem
string = "hello_world this_is_a_test not_MatChing test_example here there"
pattern = r"\b[a-z]+_[a-z]+\b"
find = re.findall(pattern, string)
print(find)

#4 problem
string = "Helloworld ThIs andthis ORthis"
pattern = r"[A-Z][a-z]+"
find = re.findall(pattern, string)
print(find)

#5 problem
string = "annsb"
string2 = "afefe"
pattern = r"a.*b$"
match = re.search(pattern, string)
if(match):
    print("This string has an 'a' followed by anything, ending in 'b'")
else:
    print("This string has no an 'a' followed by anything, ending in 'b'")

#6 problem
string = "hello world,this.is the test"
rep = re.sub("[ ,.]", ":", string)
print(rep)

#7 problem
string = "hello_world_this_is_the_test"
pattern = r"_([a-z])"
split = re.split(pattern, string)
new = []
for i in range(1, len(split) - 1, 2):
    new.append(split[i].upper() + split[i + 1])
new.insert(0, split[0])
new_string = ("").join(new)
print(new_string)

#8 problem
string = "helloWorldJgJgjGjJG"
pattern = r"([A-Z])"
split = re.split(pattern, string)
new = []
for i in range(1, len(split) - 1, 2):
    new.append(split[i] + split[i + 1])
if split[0]:
    new.insert(0, split[0])
print(new)

#9 problem
string = "HelloWorldThisIsTheTest"
pattern = r"([A-Z])"
split = re.split(pattern, string)
new = []
for i in range(1, len(split) - 1, 2):
    new.append(split[i] + split[i + 1])
if split[0]:
    new.insert(0, split[0])
new_string = (" ").join(new)
print(new_string)

#10 problem
string = "helloWorldThisIsTheTest"
pattern = r"([A-Z])"
split = re.split(pattern, string)
new = []
for i in range(1, len(split) - 1, 2):
    new.append(split[i] + split[i + 1])
new.insert(0, split[0])
new_string = ("_").join(new)
print(new_string)