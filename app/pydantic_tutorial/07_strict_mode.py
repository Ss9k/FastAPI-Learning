# 08_strict_mode.py
from pydantic import BaseModel, ConfigDict, ValidationError


class StrictStudent(BaseModel):
    model_config = ConfigDict(strict=True)
    age: int


# Valid exact type
print(StrictStudent(age=21))

# Invalid type conversion under strict mode
try:
    StrictStudent(age="21")
except ValidationError as e:
    print("\nStrict Mode prevented automatic type conversion:")
    print(e)