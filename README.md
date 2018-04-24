# password_generator

The purpose of this project is to protect your passwords. Normal people might use the same password with meaningful phrases in it for multiple websites / accounts, which is vulnerable under attacks.

But if we could generate unique hashed passwords from original passwords by cryptology algorithms, simply remember the original unsafe passwords and let the algorithm generate hashed passwords, things become easier and safer.

In addition to just the hash process, I used a "salt" string to be appended to original password strings to generate hard-to-crack passwords. By the way, if you're generating multiple passwords, the salt itself is constantly self-evolving, which makes it even harder for malicious people to crack the salt (if they know both your original and generated passwords, salt is still safe).

So as long as you remember your "salt" and several original simple passwords, downloading and running the python script could generate your safe passwords elsewhere even if you lost your original device.

The schema for seed.txt:
line1: salt
line2+: the original passwords, one by one for each line
e.g.:
this is a salt string
this is pwd1
this is pwd2
this is pwd3
