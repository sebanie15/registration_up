import pathlib

DB_PATH: pathlib.Path = pathlib.Path(__file__).parent.absolute() / 'users.json'

if __name__ == '__main__':
	print(DB_PATH)
