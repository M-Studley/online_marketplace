from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Item:
    title: str
    description: str
    price: float
    category_id: int
    seller_id: int
    created_at: datetime = datetime.now()
    id: Optional[int] = None

    def create_item(self):
        ...

    def update_item(self):
        ...

    def delete_item(self):
        ...
