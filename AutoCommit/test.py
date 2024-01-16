from cryptography.fernet import Fernet
import random

passowrd = b""

key = Fernet.generate_key()
fernet = Fernet(key)
encMessage = fernet.encrypt(passowrd)

# print(encMessage)

encPassword = b'gAAAAABlmiaKl2QKeNYW8fan-JPYncBm4A5RVbXNNP2W8tArP7Wl3sHiGQdKMElft503RPx5-Ye1Ej4aNtxz89VzPgiYwX7IvA=='
password = fernet.decrypt(encPassword)

print(password)