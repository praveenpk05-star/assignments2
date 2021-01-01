
#Develop Power Consumption Calc app
bill=int(input('no.of units of power consumption:' ))

print('units', bill)
if bill<=50:
    print('Bill amount:', 3*bill)
elif bill>=51 & bill<=100:
    print('Bill amount:', 6*bill)
elif bill>=151 & bill<=200:
    print('Bill amount:', 12*bill)
elif bill>=201:
    print('Bill amount:', 15*bill)



