import json
from pathlib import Path

folder = Path(__file__).resolve().parent
with open(folder / 'profile_sample.json', 'r', encoding='utf-8') as file:
    profile = json.load(file)
print('Логин:', profile['login'])
