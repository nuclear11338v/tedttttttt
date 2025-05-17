import pytest
from fbh.core import FBH
import os

def test_hide_and_decode():
    fbh = FBH()
    test_file = "test.txt"
    encrypted_file = "test.txt.fbh"
    decrypted_file = "test.txt.dec"
    password = "testpassword"

    # Create a test file
    with open(test_file, "w") as f:
        f.write("Hello, FBH!")

    # Test encryption
    fbh.hide_file(test_file, encrypted_file, password)
    assert os.path.exists(encrypted_file)

    # Test decryption
    fbh.decode_file(encrypted_file, decrypted_file, password)
    assert os.path.exists(decrypted_file)

    # Verify content
    with open(decrypted_file, "r") as f:
        content = f.read()
    assert content == "Hello, FBH!"

    # Clean up
    os.remove(test_file)
    os.remove(encrypted_file)
    os.remove(decrypted_file)

def test_no_password_mode():
    fbh = FBH()
    test_file = "test.txt"
    encrypted_file = "test.txt.fbh"

    with open(test_file, "w") as f:
        f.write("No decrypt!")

    fbh.hide_file(test_file, encrypted_file, password=None)
    assert os.path.exists(encrypted_file)

    # Clean up
    os.remove(test_file)
    os.remove(encrypted_file)
