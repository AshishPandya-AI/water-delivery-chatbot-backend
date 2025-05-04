from fastapi import APIRouter, Request, HTTPException
from config.database import orders_collection
from schema.schemas import serialize_order
import random
import datetime

router = APIRouter()

def get_order_details(order_number: str):
    try:
        order = orders_collection.find_one({"order_number": order_number})
        if order:
            return serialize_order(order)
        return None
    except Exception as e:
        print(f"Database Error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

def update_order_status(order_number: str, status: str):
    try:
        return orders_collection.update_one(
            {"order_number": order_number}, {"$set": {"order_status": status}}
        )
    except Exception as e:
        print(f"Database Error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/webhook")
async def dialogflow_webhook(request: Request):
    try:
        # Parse the Dialogflow request
        payload = await request.json()
        print("Request Payload:", payload)

        # Extract intent name, parameters, and other fields
        intent = payload["queryResult"]["intent"]["displayName"]
        parameters = payload["queryResult"]["parameters"]
        print("Intent:", intent)
        print("Parameters:", parameters)

        # Extract the order number and last name
        number_param = parameters.get("number")
        person_param = parameters.get("person")
        if number_param and isinstance(number_param, list) and len(number_param) > 0:
            order_number = str(int(number_param[0]))
        else:
            order_number = None

        if person_param and isinstance(person_param, list) and len(person_param) > 0:
            last_name = person_param[0].get("name")
        else:
            last_name = None

        print("Extracted Order Number:", order_number)
        print("Extracted Last Name:", last_name)

        # Handle the "track.order_status" intent
        if intent == "track.order_status":
            if order_number and order_number.isdigit() and len(order_number) == 6:
                # Store the order number in a context for validation
                response_text = "Please provide your last name for verification."
                return {
                    "fulfillmentText": response_text,
                    "outputContexts": [
                        {
                            "name": f"{payload['session']}/contexts/order_context",
                            "lifespanCount": 5,
                            "parameters": {
                                "order_number": order_number,
                            },
                        }
                    ],
                }
            else:
                response_text = "Please provide a valid 6-digit order number."

        # Handle the "Track.order.validation" intent
        elif intent == "Track.order.validation":
            # Retrieve the order number from the context
            contexts = payload["queryResult"].get("outputContexts", [])
            order_number = None
            for context in contexts:
                if "order_context" in context["name"]:
                    order_number = context["parameters"].get("order_number")
                    break

            print("Retrieved Order Number from Context:", order_number)

            if not order_number:
                return {"fulfillmentText": "Please provide your order number first."}

            if last_name:
                # Check if the order exists and validate the last name
                order = orders_collection.find_one({"order_number": order_number, "last_name": last_name})
                print("Database Query Result:", order)
                if order:
                    response_text = (
                        "Your account has been successfully verified.\n"
                        "Order Details:\n"
                        f"Order ID: {order['order_number']}\n"
                        f"Customer Name: {order['first_name']} {order['last_name']}\n"
                        f"Items: {', '.join(order['items'])}\n"
                        f"Capacity: {order['capacity']}\n"
                        f"Quantity: {order['quantity']}\n"
                        f"Status: {order['order_status']}\n"
                        f"Order Date: {order['order_date']}\n"
                    )
                else:
                    response_text = "Sorry, the last name you provided does not match our records. Please try again."
            else:
                response_text = "Please provide your last name for verification."

        # Handle the "new.order.user.phone_number" intent
        elif intent == "new.order.user.phone_number":
            # Extract the phone number from the parameters
            phone_number = parameters.get("phone-number")[0]
            if not phone_number:
                return {"fulfillmentText": "Please provide your phone number."}

            # Retrieve the user details and order details from the context
            contexts = payload["queryResult"].get("outputContexts", [])
            print("Available Contexts:", contexts)

            # Extract first name from the "order-firstname" context
            first_name = None
            for context in contexts:
                if "order-firstname" in context["name"]:
                    first_name = context["parameters"].get("person")[0].get("name") if "person" in context["parameters"] else None
                    break

            # Extract last name from the "order-lastname" context
            last_name = None
            for context in contexts:
                if "order-lastname" in context["name"]:
                    last_name = context["parameters"].get("last-name")[0] if "last-name" in context["parameters"] else None
                    break

            # Extract items from the "Order.item.water_bottle" or "Order.item.water_camper" context
            items = None
            for context in contexts:
                if "select-item-context" in context["name"] or "on-going" in context["name"]:
                    items = context["parameters"].get("items")
                    break

            # Extract quantity from the "Order.quntity.confirm" context
            quantity = None
            for context in contexts:
                if "confirm-quantity-selaction" in context["name"]:
                    quantity = context["parameters"].get("number")[0] if "number" in context["parameters"] else None
                    break

            # Extract capacity from the "quantity-selection" context
            capacity = None
            for context in contexts:
                if "quantity-selection" in context["name"]:
                    capacity = context["parameters"].get("size")[0] if "size" in context["parameters"] else None
                    break

            # Validate that all required details are present
            if not (first_name and last_name and items and quantity and capacity):
                print("Missing Details:", first_name, last_name, items, quantity, capacity)
                return {"fulfillmentText": "Some details are missing. Please provide all required information."}

            # Generate a unique 6-digit order number
            order_number = str(random.randint(100000, 999999))

            # Save the order details in the database
            order_data = {
                "order_number": order_number,
                "first_name": first_name,
                "last_name": last_name,
                "mobile_number": phone_number,
                "items": items,
                "quantity": quantity,
                "capacity": capacity,
                "order_status": "Pending",
                "order_date": datetime.datetime.now().strftime("%Y-%m-%d"),
            }
            try:
                orders_collection.insert_one(order_data)
            except Exception as e:
                print(f"Database Error: {e}")
                return {"fulfillmentText": "An error occurred while saving your order. Please try again."}

            # Format the response
            response_text = (
                f"Thank you for your order! Here are your details:\n\n"
                f"**Order Number**: {order_number}\n"
                f"**First Name**: {first_name}\n"
                f"**Last Name**: {last_name}\n"
                f"**Mobile Number**: {phone_number}\n"
                f"**Items**: {', '.join(items)}\n"
                f"**Quantity**: {quantity}\n"
                f"**Capacity**: {capacity}\n"
                f"**Order Status**: Pending\n"
                f"**Order Date**: {order_data['order_date']}\n\n"
                f"Your order has been successfully placed!"
            )

            return {"fulfillmentText": response_text}

        # Handle the "cancel.order.confirm" intent
        elif intent == "cancel.order.confirm":
            # Retrieve the order number from the context
            contexts = payload["queryResult"].get("outputContexts", [])
            order_number = None
            last_name = None
            for context in contexts:
                if "order_context" in context["name"]:
                    order_number = context["parameters"].get("order_number")
                    last_name = context["parameters"].get("last_name")
                    break

            if not order_number or not last_name:
                return {"fulfillmentText": "Please provide your order number and last name for verification."}

            # Check if the order exists and validate the last name
            order = orders_collection.find_one({"order_number": order_number, "last_name": last_name})
            if order:
                # Update the order status to "Canceled"
                result = orders_collection.update_one(
                    {"order_number": order_number}, {"$set": {"order_status": "Canceled"}}
                )
                if result.modified_count > 0:
                    response_text = (
                        f"Order {order_number} has been successfully canceled. "
                        f"Customer Name: {order['first_name']} {order['last_name']} "
                        f"Items: {', '.join(order['items'])} "
                        f"Capacity: {order['capacity']} "
                        f"Order Date: {order['order_date']}"
                    )
                else:
                    response_text = f"Failed to cancel order {order_number}. Please try again."
            else:
                response_text = "Sorry, I couldn't find any order with that number and last name."

        else:
            response_text = f"Sorry, I can't handle the intent '{intent}' right now."

    except Exception as e:
        print(f"Error: {e}")  # Log the error for debugging
        response_text = "An error occurred while processing your request. Please try again."

    return {"fulfillmentText": response_text}

# GET route to fetch an order by order number
@router.get("/orders/{order_number}")
async def get_order(order_number: str):
    order = orders_collection.find_one({"order_number": order_number})
    if order:
        order_details = serialize_order(order)
        return {
            "order_number": order_details["order_number"],
            "customer_name": order_details["customer_name"],
            "product_name": order_details["product_name"],
            "status": order_details["status"],
            "order_date": order_details["order_date"],
        }
    else:
        raise HTTPException(status_code=404, detail="Order not found")

# PUT route to update an order by order number
@router.put("/orders/{order_number}")
async def update_order(order_number: str, updated_data: dict):
    result = orders_collection.update_one(
        {"order_number": order_number}, {"$set": updated_data}
    )
    if result.modified_count > 0:
        return {"message": "Order updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Order not found or no changes made")

# DELETE route to delete an order by order number
@router.delete("/orders/{order_number}")
async def delete_order(order_number: str):
    result = orders_collection.delete_one({"order_number": order_number})
    if result.deleted_count > 0:
        return {"message": "Order deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Order not found")