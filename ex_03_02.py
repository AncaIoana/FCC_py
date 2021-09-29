sh = input('hours:')
sr = input('rate:')
try:
    fh = float(sh)
except:
    fh = -1
try:
    fr = float(sr)
except:
    fr = -1
print(fh,fr)
if fh < 0:
    print('Number of hours is invalid')
elif fr < 0:
    print('Rate is invalid')
else:    
    if fh > 40:
        pay= 40*fr + (fh-40)*fr*1.5
    elif fh <= 40:
        pay= 40*fr
    print('your pay for the week is $',pay)    
  
