import time
timestamp = (time.strftime('%H:%M:%S'))
print(timestamp)
timestamphr = int(time.strftime('%H'))

if(timestamphr>4 and timestamphr<12):
    print("Goodmorning")
elif(timestamphr>=12 and timestamphr<17):
    print("Goodafternoon")
elif(timestamphr>16 and timestamphr<21):
    print("Goodevening")
else:
    print("Goodnight<3")
    