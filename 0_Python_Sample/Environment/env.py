import os
from dotenv.main import load_dotenv

load_dotenv()

user = os.environ.get('SWITCHUSER')
print(user)
