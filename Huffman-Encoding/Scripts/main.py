from utils import *

# Filenames
inputFile = "../Files/file3input.txt"
encodedFile = "../Files/file3encoded.txt"
decodedFile = "../Files/file3decoded.txt"

# Get the Character Array from the given input file
charArray = ConvertFileToCharArray(inputFile)

startMakeCode = time.time()

# Create a Frequency Table of the characters in the input file
freqTable = CreateFreqTable(charArray)

# Create the Huffman Tree based on the Frequency Table
huffmanTree = CreateHuffmanTree(freqTable)

# Create the Huffman Code Dictionary from the Huffman Tree
huffmanCode = {}
GenerateHuffmanCode(huffmanTree, huffmanCode, "")

endMakeCode = time.time()

# Print the Huffman Code Dictionary
PrintHuffmanCode(huffmanCode)

print("Code Generation Time\t: {} ms".format((endMakeCode - startMakeCode) * 1000))

# Use the Huffman Code Dictionary to encode the input file
EncodeFile(inputFile, encodedFile, huffmanCode)

# Use the Huffman Code Dictionary to decode the encoded file
DecodeFile(encodedFile, decodedFile, huffmanCode)

# Compare the original file size with the encoded file size
CompareFileSizes(inputFile, encodedFile)

# Compare the original file content with the decoded file content
CompareFileContents(inputFile, decodedFile)
