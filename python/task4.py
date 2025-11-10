# orders_data.py
from typing import List, Dict, Any

Order = Dict[str, Any]
ORDERS: List[Order] = [
    {"id": 101, "total": 29.99, "created": "2025-01-15T09:30:00", "customer": {"first": "Ana", "last": "Zhang"}},
    {"id": 102, "total": 120.00, "created": "2025-01-14T16:10:00", "customer": {"first": "Ben", "last": "Adams"}},
    {"id": 103, "total": 120.00, "created": "2025-01-14T08:05:00", "customer": {"first": "Ben", "last": "Adams"}},
    {"id": 104, "total": 75.50, "created": "2025-01-13T12:00:00", "customer": {"first": "Cara", "last": "Lopez"}},
]


#print(ORDERS[1])
#print(ORDERS[1].keys)
print(ORDERS[1]["customer"]["last"])

#write a loop that checks compares the first letter of each last name and stores alphabetic order in new list

#for i in range(4):
 #   print(ORDERS[i]["customer"]["last"])
  #  if (ORDERS[i][total] < ORDERS[i+1][total]):

#print(ORDERS.sort())

