import os
from dotenv import load_dotenv

user = os.environ.get('SWITCHUSER')
print(user)
