from dotenv import load_dotenv
import os

def load_env():
    dotenv_path = os.path.join(os.path.dirname((os.path.abspath(__file__))), '.env')
    load_dotenv(dotenv_path)

load_env()