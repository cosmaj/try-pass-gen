import string
import secrets


def get_random_secret_key(length=100):
    if length < 8:
        raise ValueError(
            "Password length should be at least 8 to ensure stronger security"
        )

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    password = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digits),
        secrets.choice(punctuation),
    ]
    secrets.SystemRandom().shuffle(password)
    all_characters = lower + upper + digits + punctuation
    remaining_chars = length - 4
    password.extend(
        all_characters[b % len(all_characters)]
        for b in secrets.token_bytes(remaining_chars)
    )

    secrets.SystemRandom().shuffle(password)

    return "".join(password)
