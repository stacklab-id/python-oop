from enum import StrEnum

class Gender(StrEnum):
    MALE = "Laki-laki"
    FEMALE = "Perempuan"
    UNKNOWN = "Tidak diketahui"

for gender in Gender:
    print(f"{gender.name} = {gender.value}")
