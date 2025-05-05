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
* 📲 Collects user details (first name, last name, email, phone)
* 🧠 Dialogflow Webhooks connected to FastAPI backend
* 🔄 Real-time data stored in MongoDB Atlas

---

## 📁 Folder Structure

```
├── main.py                   # FastAPI main file
├── config/
│   └── database.py           # MongoDB Atlas setup
├── routes/
│   └── route.py              # All API endpoints (track, cancel, store)
├── models/
│   └── todos.py              # Pydantic model for validation
├── schema/
│   └── schemas.py            # Serializer for MongoDB documents
├── .env                      # (Optional) Secure MongoDB credentials
├── README.md                 # This file!
```

---

## 🔗 Dialogflow Setup

1. **Create Intents:**

   * Welcome Intent (buttons for New Order, Track Order, Cancel Order)
   * New Order → Item → Capacity → Quantity → Confirmation
   * Track Order → Enter 6-digit Order ID
   * Cancel Order → Enter Order ID
   * Collect User Info → First name, Last name, Email, Phone

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
  * first\_name, last\_name, email, phone
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
* Integration with SMS/Email for notifications

---

## 🙌 Credits

* Built with ❤️ by \[DhruvilKumar Patel]
* Guided and structured with FastAPI, MongoDB & Dialogflow

---

## 📄 License

This project is licensed under the MIT License.
