from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Order:
    item_id: int
    buyer_id: int
    status: str
    created_at: datetime = datetime.now()
    id: Optional[int] = None

    def create_order(self):
        ...

    def update_order(self):
        ...

    def delete_order(self):
        ...
