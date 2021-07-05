import hashlib

str_info = input("Enter string to be hashed: \n")

#To generate md5 of string data

result = hashlib.md5(str_info.encode()).hexdigest()

print('The result generated after hashing is: ', result)