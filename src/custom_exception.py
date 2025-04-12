import requests

class NotFoundError(Exception):
    pass

def get_url(url: str) -> None | str:
    response = requests.get(url)
    if response.status_code == 200:
        return "halaman ditemukan"
    elif response.status_code == 404:
        raise NotFoundError("halaman tidak ditemukan")

try:
    result = get_url("https://stackoverflow.com/salah")
    print(result)
except NotFoundError as e:
    print(f"terjadi kesalahan: {e}")