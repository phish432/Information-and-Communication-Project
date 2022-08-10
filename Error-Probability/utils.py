import random
import matplotlib.pyplot as plt

# Generate a random code
# By picking 2^k random vectors from the binary vector space {0, 1}^n
def GenerateCode(n, k):
    code = []
    for i in range(2**k):
        codeword = []
        for j in range(n):
            codeword.append(random.randint(0, 1))
        code.append(codeword)
    return code


# Selecting a random codeword from the code
def SelectCodeword(code):
    return random.choice(code)


# Binary Symmetric Channel
def BSC(p_error, codeword):
    # For every bit in the codeword, we will flip it with probability p_error
    change = []
    for bit in codeword:
        if random.random() < p_error:
            change.append(flip(bit))
        else:
            change.append(bit)
    return change


# Function to flip a bit
def flip(bit):
    # If bit is 1, make it (1+1)%2 = 0
    # If bit is 0, make it (0+1)%2 = 1
    return (bit + 1) % 2


# Minimum Distance Decoder
def MDD(code, y):
    # Pre-calculate hamming distances
    HDArray = []
    for codeword in code:
        HDArray.append(HammingDistance(codeword, y))

    # Finding the minimum hamming distance
    minHD = min(HDArray)

    # Finding the codewords having minimum hamming distance
    estimatesArray = []
    for i in range(len(code)):
        if HDArray[i] == minHD:
            estimatesArray.append(code[i])

    return estimatesArray


# Hamming Distance
def HammingDistance(c1, c2):
    HD = 0
    for i in range(len(c1)):
        if c1[i] != c2[i]:
            HD += 1
    return HD


# Function to calculate error indicator I
def ErrorIndicator(estimate, c):
    # If there is an error, the error indicator is 1
    # If there is no error, the error indicator is 0
    if estimate != c:
        return 1
    else:
        return 0
