from dataclasses import dataclass
from typing import Optional


@dataclass
class Category:
    name: str
    id: Optional[int] = None

    def create_category(self):
        ...

    def update_category(self):
        ...

    def delete_category(self):
        ...
