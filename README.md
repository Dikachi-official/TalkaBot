
## ⚛️ **Frontend (React) – `README.md`**

```text
# AI Chat App Frontend – React + Tailwind CSS

This is the frontend of a Fullstack AI Chat Application built with React and Tailwind CSS. It provides a sleek and responsive chat interface that communicates with a Django REST API and the GPT-4 model via OpenAI.

## ⚙️ Tech Stack
- React (with Vite)
- Tailwind CSS + Shadcn ui
- Axios
- OpenAI (indirectly via backend)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Dikachi-official/TalkaBot.git
cd frontend


### 2. Install Dependencies

```bash
npm install



### 3. Run the Development Server

```bash
npm run dev


Visit: `http://localhost:5173`

````



## 2. Setup the backend (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```



TalkaBot/
│── backend/        # Django backend (APIs, models, chatbot logic)
│── frontend/       # React + Tailwind CSS + Shadcn ui
│── README.md       # Project documentation



## 🖼️ Features

* Clean chat UI with scrollable message history
* Message input and loading spinner
* Displays AI responses in real time
* Handles API loading states and errors
* Works with any GPT-4 powered backend

## 🧠 How It Works

* The frontend sends user messages to the Django API
* Django relays them to OpenAI GPT-4 and returns the response
* React renders the conversation in a chat-style UI



🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open a PR or submit an issue.

👤 Author

Dikachi Chikezie
 >💼 Backend Developer (Python & Django)
 >🌐 Portfolio
