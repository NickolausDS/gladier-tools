from gladier import GladierBaseTool, GladierBaseClient, generate_flow_definition
from pprint import pprint


def encrypt(**data):
    import os
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    import base64

    password = bytes(data['encrypt_key'], 'utf-8')
    salt = b'\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00'
    # salt = os.urandom(16)

    # PBKDF2HMAC is a key derivation function, which is used to derive a
    # URL-safe base64-encoded 32-byte key from the initial user input password
    # Cryptography library documentation: https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32,
                     salt=salt, iterations=100000)
    key = base64.urlsafe_b64encode(kdf.derive(password))
    fernet = Fernet(key)

    infile = data['encrypt_input']
    if '~' in infile:
        infile = os.path.expanduser(infile)

    outfile = infile+".aes"

    if os.path.isdir(infile):
        raise Exception(
            "Please input the path to a file or a tarred directory.")

    # opening the original file to encrypt
    with open(infile, 'rb') as file:
        original = file.read()

    # encrypting the file
    encrypted = fernet.encrypt(original)

    # opening the file in write mode and
    # writing the encrypted data
    with open(outfile, 'wb+') as encrypted_file:
        encrypted_file.write(encrypted)

    return outfile


@generate_flow_definition
class Encrypt(GladierBaseTool):
    funcx_functions = [encrypt]
    required_input = [
        'encrypt_input',
        'encrypt_key',
        'funcx_endpoint_compute'
    ]
