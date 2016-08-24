import hashlib
import os

password = "password"
salt = os.urandom(16)

m = hashlib.md5()
m.update(salt + password)
m.hexdigest()


from passlib.hash import pbkdf2_sha256

hash = pbkdf2_sha256.encrypt("password", rounds=200000, salt_size=16)


from passlib.hash import pbkdf2_sha256

pbkdf2_sha256.verify("password", hash)

print('What is the password? ')