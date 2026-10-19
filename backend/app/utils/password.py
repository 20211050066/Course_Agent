import bcrypt


def hash_password(password: str) -> str:
    """
    Hashes a password using a secure hashing algorithm.

    Args:
        password (str): The plaintext password to hash.

    Returns:
        str: The hashed password.
    """

    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verifies a plaintext password against a hashed password.

    Args:
        password (str): The plaintext password to verify.
        hashed_password (str): The hashed password to compare against.

    Returns:
        bool: True if the password matches the hash, False otherwise.
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
