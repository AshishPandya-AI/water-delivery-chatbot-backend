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

## 🌱 Future Improvements

* Integrate payment confirmation
* Admin dashboard for managing orders
* Analytics dashboard for business insights
* Integration with SMS for notifications

---

## 🙌 Credits

* Built with ❤️ by the creator of this repository
* Powered by FastAPI, MongoDB & Dialogflow

---

## 📄 License

This project is licensed under the MIT License.
