import unittest
from aes import AES

class TestBlock(unittest.TestCase):
    def setUp(self):
        key = b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c'
        self.aes = AES(key)

    def test_success(self):
        message = b'\x32\x43\xf6\xa8\x88\x5a\x30\x8d\x31\x31\x98\xa2\xe0\x37\x07\x34'
        ciphertext = self.aes.encrypt_block(message)

def run():
    unittest.main()

if __name__ == '__main__':
    run()