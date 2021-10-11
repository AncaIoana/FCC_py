str = 'X-DSPAM-Confidence: 0.8475 '

#find the position of the :
cpos = str.find(':')

#print the part of the string after the : to the end
print(str[cpos+1 : ])

#print the part of the string after : to the end, removing the spaces on left and right
print(str[cpos+1 : ].strip())

#another way to do it:

#find out the size of the string str
size = len(str)

#print the part of the string with spaces, and then without spacces
print(str[cpos + 1 : len(str) + 1])
print(str[cpos + 1 : len(str) + 1].strip())


#convert the extracted bit into a floating point number

number1 = float(str[cpos+1 : ])
number2 = float((str[cpos + 1 : len(str) + 1]))

print(number1)
print(number2)

