from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():
    def bcrypt_password(password: str):
        hashed_password = pwd_cxt.hash(password)
        return hashed_password
