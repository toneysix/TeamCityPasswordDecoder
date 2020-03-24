from Crypto.Cipher import DES3
from codecs import decode

ciphertext = "YOUR PASSWORD HERE"

key_signed_byte_array = [61, 22, 11, 57, 110, 89, -20, -1, 0, 99, 111, -120, 55, 4, -9, 10, 11, 45, 71, -89, 21, -99, 54, 51]
key_byte_array = [ b & 0xff for b in key_signed_byte_array ]
key = bytes(key_byte_array)

des3_ciphertext = ciphertext.lstrip('zxx')
des3_cipherbytes = decode(des3_ciphertext, 'hex')

cipher = DES3.new(key, DES3.MODE_ECB)

plaintext_padded = cipher.decrypt(des3_cipherbytes)
plaintext = plaintext_padded[:-plaintext_padded[-1]]

print("Decoded password:")
print(plaintext.decode())

