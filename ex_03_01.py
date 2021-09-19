hours = input('How many hours did you work this week? ')
rate = input ('What is your hourly rate? ')
# At this point I could also change the inputs to float
if float(hours )<= 40:
    pay = float(hours)*float(rate)
    # print('you will get regular pay')
else:
    pay = (40*float(rate))+(float(hours)-40.0) *float(rate)*1.5
    # print('you are getting paid overtime')

print('Your pay for this week is: $',pay)
