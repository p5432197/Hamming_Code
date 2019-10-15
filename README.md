# Hamming_Code
A channel coding for Wireless Network

## How does Hamming Coding work
If there exist a 8-bit data, 10101001.

We can use 4-bit check bit to encode the data.

Because 4+8 = 12, using 4-bit check bit can represent the all situations.

## How to encode the data
Step 1: Choosing the position for binary data 1. So we choose 1, 4, 6 and 8.

Step 2: 1 in binary is 0001, 4 in binary is 0100, 6 in binary is 0110 and 8 in binary is 1000.

Step 3: Do XOR operation for those four binary data. So the encoded hamming code is 1011.

Step 4: Put 1011 into original data 10101001. 

Step 5: So the encoded hamming code is 101010011011.
                                                   
## How to decode the data
Step 1: Pick up the all 1 binary number positions in encoded hamming code 101010011011.

Step 2: All 1 binary number position are 

Step 3: Exclude the 2**n position, so the 1 binary number position are 3, 7, 10, 12.

Step 4: 3 in binary is 0011, 7 in binary is 0111, 10 in binary is 1010, 12 in binary is 1100.

Step 5: Do XOR operation for those four binary number and hamming code 1011. So get the syndrome 0000 which means no error happened.

