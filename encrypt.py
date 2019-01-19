import array
 
def alphaTobin_conversion(strng):
	res = []
	for i in range (0,len(strng)):
		res.append(ord(strng[i])) #gets ascii value
	result=""
	for d in res:
		#result= result + str(dec_to_bin(d)) #discarded as dec_to_bin is no more returning int
		result= result + dec_to_bin(d)
	return result
		
def dec_to_bin(x):
    #return int(bin(x)[2:]) #returning  7 bits, so discarded
	return format(x,'08b')


def xor(msg,key):
	cipher = ""
	for i in range (0,len(key)):
		if msg[i] == key[i]:
			cipher = cipher + '0'
		else:
			cipher = cipher + '1'
	return cipher

def binToAlpha(cipher):
	#print(len(cipher))
	res = ""
	for i in range (0,len(cipher),8):
		substr1= (cipher[i:i+8])
		print (substr1)
		deci=binToDec(substr1)
		#print (deci)
	#for i in range (0,len(deci)):
		cipher_1=dec_to_char(deci)
		#print(cipher_1)
		res = res + cipher_1
	return res
	
def binToDec(substr):
	return int(substr,2)
	
def dec_to_char(x1):
	return chr(x1)	

	
def decrypt(key_bin):
	k = open("result.txt","r")
	cipher_txt=k.read()
	cipher_txt_len =  len(cipher_txt)
	print(cipher_txt[0:cipher_txt_len-1])
	cipher_bin=alphaTobin_conversion(cipher_txt[0:cipher_txt_len-1])
	print("key in binary - "+key_bin+" Key Length "+str(len(key_bin))+" Cipher in binary - "+cipher_bin+" Cipher Length "+str(len(cipher_bin)))
	msg_bin=xor(cipher_bin,key_bin)
	print(binToAlpha(msg_bin))

	
msg = input('Enter the 4 letter msg : ')
msg_len = len(msg)
msg_bin = alphaTobin_conversion(msg)

#below part accept key from user
#key = input('Enter the 4 letter key : ')
#key_len=len(key)
#if(msg_len==key_len):
#	key_bin = alphaTobin_conversion(key,key_len)
#else:
#	print("Cant do one time padding")
#	exit()

#below  part accept key from file
f = open("key.txt","r")
key_bin=f.read()


print("key in binary - "+key_bin+" Key Length "+str(len(key_bin))+" Msg in binary - "+msg_bin+" Msg Length "+str(len(msg_bin)))
	
#print (xor(msg_bin,key_bin))
cipher = xor(msg_bin,key_bin)	
	
#print(binToAlpha(cipher))
f=open("result.txt","w")
f.write(binToAlpha(cipher))
f.close()
decrypt(key_bin)

