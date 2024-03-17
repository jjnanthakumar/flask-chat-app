from string import ascii_letters
import random

def getRoomCode(length: int, existing_codes: list[str]) -> str:
    while True:
        code_chars = [random.choice(ascii_letters) for _ in range(length)]
        code = ''.join(code_chars)

        if code not in existing_codes:
            return code
