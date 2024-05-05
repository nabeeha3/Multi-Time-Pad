import codecs
import re

messages = []
threshold = 2

# open file and take ciphertexts as input
filename = "ciphers.txt"
try:
	with open(filename, 'r') as cFile:
		for line in cFile:
			line = line.strip()
			messages.append(codecs.decode(line, 'hex'))
except:
	print(filename + ' not found')
	exit()

#the cipher text line to be decrypted
try:
	targetFile = "target.txt"
	with open(targetFile, 'r') as tFile:
		for line in tFile:
			line = line.strip()
			target = codecs.decode(line, 'hex')
except:
	print(targetFile + ' not found')

key = [0] * 1024

#XOR ciphertexts
def xor(a, b):
	if(len(a) > len(b)):
		return bytes([x ^ y for (x, y) in zip(a[:len(b)], b)])
	else:
		return bytes([x ^ y for (x, y) in zip(a, b[:len(a)])])

for a in messages:
	zeros = [0] * len(a)
	for b in messages:
		if(a == b):
			continue
		else:
			c = xor(a, b)
			for k in range(len(c)):
				if(re.match(r'[a-zA-Z]', chr(c[k])) or c[k] == 0):
					zeros[k] += 1

	for i in range(len(a)):
		if(zeros[i] >= (len(messages) - threshold)):
			key[i] = (a[i] ^ 0x20)


keyIn = bytes([x for x in key])


msg = "".join([chr(x) for x in xor(keyIn, target)])

print(msg)

try:
	decryptFile = 'decrypt.txt'
	with open(decryptFile, 'w') as dFile:
		dFile.write(msg)
except:
	print(decryptFile + ' not found')
