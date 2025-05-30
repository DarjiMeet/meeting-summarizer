#  Meeting Summarizer App

A smart web app that takes in meeting audio/video recordings and outputs a concise summary and action items using OpenAI Whisper and BRAT for summary.

---

## 📸 Screenshot

<img src='image.png'/>

---

##  Project Structure
meeting-summarizer/ <br/>
├── backend/ # Flask backend (transcription & summary) <br/>
├── Frontend/meeting-summarizer/ # React frontend (user interface) <br/>
├── .gitignore <br/>
├── README.md <br/>


---

##  Tech Stack

| Layer       | Technology          |
|-------------|---------------------|
| Frontend    | React + Vite        |
| Backend     | Python + Flask      |
| AI Model    | OpenAI Whisper + BRAT |
| Database    | SQLite (local)      |

---

##  Features

- Upload meeting recordings (audio/video)
- Automatically generate a summary
- Extract actionable items
- Simple UI built with React

---

##  Setup Instructions

###  Prerequisites

- Node.js & npm
- Python 3.9+
- `pip` package manager

---

### Backend Setup (Flask)

cd backend
python -m venv venv
<br/>
#### On Windows:
.\venv\Scripts\activate
#### On Mac/Linux:
source venv/bin/activate
<br/>
pip install -r requirement.txt <br/>
python app.py

### Fronted Setup
cd Frontend/meeting-summarizer<br/>
npm install<br/>
npm run dev<br/>
[Link Text]([https://example.com](https://darling-moxie-2b799f.netlify.app/))
