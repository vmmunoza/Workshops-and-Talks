from Crypto.PublicKey import DSA
from Crypto.Random import random
from Crypto.Hash import SHA

"""
This code snippet demonstrates a ZKP where the prover knows the discrete logarithm x of y to the base g modulo p without revealing x. 
The prover generates a random k, computes r and s, and sends them to the verifier. 
The verifier then computes v and checks if it equals r. 
If it does, the verifier is convinced that the prover knows x without actually learning its value.
"""

# Generate a DSA key pair (public and private)
key = DSA.generate(1024)

# The public components (known to both prover and verifier)
p = key.p
q = key.q
g = key.g
y = key.y

# The secret to prove knowledge of (only known to the prover)
x = key.x

# The prover generates a proof
k = random.StrongRandom().randint(1, q-1)
r = pow(g, k, p)
e = SHA.new(str(r).encode()).digest()
e = int.from_bytes(e, byteorder='big') % q
s = (k - x*e) % q

# The prover sends (r, s) to the verifier as the proof
proof = (r, s)

# The verifier checks the proof
w = pow(s, q-2, q)
u1 = (e * w) % q
u2 = (r * w) % q
v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

# If v == r, the proof is valid
valid = v == r
print(f"Proof valid: {valid}")
