import hashlib
from typing import Dict, Optional


class Sha256Hasher:
    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()


class InMemoryUserStore:
    def __init__(self) -> None:
        self._users: Dict[str, str] = {}

    def user_exists(self, username: str) -> bool:
        return username in self._users

    def add_user(self, username: str, password_hash: str) -> None:
        self._users[username] = password_hash

    def get_password_hash(self, username: str) -> Optional[str]:
        return self._users.get(username)


class AuthService:
    def __init__(self, store: InMemoryUserStore, hasher: Sha256Hasher) -> None:
        self.store = store
        self.hasher = hasher

    def register_user(self, username: str, password: str) -> str:
        if self.store.user_exists(username):
            return "Error: Username already exists."
        self.store.add_user(username, self.hasher.hash_password(password))
        return "Registration successful."

    def login_user(self, username: str, password: str) -> str:
        stored_hash = self.store.get_password_hash(username)
        if stored_hash is None:
            return "Error: User not found."
        if stored_hash == self.hasher.hash_password(password):
            return "Login successful."
        return "Error: Incorrect password."


_store = InMemoryUserStore()
_hasher = Sha256Hasher()
_auth = AuthService(_store, _hasher)


def register_user(username: str, password: str) -> str:
    return _auth.register_user(username, password)


def login_user(username: str, password: str) -> str:
    return _auth.login_user(username, password)


def main() -> None:
    print("Simple Auth Demo")
    while True:
        choice = input("Choose action: [r]egister, [l]ogin, [q]uit: ").strip().lower()
        if choice == "q":
            break
        if choice == "r":
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            print(register_user(username, password))
            continue
        if choice == "l":
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            print(login_user(username, password))
            continue
        print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()