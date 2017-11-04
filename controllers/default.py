def index():
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))
# start
# Arjun @arjuntherajeev
# Caesar Cipher 
# Reference:- www.inventwithpython.com
def validateKey(key):
	if(key in range(1,27)):
		return True
	else:
		return False
    
def encodeCipher(msg,key):
	result = ""
	for ch in msg: 
		if ch.isalpha():
			num = ord(ch)
			num = num + key
			if ch.isupper():
				if num > ord('Z'):
					num = num - 26
				elif num < ord('A'):
					num = num + 26
			elif ch.islower():
				if num > ord('z'):
					num = num - 26
				elif num < ord('a'):
					num = num + 26 
			result = result + chr(num)
		else: 
			result = result + ch
	return result

def echo(): 
    a = encodeCipher(request.vars.message, int(request.vars.key))
    return a

def decode():
    return dict()

# Vigenere :) 
from itertools import cycle
ALPHA = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def encrypt(key, plaintext):
    pairs = zip(plaintext, cycle(key))
    result = ''
    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) + ALPHA.index(y), pair)
        result += ALPHA[total % 26]
    return result.lower()

def decrypt(key, ciphertext):
    pairs = zip(ciphertext, cycle(key))
    result = ''
    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) - ALPHA.index(y), pair)
        result += ALPHA[total % 26]
    return result

def show_result(plaintext, key):
    encrypted = encrypt(key, plaintext)
    decrypted = decrypt(key, encrypted)
    print 'Key: %s' % key
    print 'Plaintext: %s' % plaintext
    print 'Encrytped: %s' % encrypted
    print 'Decrytped: %s' % decrypted

def v_echo():
    encrypted = encrypt(request.vars.v_key, request.vars.v_message)
    return(encrypted)

def v_decode():
    decrypted = decrypt(request.vars.v_key1, request.vars.v_message1)
    return(decrypted)
