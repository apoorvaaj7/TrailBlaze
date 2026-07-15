# 🏔️ TrailBlaze - Trekking Management System

TrailBlaze is a full-stack web application developed as part of the IIT Madras Modern Application Development II course. It provides a platform for managing trekking events where administrators can manage staff and treks, staff members can oversee assigned treks, and trekkers can discover, book, and manage their trekking adventures.

The project follows a role-based architecture with three user roles:
- Admin
- Staff
- Trekker

---

## Features

### Authentication
- User Registration
- Secure Login using JWT Authentication
- Role-based Authorization
- Password Hashing

### Admin
- Dashboard with statistics
- Create and manage staff members
- Create, update and delete treks
- Assign staff to treks
- View all trekkers
- View all bookings
- Activate/Blacklist trekkers
- Search users and treks

### Staff
- View assigned treks
- Update available slots
- Change trek status
- View trekkers for assigned treks

### Trekker
- Browse available treks
- View trek details
- Book treks
- Cancel bookings
- Simulated trek payment
- View booked treks
- Update personal profile
- Export booking history as CSV

### Additional Features
- Redis caching for dashboard
- Celery background tasks
- Welcome email for newly created staff
- CSV export using Celery
- Responsive Vue.js frontend

---

## Tech Stack

### Frontend
- Vue 3
- Vue Router
- Bootstrap 5
- Axios

### Backend
- Flask
- Flask RESTful
- Flask JWT Extended
- SQLAlchemy
- SQLite

### Background Services
- Celery
- Redis

---

## Database Schema

The application consists of four main entities:

- Users
- Staff Profiles
- Treks
- Bookings

Relationships:
- One User can have one Staff Profile.
- One Staff manages multiple Treks.
- One Trek can have multiple Bookings.
- One Trekker can make multiple Bookings.

---

## Project Structure

```
TrailBlaze/
│
├── backend/
│   ├── controllers/
│   ├── models.py
│   ├── database.py
│   ├── app.py
│   ├── tasks.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── views/
│   │   ├── router/
│   │   └── App.vue
│   └── package.json
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/23f2004758/TrailBlaze.git

cd TrailBlaze
```

---

### Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Flask

```bash
python app.py
```

Backend runs at

```
http://127.0.0.1:5000
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

## Screens Included

- Home Page
- Login
- Registration
- Admin Dashboard
- Manage Staff
- Manage Treks
- Staff Dashboard
- Trekker Dashboard
- Trek Details
- My Bookings
- Profile Page


---

## Author

**Apoorva Jaiswal**

IIT Madras BS Degree Programme

Roll No: **23f2004758**

Email: **23f2004758@ds.study.iitm.ac.in**

---

This project was developed as part of the Modern Application Development II course offered in the BS Degree Programme at IIT Madras.
