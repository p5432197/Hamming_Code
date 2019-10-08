# Hamming_Code
A channel coding for wireless network

## How does Hamming Coding work
If there is a 8-bit data, 10101001.

We can use 4-bit check bit to encode the data.

Because 4+8 = 12, using 4-bit check bit can represent the all situations.

## How to encode the data
Step 1: Choosing the position for binary data 1. So we choose 1, 4, 6 and 8.

Step 2: 1 in binary is 0001, 4 in binary is 0100, 6 in binary is 0110 and 8 in binary is 1000

Step 3: Do XOR operation for those four binary data. So the encoded hamming code is 1011.

Step 4: Put 1011 into original data 10101001. 

Step 5: So the encoded hamming code is 101011000111.

​                                                     
