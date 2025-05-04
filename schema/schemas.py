def list_serial(cursor):
    return [serialize_doc(doc) for doc in cursor]

def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])  # Convert ObjectId to string
    return doc

def serialize_order(order):
    order["_id"] = str(order["_id"])  # Convert ObjectId to string
    return order