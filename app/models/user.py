from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class User:
    user_name: str
    password: str
    email: str
    created_at: datetime = datetime.now()
    id: Optional[int] = None

    def create_user(self):
        ...

    def update_user(self):
        ...

    def delete_user(self):
        ...
