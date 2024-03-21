#!/usr/bin/env python3

test_string = "Now is the time for all good persons to come to the aid of their country. ASDFjkl; 1234567890 !@#$%^&*()"
a_list = []
for letter in test_string:
    a_list.append(f"Found {test_string.count(letter)}, {letter.encode('utf-8')} in the string: {test_string}")


# set_list = set(a_list)
# sorted_list = sorted((set(set_list)))
#
# for element in s_list:
#     print(element)

set_list = set(a_list)
sorted_list = sorted(set_list)
print(*sorted_list, sep="\n")
