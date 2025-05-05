# 💧 Gaytri-Minral Water Delivery Chatbot

Welcome to the official repository for the **Gaytri-Minral Water Delivery Chatbot** — a smart, interactive chatbot system built to handle water camper and bottle orders, cancellations, and tracking using **Dialogflow**, **FastAPI**, and **MongoDB Atlas**.

---

## 📌 Project Overview

**Objective:** To build an intelligent water delivery ordering assistant that handles:

* New orders (water camper or water bottle)
* Order tracking by 6-digit order ID
* Order cancellation
* Storing user and order data in a real-time backend database

**Tech Stack:**

* **Dialogflow CX** (NLP platform for chatbot development)
* **FastAPI** (Web backend & API for logic handling)
* **MongoDB Atlas** (Cloud-based NoSQL database)
* **Python** (Core backend logic)

---

## 🧠 Key Features

* 💬 Rich chatbot UI using cards, chips, and inputs
* 📦 New order placement with dynamic item/capacity selection
* 🔍 Track orders by 6-digit Order ID
* ❌ Cancel orders by ID
* 📲 Collects user details (first name, last name, phone)
* 🧠 Dialogflow Webhooks connected to FastAPI backend
* 🔄 Real-time data stored in MongoDB Atlas
* 🔧 RESTful API endpoints for tracking, updating, and canceling orders

---

## 📁 Folder Structure

```
├── main.py                           # FastAPI main file
├── config/
│   ├── __pycache__/
│   ├── database.py                   # MongoDB Atlas connection
│   └── setup_database.py             # (Optional) Setup script
├── routes/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── code.txt                      # Miscellaneous or reference code
│   ├── index.html                    # Frontend page (if used)
│   └── route.py                      # All API endpoints (track, cancel, store)
├── models/
│   ├── Order_Details_Added.py       # Models for storing order-related info
│   └── orders.py                    # Additional model definitions
├── schema/
│   └── schemas.py                   # Serializers for MongoDB documents
├── env/                              # Python virtual environment folder
│   ├── Scripts/
│   └── Lib/
├── ngrok-v3-stable-windows-amd64/
│   └── ngrok.exe                     # For tunneling localhost to public URL
├── .gitignore
├── README.md                         # This file!
```

---

## 🔗 Dialogflow Setup

1. **Create Intents:**

   * Welcome Intent (buttons for New Order, Track Order, Cancel Order)
   * New Order → Item → Capacity → Quantity → Confirmation
   * Track Order → Enter 6-digit Order ID
   * Cancel Order → Enter Order ID
   * Collect User Info → First name, Last name, Phone

2. **Webhook URL:**

   * Provided by FastAPI server (e.g., [http://127.0.0.1:8000/track\_order](http://127.0.0.1:8000/track_order))

3. **Enable Fulfillment:** In Dialogflow, toggle webhook for each intent that calls backend logic.

---

## 🔌 FastAPI Setup

```bash
# Step 1: Activate virtual env and install dependencies
pip install fastapi pymongo uvicorn python-dotenv

# Step 2: Run the server
uvicorn main:app --reload
```

### 🔥 Example API Endpoint

```bash
POST http://127.0.0.1:8000/track_order
{
  "order_id": "123456"
}
```

---

## 💾 MongoDB Atlas

* Database: `todo_db`
* Collection: `todo_collection`
* Stores each order with fields:

  * product, capacity, quantity
  * first\_name, last\_name, phone
  * order\_id (6-digit)

> Make sure the MongoDB URI is properly formatted and credentials are URL-encoded using `urllib.parse.quote_plus`

---

## 🧪 Testing

* Use Postman or PowerShell `Invoke-RestMethod` to test `/track_order`, `/cancel_order`, and `/store_order`
* All routes return clear success or failure JSON responses

---

## 🚀 Features

* **Order Tracking**: Customers can track their order status by providing their order number and last name.
* **Order Placement**: Customers can place new orders by providing details such as name, phone number, items, quantity, and capacity.
* **Order Cancellation**: Customers can cancel their orders by verifying their order number and last name.
* **CRUD Operations**: RESTful API endpoints for managing orders (GET, PUT, DELETE).

---

## 📬 API Endpoints

### Webhook

* **POST** `/webhook`: Handles Dialogflow webhook requests.

### Order Management

* **GET** `/orders/{order_number}`: Fetch an order by its order number.
* **PUT** `/orders/{order_number}`: Update an order by its order number.
* **DELETE** `/orders/{order_number}`: Delete an order by its order number.

---

## 🎯 Example Dialogflow Intents

1. **track.order\_status**: Verify order status by providing the order number.
2. **Track.order.validation**: Validate the order using the last name.
3. **new\.order.user.phone\_number**: Place a new order by providing user details.
4. **cancel.order.confirm**: Cancel an order by verifying the order number and last name.

---

## 🛠️ Dependencies

* **FastAPI**: High-performance web framework for building APIs.
* **MongoDB**: NoSQL database for storing order details.
* **Uvicorn**: ASGI server for running the FastAPI app.

Install all dependencies using the `requirements.txt` file.

---

## 🧑‍💻 Development

To contribute to this project:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Credits

* Built with ❤️ by the creator of this repository
* Powered by FastAPI, MongoDB & Dialogflow
