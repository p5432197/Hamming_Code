import random
x=[]         #Original data for 1024bits
checkbit=[]  #Check bits for original data for 11bits
recv=[]      #The received data.It might be ruin for one or more bits
counter1=len(x)
counter2=len(checkbit)
counter3=len(x)
counter4=len(checkbit)
hamming=0    #hamming is a XOR result for all of the places in binary in data which stand for 1 
syndrome=0   #syndrome is using received data to do Hamming Coding.If there is no error for received data, the syndrome will be all 0

###          Random create a 1Kbits(1024bits) for original data          ###
while counter1<1024:
    if random.random()<0.5:
        x.append(0)
        counter1=counter1+1
    else:
        x.append(1)
        checkbit.append(counter1)
        counter1=counter1+1
###          End          ###

###          Hamming Coding, need check bits=11          ###
while counter2<len(checkbit):
    hamming=int(format(checkbit[counter2],'b'),2) ^ int(format(hamming,'b'),2)
    counter2=counter2+1
###          End          ###    

###          Ruinning the data          ###
ruinnum=random.randint(0,1023)
if x[ruinnum]==0:
    x[ruinnum]=1
else:
    x[ruinnum]=0
while counter3<len(x):
    if x[counter3]==1: 
        recv.append(counter3)
    counter3=counter3+1
###          End          ### 

###          Using the ruin data to do Hamming Coding          ###
while counter4<len(recv):
    syndrome=int(format(recv[counter4],'b'),2) ^ int(format(syndrome,'b'),2)
    counter4=counter4+1
syndrome=int(format(hamming,'b'),2) ^ int(format(syndrome,'b'),2)
###          End          ### 
