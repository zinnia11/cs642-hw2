# /usr/bin/env python3

# CS 642 University of Wisconsin
#
# usage: python3 attack.py ciphertext
# Outputs a modified ciphertext and tag

debug = 0
debug2 = 0
debug3 = 0

import sys
import array

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

modified_msg = mutableFullCiphertext
if(debug3):print(len(modified_msg))
if(debug3):print(modified_msg[100])
modified_msg[100] = '0'
#for i in range(100, 110):
#  modified_msg[i] = '0'
if(debug3):print(modified_msg[100])
if(debug2): print("ciphertextWithTag.hex() = \n" + str(ciphertextWithTag.hex()))
if(debug2): print()
if(debug2): print("modified_msg = ")
#if(debug2): print("modified_msg = \n" +str(modified_msg)[12:len(str(modified_msg))-2])
print(str(modified_msg)[12:len(str(modified_msg))-2])
#print(str(tag.hex()) + str(modified_msg)[12+len(str(tag.hex())):len(str(modified_msg))-2])