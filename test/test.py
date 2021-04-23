from requests import get, post, delete
from CONSTANTS import *


print(get(f"http://{HOST}:{PORT}/api/users").json())
print(get(f"http://{HOST}:{PORT}/api/users/1").json())

print(post(f"http://{HOST}:{PORT}/api/users",
           json={'age': 18, 'email': 'boldirev_as@koriphey.com',
                 'height': 180, 'name': 'Ivan', 'sex': 'm',
                 'surname': 'Boldirev', 'weight': 80}).json())

print(get(f"http://{HOST}:{PORT}/api/users").json()['users'][-1])

print(delete(f"http://{HOST}:{PORT}/api/users/3"))

print(get(f"http://{HOST}:{PORT}/api/users").json()['users'][-1])
