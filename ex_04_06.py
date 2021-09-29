shours = input('Hours:')
srate = input ('Rate:')

def computepay(hours,rate):
    hours = float(shours)
    rate = float(srate)
    if hours > 40:
        pay = 40*rate + (hours-40)*rate*1.5
    else:
        pay = rate*hours
    return(pay)

print('Your pay is $',computepay(shours,srate))
