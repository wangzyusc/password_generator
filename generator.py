import hashlib
import base64

LEN = 26

with open("seed.txt", "r") as f:
    lines = list(f.readlines())
    salt, lines = lines[0], lines[1:]
    for line in lines:
        salt = hashlib.sha224(salt).hexdigest()
        newpwd = base64.b64encode(hashlib.sha224(line + salt).hexdigest())
        print line[:-1] + " -> " + newpwd[:LEN]
