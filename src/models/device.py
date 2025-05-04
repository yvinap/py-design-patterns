from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Device:
    name: str
    model: str
    vendor: str
    type: str
    id: Optional[str] = None
    date_added: Optional[datetime] = None
    date_modified: Optional[datetime] = None