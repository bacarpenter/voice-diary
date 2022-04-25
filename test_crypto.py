#!/usr/bin/env python3
# || ---------- test_crypto.py ---------- ||
# Tests for crypto.py
# 
# Ben Carpenter and Nancy Onyimah
# April 24, 2022
# ------------- test_crypto.py -------------


from crypto import convert_passphrase_to_key, encrypt, decrypt

def test_convert_passphrase_to_key():
    """
    Test that:
        1. Different strings create different keys
        2. All keys are 128 bits long (32 chars)
    """

    str_1 = "The cow jumped over the moon"
    str_2 = "The mouse ran up the clock"

    assert convert_passphrase_to_key(str_1) != convert_passphrase_to_key(str_2)
    assert len(convert_passphrase_to_key(str_1)) == 32 and len(convert_passphrase_to_key(str_2)) == 32

def test_encrypt():
    """
    Test that:
        1. The encrypted form of a message does not equal the un-encrypted form of the message
        2. The same message has diffrent encrypted forms with diffrent keys
        3. Different messages have diffrent encrypted forms with the same key
    """

    key_1 = convert_passphrase_to_key("The cow jumped over the moon")
    key_2 = convert_passphrase_to_key("The mouse ran up the clock")

    str_1 = "I went to the barn and there was no hay"
    str_2 = "I left the barn and found hay on the ground"

    assert encrypt(str_1, key_1) != str_1
    assert encrypt(str_1, key_1) != encrypt(str_1, key_2)
    assert encrypt(str_1, key_1) != encrypt(str_2, key_1)

def test_decrypt():
    """
    Test that:
        1. A message is the same after being encrypted then decrypted
        2. A message decrypted with the wrong key returns None
    """

    key_1 = convert_passphrase_to_key("The cow jumped over the moon")
    key_2 = convert_passphrase_to_key("The mouse ran up the clock")

    str_1 = "I went to the barn and there was no hay"

    encrypted= encrypt(str_1, key_1)

    assert decrypt(encrypted, key_1) == str_1
    assert decrypt(encrypted, key_2) == None
    