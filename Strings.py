# What is strings- is a sequence of characters - meaning>> letters, numbers and other characters like dollar sign ,
# spaces and punctuation enclosed by single quotes, double quotes or even triple quotes while spanning multiple lines.

# So let's define a string and assign it a variable.
# I am going to create a variable named my_string and assign it the following value:"This is my first  string", first using double quotes.

# my_string = "This is my first string"
# print(my_string)
#
# my_string = 'This is my first string'
# print(my_string)

# Now, what do we need triple quotes for? = we need them whenever we want to enter a string for multiple lines; for instance a comment in our code

# lets see how to do this>> lets assign the same text to my_string variable

# my_string = '''This
# is
# my
# first
# string '''
# print(my_string)

# Now lets learn indexing
# Python uses indexes to mark the position  of an element within a sequence of elements - a string is a sequence of elements and the elements of a string are the characters themselves. One character , one element.

# the first element of any sequence, when counting from left to right, has the index 0. Then the second of the sequence has index 1, the third element is positioned at index 2,and so on. So when using indexes, remember to always start counting from 0.

# when counting backwards, from right to left, the first index will be index -1. So the last character in a string will have indes -1, when looking right to left.

# lets create a variable string1 and assign in the value "Cisco Router"
string1 = "Cisco Router"
# now lets extract the first character of strings? By
# Using an index. And as stated before, that would be the index 0
# So to access the element of string1 positioned at the index0 in the string, we would type the following
# the name of the variable, string1 and then without inserting any space, the index number in between brackets.
# so:
# variable_name[index_number]
print(string1[0])
# This returns the letter C which is correct because it is the first character in the string
# Now let's find the third character of string1. What index should we use? index2
print(string1[2])  # returns "s"

# now,  for negative indexes.
# lets access the last character in the string.
# we will use index -1
print(string1[-1])  # returns "r"
# What about string1[-4]
print(string1[-4])  # returns "u"

# what if we have an invalid index for the string?
# lets see, what do i mean by that? let's find out string1's length. We can count how many characters are in that visually, but what if we have a very very, veeeery long string, maybe a newspaper pae? Python has a solution for this and it's called len() function. This function is easy to use just type len and without any spaces after it, add the variable name pointing to our string in between the parentheses, so len(string1) returns the number of characters, which is 12
print(len(string1))  # returns 12

# Now back to the first question. What happens when we enter an invalid index? Well, let's try it! String1 has 12 characters.So, starting at index0 and counting from left to right, the last character should have the index 11
# So:
print(string1[11])  # returns r

# This is the same as
print(string1[-1])

# now, lets see what happens if we enter index 20
# print(string1[20])  # returns an indexError - string index out of range

# Now, it's time to have a look at some string operations and methods that will help us work with this data type.
# Python Strings - Methods

# 1. First , one more thing about indexes - you can find out the index of a character given string by using the index () function. Just remember that this method returns on lju the first occurence of that particular character in the string. So lets create a variable "a" and assign it the string  'Cisco Switch'
a = "Cisco Switch"

# You can clearly see that the letter 'i' appears two times in this string . So let's find out the index of the first occurence 'i' in the string

# Syntax
# We have the name of the variable associated with the string, the  a dot , the name of the method, index, then , i n between parentheses , we enter the character we want to find out the index for "i" . Don't forget to enclose "i" in single or double quotes, since this letter is also a string.

print(a.index("i"))

# 2, Another useful python method is one that helps you find how many times a character appears in a string or, generally speaking, inside a particular sequence. This method is called count().

# The syntax of count is similar to that of the index () method you've seen  earlier. To use the count method , just type in the  name of the variable , then a dot, then the word count, then open  and close parentheses and finally the letter you want to count surrounded by quotes.
print(a.count("c"))  # returns 2
print(a.count("C"))  # returns 1
print(a.count("i"))  # returns 2

#  3. Another string method is find(). This method simply searches for a sequence of characters inside a string, if it finds a match then it returns the index where that sequence begins.

print(a.find("sco"))  # returns 2

# on the other hand if python does not find a match then it will return the value -1.

print(a.find("xyz"))  # returns -1
print("The string you are searching for cannot be found!")
# else:
print("The string you are searching for cannot be found!" + str(a.find("sco")))

# 4. We can also use some predefined Python methods to turn a string from upper cases to lower case or vice versa, if we want that.
# This can be accomplished by using the lower() and upper() methods

a = "Cisco Switch"
print(a.lower())  # lower case
print(a.upper())  # upper case

# Keep one thing in  mind here! Although we have just applied athe lower() and the upper() methods, the initial string is still the same. No changes have been applied.

print(a)
# This is a great prove that strings are immutable

# 5. You can also verify that a string that starts or ends with a particular character or substring. We have two methods available for this. They are called starts with() and ends with ()
print(a.startswith("C"))
print(a.endswith("h"))
print(a.endswith("q"))

# 6. Three important methods which you should always keep in mind , because you will always use them a lot when working with strings, are strip(), split(), and join()

# 6.1 First the sgtrip() method eliminates all whitespaces from the start and the end of the dxtring.
# lets say we have a string, one with 3 white spaces before "Cisco" and 4 white spaces after "Switch"
b = "  Cisco Switch   "
print(b)
print(b.strip())

# now consider that instead of three sp;aces on each side of the string, we had the $ that we want to remove
c = "$$$Cisco switch$$$$"

# We want to eliminate the leading trailing dollar signs. Fot=r this wed should specify the character we want to remove in between  strips()s parenthesis

print(c)
print(c.strip("$"))

# Byt , what if we want all spaces removed from the string including those inside the string ? Then we would use the replace() method instead of strip()
print(b.replace(" ", ""))

# 6.2 Let's have a look at the split() methis, As its name implies, this method simply split a string into substrings. Furthermore, you can  specify a delimiter for splitting the string. The result of this method is a list.

# You have a string reference by variable d
d = "Cisco,Jupiter,Hp, Avaya,Nortel"

# The network device manufacturers in this string are delimited by commas.

# so, the comma is regarded as our delimiter for the splitter

# what if we want to extract each provider from the string in a nice format? well. in this case the split method saves the day

print(d.split(","))

# Python returns a list where each provider in  the string is an element of this list that can be further used into an application.

# 6.3 Finally we have the joi() method for dealing with strings. Let's remember striking "a" which is "Cisco Switch". What if we want to insert in between every two characters of this string? we want to change this string to "C_i_s_c_o__S_w_i_t_c_h"


print("_".join(a))

# please find a comprehensive list of string methods in the link below
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

# python 3 strings - Operators $ formatting
# what else can we do with strings?
# for instance we can concatenate them.concatenation means unifying two or more strings into a single string

# You can do this using the " +" operator , like you would when adding two numbers:

# lets set x with the value of " Cisco"

x = "Cisco"

# y is the value of "Switch"
y = "Switch"

# and finally , add them together

z = x + y

print(z)
# another thing we can do is string repetition ,by using the multiplication operator, " *" s,

print(x * 5)
# You can also verify if a character is in a string or not using the "in" and "not in " operator

print("o" in x)  # return true
print("b" not in x)  # return true

# let's say we have some kind of string templates and we want to contanly modify only a few words inside the text but keep the overall templates the same
# let's assume we have the following strings. Doesn't matter what it stands for , just focus on the string itself
"Cisco model: 2600XM 2 WAN slots , IOS 12.4"

# We want to keep the string as a template and just change the model name , number of slots and ios version a couple of times, while running our Python program. So , this would need a dynamic change time

# for this we should use the percentage "% " operator, followed by "s" for string, 'd' for digit and f for float point number
"Cisco model: %s, %d  WAN slots , IOS %f" % ("2600XM", 2, 12.4)

# now lets translate
# THE %S THAT THIS IS a placeholder for a string we will specify in between parenthesis at the end of this line. The %d operator follows the same logic , but for a number , instead of a string , and, finally the %f refers to a floating point number, a number with a decimal point.
# Now moving on, the first value from within the parentheses, is going to be associated with the first format operator in the string, the second value from within the parentheses is going to be associated with the second format operator in the string , and so on, for all the format operator you have in  your string.

# Also do NOT forget to insert the % sign between the string and the parentheses containing the values. This operator maps the format operators inside the string with the values inside the parentheses.

# lets see this in action
print("Cisco model: %s, %d  WAN slots , IOS %f" % ("2691XM", 4, 12.4))
print("Cisco model: %s, %d WAN slots, IOS %f" % ("7200XR", 8, 15.4))
print("Cisco model: %s, %d WAN slots, IOS %f" % ("1841M", 1, 12.2))

# If we want a single digit after the floating point, we should use .1, like this
print("Cisco model: %s, %d  WAN slots , IOS %.2f" % ("2691XM", 4, 12.4))

# finally , if we want mno digits at all and no floating point, we just enter a dot and we will bet the value 12 returned.
print("Cisco model: %s, %d  WAN slots , IOS %.f" % ("2691XM", 4, 12.4))

# howeverm this is not the only way of dealing with string formatting.

# Instead of formatting operators like the ones you've just seen, we can use other notation, replacing %s, %d or %F worth a pair of curly braces . Also after the string , the % operator we used for mapping the values is going to be replaced by a method called format()

print("Cisco model: {}, {}  WAN slots , IOS {}".format("2691XM", 4, 12.4))

print("Cisco model: {0}, {1}  WAN slots , IOS {2}".format("2691XM", 4, 12.4))

first_name = "Daisy"
last_name = "Chebet"

# + operator

full_name = first_name + " " + last_name
print(full_name)

# format function
print("{} {}".format(first_name, last_name))
print("{}".format(full_name))

# f-string formatter
print(f"Hello everyone, my name is {first_name} {last_name}.")

# Python 3 String- slices
# Slices allow us to extract various parts of a string (or list, other sequence of elements), leaving the initial string unchanged

# The syntax for a string slice is the following:

# We have the name of the variable pointing to the string we want to slice, followed by a pair of square brackets, in between the brackets we have a full colon then on the left side of the colon we specify the index at which to start the splicing process, the SLICES WILL GO UPTO , but not include the index specified on the right side of the colon. the first character in our slice should be 1 and last 9  which is located at index 14 right ok so will have to go upto index 15 as the slice , however as previously stated the character at index 15 will not be included in the slice

# Examples
# extract the first ip address in the string, 10.110.8.9
string1 = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"
print(len(string1[5: 15]))
print(len(string1[5: 16]))

# Now what if we don't specify the second index inside the brackets ? well the string slice would start at the imdex given before the colon and would end at the end of the string. So this way, we will get the rest of the string, starting from the character at index 5
print(string1[5:])

# This will print upto the 11th character from the beginning.

print(string1[:10])
# Another question might be what if we don't enter any indexes at all? it will print all string
print(string1[:])
# lets see how we can use negative indexes then we will use [-] theat index
print(string1[-1])

# to print the Ethernet then will have "E " at index -9  and "R" at index -2
print(string1[-9:-1])

# #=So our slices at index -9 and goes upto but does not include index -1. This means that the last character we are extracting is positioned at index -2 2hich is right before -1. The final result is correct , since we got the "Ethernet" substring printed out.
print(string1[-18:-11])

# what if we want
# to obtain the last 5 character
print(string1[-5:])

# What  if we want to slice string1 starting at the beginning of the string and leave out the last 5 characters?
print(string1[:-5])

# we can specify element within the square brackets after the indexes also separated by colon
# if you like to skip every second character of the string and obtain a new string with these elements removed you can write the following slices

print(string1[::2])

# using these slices we are referring to the entire string, starting from the end of the string at index -1 character by character . and this is how you can easily print a string in reversed order.
print(string1[::-1])