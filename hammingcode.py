import random

fp=open("output(hamming)_108064501.txt","w")
#random 1Kbits for binary data
x=[]
checkbit=[]
recv=[]
errcount=0
counter1=len(x)
counter2=len(checkbit)
counter3=len(x)
counter4=len(checkbit)
hamming=0
syndrome=0
while counter1<1024:
    if random.random()<0.5:
        x.append(0)
        counter1=counter1+1
    else:
        x.append(1)
        checkbit.append(counter1)
        counter1=counter1+1
print("Original data=",x)
fp.write("Original data=")
for i in x:
    fp.write(str(i))
#Hamming Coding, need check bits=11
while counter2<len(checkbit):
    hamming=int(format(checkbit[counter2],'b'),2) ^ int(format(hamming,'b'),2)
    counter2=counter2+1
print("Hamming Code=",'{0:b}'.format(hamming).zfill(11))
fp.write("\nHamming Code=")
fp.write('{0:b}'.format(hamming).zfill(11))
#Ruinning the data
ruinnum=random.randint(0,1023)
print("ruinplace=",ruinnum)
fp.write("\nruinplace=")
fp.write(str(ruinnum))
if x[ruinnum]==0:
    x[ruinnum]=1
else:
    x[ruinnum]=0
print("Defective data=",x)
fp.write("\nDefective data=")
for i in x:
    fp.write(str(i))
while counter3<len(x):
    if x[counter3]==1: 
        recv.append(counter3)
    counter3=counter3+1
#Using the ruin data to do Hamming Coding
while counter4<len(recv):
    syndrome=int(format(recv[counter4],'b'),2) ^ int(format(syndrome,'b'),2)
    counter4=counter4+1
syndrome=int(format(hamming,'b'),2) ^ int(format(syndrome,'b'),2)
print("syndrome=",syndrome,"=",'{0:b}'.format(syndrome).zfill(11))
fp.write("\nsyndrome=")
fp.write('{0:b}'.format(syndrome).zfill(11))
fp.write("=")
fp.write(str(syndrome))
#Compare the original data and decoded data
for i in range(0,1024):
    if i == ruinnum:
        errcount=errcount+1
print("The number of bit(s) error detected:",errcount)
fp.write("\nThe number of bit(s) error detected:")
fp.write(str(errcount))
if syndrome==ruinnum:
    print("Corrected!")
    fp.write("\nCorrected!")
else:
    print("Not Corrected!")
    fp.write("\nNot Corrected!")
fp.close()