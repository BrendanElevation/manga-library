# Manga Library — Full‑Stack Flask + PostgreSQL Application

A full‑stack web application built as part of my backend development coursework.  
This project demonstrates how to build a dynamic, database‑driven website using **Flask**, **PostgreSQL**, and **SQLAlchemy**, with a clean front‑end powered by HTML, CSS, and JavaScript.

---

## 🚀 Features

### ✔ Full CRUD Functionality
Users can:
- Add manga entries  
- View manga details  
- Submit order forms  
- Store data in a PostgreSQL database  

### ✔ PostgreSQL Database Integration
The app uses:
- SQLAlchemy ORM  
- Relational database tables  
- Secure form handling  
- Server‑side validation  

### ✔ Flask Backend
- Routing  
- Template rendering  
- Form processing  
- Database operations  

### ✔ Front‑End
- Responsive HTML templates  
- Custom CSS  
- JavaScript for interactivity  
- Image assets stored in `/static/img/`

---

## 🛠 Tech Stack

**Backend**
- Python  
- Flask  
- SQLAlchemy  
- PostgreSQL  
- psycopg2  

**Frontend**
- HTML  
- CSS  
- JavaScript  

**Tools**
- Git & GitHub  
- VS Code  
- WSL (Ubuntu)

---

## 📁 Project Structure

manga-library/
│
├── static/
│   ├── img/
│   ├── script.js
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── orderform.html
│
├── project-app-postgres.py
├── requirements.txt
└── .gitignore

---

## ⚙️ Installation & Setup

### 1. Clone the repository
git clone https://github.com/BrendanElevation/manga-library.git
cd manga-library

### 2. Install dependencies  
(Works with or without a virtual environment.)

pip install -r requirements.txt

### 3. Set up environment variables  
Create a `.env` file in the project root:

DATABASE_URL=postgresql://username:password@localhost:5432/your_database_name
SECRET_KEY=your_generated_secret_key

Your `.env` file is already protected by `.gitignore` and will not be uploaded to GitHub.

### 4. Run the application

python3 project-app-postgres.py

---

## 🗄 Database Schema (Example)

Manga

id (Primary Key)
title
author
genre
description
image_url

---

## 📸 Screenshots

_Add screenshots of your homepage, order form, and database-driven pages here._

Example:

/screenshots
homepage.png
orderform.png

---

## 🎯 Purpose of the Project

This project was built to learn and demonstrate:
- Backend development with Flask  
- Connecting Flask to PostgreSQL  
- Using SQLAlchemy ORM  
- Handling forms and user input  
- Building a full-stack application from scratch  

It is now part of my personal developer portfolio.

---

## 📬 Contact

If you'd like to discuss the project or work together:

**Brendan Lewis**  
St. Albert, AB  
GitHub: https://github.com/BrendanElevation
