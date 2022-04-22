from Crypto.Cipher import Salsa20
import hashlib

def convert_passphrase_to_key(passphrase: str) -> str:
    """
    Convert user passphrase of variable length to a key of set length that can be used as an encryption key.
    """
    # Hash passphrase with the shake_128 algorithm, giving us a set length of 128 bits, which can be used as a key
    hashed_p_phrase = hashlib.shake_128(passphrase.encode('utf-8')).hexdigest(16) # https://docs.python.org/3/library/hashlib.html#shake-variable-length-digests
    return hashed_p_phrase


def encrypt(string: str, key) -> str:
    """
    Encrypt user text with key
    """
    # https://pycryptodome.readthedocs.io/en/latest/src/cipher/salsa20.html
    cipher = Salsa20.new(key=key.encode())
    data = cipher.nonce + cipher.encrypt(string.encode())
    return data.hex() #https://stackoverflow.com/a/36149089



def decrypt(string: str, key) -> str:
    """
    Decrypt user text with key
    """
    string = bytes.fromhex(string) #https://stackoverflow.com/a/36149089
    # https://pycryptodome.readthedocs.io/en/latest/src/cipher/salsa20.html
    msg_nonce = string[:8]
    ciphertext = string[8:]
    cipher = Salsa20.new(key=key.encode(), nonce=msg_nonce)
    plaintext = cipher.decrypt(ciphertext)

    try:
        plaintext = plaintext.decode()
    except UnicodeDecodeError:
        plaintext = None
    
    return plaintext