# /usr/bin/env python3

# CS 642 University of Wisconsin
#
# usage: python3 attack.py ciphertext
# Outputs a modified ciphertext and tag

debug = 0
debug2 = 0
debug3 = 0 #modifying the message
debug4 = 0 #XOR

import sys
import array
import hashlib
import base64

my_message = \
"""AMOUNT: $  99.99
Originating Acct Holder: Alexa
Orgininating Acct #98166-20633

I authorized the above amount to be transferred to the account #51779-31226 
held by a Wisc student at the National Bank of the Cayman Islands.
"""

#first block 
PT1 = "AMOUNT: $  12.99"
my_PT1 = "AMOUNT: $  99.99"

# Grab ciphertext from first argument
ciphertextWithTag = bytes.fromhex(sys.argv[1])
mutableFullCiphertext = array.array('u', sys.argv[1])
#mutableFullCiphertext = bytearray(sys.argv[1], "utf-8")

if len(ciphertextWithTag) < 16+16+32:
  print("Ciphertext is too short!")
  sys.exit(0)

iv = ciphertextWithTag[:16]
ciphertext = ciphertextWithTag[:len(ciphertextWithTag)-32]
tag = ciphertextWithTag[len(ciphertextWithTag)-32:]

# TODO: Modify the input so the transfer amount is more lucrative to the recipient
# PT1 XOR IV
X = bytes(a ^ b for (a, b) in zip(PT1.encode(), iv))
if(debug4): 
  print(PT1.encode().hex())
  print(iv.hex())
  print(X.hex())
#PT1' XOR (PT1 XOR IV)
modified_iv = bytes(a ^ b for (a, b) in zip(my_PT1.encode(), iv))
if(debug4): 
  print(my_PT1.encode().hex())
  print(X.hex())
  print(modified_iv.hex())


# TODO: Print the new encrypted message
# you can change the print content if necessary
if(debug):
  print("iv.hex() = " + str(iv.hex()))
  print()
  print("ciphertext.hex() = " + str(ciphertext.hex()))
  print()
  print("tag.hex() = " + str(tag.hex()))
  print()

if(debug2): print("len(mutableFullCiphertext) = " + str(len(mutableFullCiphertext)))

modified_msg = ciphertext[16:].hex()
#print(ciphertext[16:].decode())

if(debug2): print("ciphertextWithTag.hex() = \n" + str(ciphertextWithTag.hex()))
if(debug2): print()
if(debug2): print("modified_msg = ")
#if(debug2): print("modified_msg = \n" +str(modified_msg)[12:len(str(modified_msg))-2])
#print(str(modified_msg)[12:len(str(modified_msg))-2])
#modified_plaintext = str(modified_msg)[12+len(str(iv.hex())):len(str(modified_msg))-2-len(str(tag.hex()))]
newtag = hashlib.sha256(my_message.encode()).hexdigest()
#print(len(modified_msg))
print(str(modified_iv.hex())+ modified_msg + newtag)
#print(len(str(modified_iv.hex())+ modified_msg + newtag))
#print(str(tag.hex()) + str(modified_msg)[12+len(str(tag.hex())):len(str(modified_msg))-2])