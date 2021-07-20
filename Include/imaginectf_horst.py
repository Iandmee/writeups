import math
import hashlib
def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

s = "b020563166cfacda8201e8817265baf945b2dc49517f73903241f9fbedd3943d79d17b6ecd6acb45810eb95b1687ead8851fc923fdb40d5e208f3d4a34840bd1"
s = bytes.fromhex(s)
for i in range(25):
	t = hashlib.sha256(s[:32]).digest()
	L = xor(t, s[32:])
	s = L + s[:32]

print(s)

