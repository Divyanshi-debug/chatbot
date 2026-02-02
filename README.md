# 🗨️ Python Chatbot (News & Location)

A simple Python-based chatbot that can:
- Respond to greetings
- Tell the current date and time
- Open websites
- Perform basic calculations
- Fetch user location (city & country)
- Show latest India-related news using NewsAPI

This project is built for learning purposes and runs entirely in the terminal.

---

## 🚀 Features

- 👋 Greeting responses
- 📅 Current date
- ⏰ Current time
- 🌐 Open websites (Google, etc.)
- 🧮 Basic calculator
- 📍 Detect location using IP address
- 📰 Fetch latest India-related news

---

## 🛠️ Technologies Used

- Python 3
- `requests` library
- NewsAPI
- IP-API (for location)

---

## 📂 Project Structure

chat_app/
│── app.py
│── README.md


---

## ▶️ How to Run

1. Make sure Python is installed
2. Install required library:
3. Run the chatbot:

---

## 💬 Example Commands

hi
date
time
open google
calculate 5+10
location
news
bye


---

### Environment Variables

Create a `.env` file in the project root and add:

NEWS_API_KEY=your_api_key_here


## 🔐 API Key Notice

This project uses **NewsAPI**.
For security reasons, do **NOT** expose your real API key in public repositories.

Replace it with:
```python
apiKey = "YOUR_API_KEY"

