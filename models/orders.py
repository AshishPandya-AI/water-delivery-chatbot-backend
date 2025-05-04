from pydantic import BaseModel

class Order(BaseModel):
    order_number: str  # 6-digit order number
    customer_name: str
    product_name: str
    status: str
    order_date: str