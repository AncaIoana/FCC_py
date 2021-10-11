#file location: www.pythonlearn.com/code3/mbox-short.txt

file = input('Enter file name:')
handle = open(file)

for line in handle:
    line = line.rstrip()
    print(line.upper())


