
from hashlib import sha512


def encrypt(password: str) -> str:
	return sha512(bytes(password, 'utf-8')).hexdigest()
