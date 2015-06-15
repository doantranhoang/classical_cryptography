#!/usr/bin/env python
# author:	Hoang Doan
# date:		21/05/2015
# From wiki (http://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

import string, sys

class ClassicCryptoVigenere:
	def __init__(self, secret_key = ''):
		self.KEY = secret_key.upper()
		self.PLAIN_TEXT = ''
		self.CIPHER_TEXT = ''
		self.vigenere_square = []
		self.uppercase_chars = string.ascii_uppercase
		for i in xrange(0, 26):
			row = []
			chars = self.uppercase_chars[i:] + self.uppercase_chars[:i]
			for c in chars:
				row.append(c)
			self.vigenere_square.append(row)

	def key_alignment(self, pt_length):
		while len(self.KEY) < pt_length:
			self.KEY += self.KEY
		self.KEY = self.KEY[:pt_length]
		return self.KEY

	def encrypt(self, plain_text = ''):
		plain_text = plain_text.strip().upper()
		self.key_alignment(len(plain_text))
		self.CIPHER_TEXT = ''
		for p in xrange(0, len(plain_text)):
			if plain_text[p] in self.uppercase_chars:
				c = self.uppercase_chars.index(plain_text[p])
				r = self.uppercase_chars.index(self.KEY[p])
				self.CIPHER_TEXT += self.vigenere_square[c][r] 
			else:
				self.CIPHER_TEXT += plain_text[p]
		return self.CIPHER_TEXT

	def decrypt(self, cipher_text):
		cipher_text = cipher_text.strip().upper()
		self.key_alignment(len(cipher_text))
		self.PLAIN_TEXT = ''
		for p in xrange(0, len(self.KEY)):
			if cipher_text[p] in self.uppercase_chars:
				r = self.uppercase_chars.index(self.KEY[p])
				c = self.vigenere_square[r].index(cipher_text[p])
				self.PLAIN_TEXT += self.uppercase_chars[c]
			else:
				self.PLAIN_TEXT += cipher_text[r]
		return self.PLAIN_TEXT

def __main__():
	if (len(sys.argv) < 3):
		print '[+] Usage:'
		print "\t$ python vigenere.py <act> <key> <data>"
		print "\tWith:\n\t\t<act>\t: 'enc' for encryption or 'dec' for decryption\n\t\t<key>\t: secret key\n\t\t<data>\t: text for processing"
		exit(1)

	for c in (sys.argv[1]+sys.argv[2]):
		if c not in string.ascii_letters:
			print '[+] Error: Only ASCII letters accepted in secret key and message!'
			exit(1)

	vigenere = ClassicCryptoVigenere(sys.argv[2]) # init with secret key
	if (sys.argv[1].strip() == 'enc'):
		print "[+] Key k\t= %s\n[+] Message m\t= %s" %(sys.argv[2].upper(), sys.argv[3].upper())
		print '[+] => E(k, m)\t= %s' %vigenere.encrypt(sys.argv[3]) # encrypt message
	elif (sys.argv[1].strip() == 'dec'):
		print "[+] Key k\t= %s\n[+] Cipher c\t= %s" %(sys.argv[2].upper(), sys.argv[3].upper())
		print '[+] => D(k, c)\t= %s' %vigenere.decrypt(sys.argv[3]) # decrypt message
	else:
		print '[+] Error: Action invalid! "enc" or "dec"?'

__main__()
