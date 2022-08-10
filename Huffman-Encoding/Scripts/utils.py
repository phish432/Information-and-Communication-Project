import time

# A treeNode class to store the Huffman tree nodes
class treeNode:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right


# Function to create a character array from a file
def ConvertFileToCharArray(filename):
    charArray = []
    with open(filename, "r") as f:
        for ch in f.read():
            charArray.append(ch)
    return charArray


# Function to read a character array and create a frequency table
def CreateFreqTable(charArray):
    # Create a dictionary to store the frequency of each character
    freqTable = {}
    for char in charArray:
        if char in freqTable:
            freqTable[char] += 1
        else:
            freqTable[char] = 1

    # Create a list of tree nodes from the frequency table dictionary
    M = []
    for char, freq in freqTable.items():
        M.append(treeNode(char, freq))
    return M


# Function to create the Huffman tree from the frequency table
def CreateHuffmanTree(freqTable):
    # Till we have only one node in the list
    while len(freqTable) > 1:
        # Sort the list in ascending order of the frequency
        freqTable.sort(key=lambda node: node.freq)

        # Take the two lowest probability nodes and combine them
        left = freqTable.pop(0)
        right = freqTable.pop(0)
        mergeFreq = left.freq + right.freq
        newNode = treeNode(None, mergeFreq, left, right)

        # Add the new node to the list
        freqTable.append(newNode)

    return freqTable[0]


# Recursive Function to generate the Huffman code from the Huffman tree
def GenerateHuffmanCode(huffmanTree, code, string):
    # Base Case : If we are at leaf node, then the string is the codeword for the leaf node
    if huffmanTree.left == None and huffmanTree.right == None:
        code[huffmanTree.char] = string

    # Recursive Case : If we are not at leaf node,
    # then recursively call the function on the left and right subtrees
    else:
        GenerateHuffmanCode(huffmanTree.left, code, string + "0")
        GenerateHuffmanCode(huffmanTree.right, code, string + "1")


# Function to print the Huffman code for a given file
def PrintHuffmanCode(code):
    print("Huffman Code\n")
    print("Char\t--->\tCodeword")
    for char, string in code.items():
        # Special case for newline character
        if char == "\n":
            char = "\\n"
        print("'{}'\t--->\t{}".format(char, string))
    print()


# Function to encode/compress a file using Huffman coding
def EncodeFile(inputFile, encodedFile, code):
    with open(inputFile, "r") as f, open(encodedFile, "w") as g:

        startEncode = time.time()

        for char in f.read():
            g.write(code[char])

        endEncode = time.time()
        print("Encoding Time\t\t: {} ms".format((endEncode - startEncode) * 1000))


# Function to decode a file which is encoded using Huffman coding
def DecodeFile(encodedFile, decodedFile, huffmanCode):
    with open(encodedFile, "r") as f, open(decodedFile, "w") as g:
        startDecode = time.time()

        # Invert the Huffman code dictionary
        inverseHuffmanCode = InvertDict(huffmanCode)
        s = ""
        for char in f.read():
            # Append the character to the string
            s += char

            # If the string is a valid Huffman code, then we have found the corresponding character
            if s in inverseHuffmanCode:
                g.write(inverseHuffmanCode[s])
                s = ""

        endDecode = time.time()
        print("Decoding Time\t\t: {} ms".format((endDecode - startDecode) * 1000))


# Function to invert a dictionary
# We are guaranteed a one-one mapping in Huffman coding
# So the inverse dictionary is a valid mapping
def InvertDict(D):
    invD = {}
    for key, value in D.items():
        invD[value] = key
    return invD


# Function to compare the lengths of two files
def CompareFileSizes(inputFile, encodedFile):
    with open(inputFile, "r") as f, open(encodedFile, "r") as g:
        # Size of the input file in bytes
        inputSize = float(len(f.read()))

        # Size of the encoded file in bytes
        # Since the encoded file is in ASCII, each character takes 8 bits
        # But while encoding, we only using 1 bit for each character
        # So, we need to divide by 8 to get the actual size of the encoded file while compressing
        encodedSize = float(len(g.read()) / 8)

    print("Size of Original File\t: {} Bytes".format(inputSize))
    print("Size of Encoded File\t: {} Bytes".format(encodedSize))


# Function to compare the contents of two files
def CompareFileContents(inputFile, encodedFile):
    with open(inputFile, "r") as f, open(encodedFile, "r") as g:
        # Compare the contents of the input and encoded files
        for i, j in zip(f.read(), g.read()):
            if i != j:
                print("File Contents Do Not Match")
                break
        else:
            print("File Contents Match")
