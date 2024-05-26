from Crypto.PublicKey import RSA

def generate_rsa_key(bits=2048):
    key = RSA.generate(bits)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# 10개의 2048비트 RSA 키 생성
for i in range(10):
    private_key, public_key = generate_rsa_key()
    print(f"Private Key {i+1}:\n{private_key.decode('utf-8')}\n")
    print(f"Public Key {i+1}:\n{public_key.decode('utf-8')}\n")
