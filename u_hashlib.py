import hashlib

print(hashlib.algorithms_available) # set of all algo. present including OpenSSL ones
print(hashlib.algorithms_guaranteed) # prints set of algorithms present in the module

# using md5
a=hashlib.md5(b'Hello World') # b before the string converts the strings to bytes
print(a.digest())
print(a.hexdigest())

# using SHA1
print(hashlib.sha1(b'My Name is Khan').hexdigest())

# using SHA512
h=hashlib.sha512()
h.update(b'NewYork') # updates the hash object
print(h.hexdigest())

# using OpenSSL algo.
k=hashlib.new('DSA-SHA')
k.update(b'newyork')
print(k.hexdigest())

l=hashlib.new('DSA-SHA')
l.update(b'new')
l.update(b'york')
 # this will be same as above bcoz after updating the same hash object has been created
print(l.hexdigest())
print(l.block_size) # block size in bytes
print(l.digest_size) # size of resulting hash in bytes
