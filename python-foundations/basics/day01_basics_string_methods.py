my_string = "hello world           "

#upper case
print(my_string.upper())
# strip string of outside whitespace
print(my_string.strip())
# replacing a part of a string
print(my_string.replace("hello", "HIIII"))

#split string into an array at the whitespace if no split is given
print(my_string.split())

#join
my_list = my_string.split() #["hello", "world"]
print(" ".join(my_list))


