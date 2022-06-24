from typing import Union

Buffer = Union[bytes, bytearray, memoryview]

class FF3:
    def __init__(self, radix: int, alphabet: str, key: Buffer) -> None: ...
    def _num_radix(self, X): ...
    def _num(self, X): ...
    def _str_m_radix(self, m, x): ...
    def _rev(self, X: str): str
    def _revb(self, X: Buffer): Buffer
    def _check_numeral_string(self, X: str): None
    def _convert_tweak(self, T_56: Buffer): Buffer
    def _encrypt_numeral_string(self, X: str, T: Buffer): str
    def _decrypt_numeral_string(self, X: str, T: Buffer): str
    def encrypt(self, pt: str, T_56: Buffer): str
    def decrypt(self, pt: str, T_56: Buffer): str
