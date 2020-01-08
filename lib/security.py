import hashlib
import secrets

def app_secret_key():
    return secrets.token_hex(32)

def checksum(path):
    md5hash = hashlib.md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            md5hash.update(chunk)
    return md5hash.hexdigest()
