
import json
from db.config import DB_PATH
from utilities.utilities import encrypt


class User:

	def __init__(self, first_name, second_name, email, user_name, password):
		self.first_name = first_name
		self.second_name = second_name
		self.email = email
		self.user_name = user_name
		self.password = encrypt(password)

	@property
	def full_name(self) -> str:
		return f'{self.first_name} {self.second_name}'

	def __repr__(self) -> str:
		return self.full_name

