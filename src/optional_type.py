import json
import requests

from typing import Optional

def get_user_profile(user_id: int) -> Optional[dict]:
    url: str = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

user_profile: Optional[dict] = get_user_profile(9999999)
result = json.dumps(user_profile, indent=4)
print(result)