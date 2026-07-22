# 🏸 Paddle API

**Sports Court Booking System (Paddle & Tennis) with Django REST Framework**

---

## ✨ Features

### Court Management
- Define paddle and tennis courts with complete specifications
- Dynamic pricing based on weekdays, weekends, and holidays
- Multi-image upload for each court
- Filter by city, court type, price range, and facilities

### Booking System
- View available time slots for any date
- Online reservation with player selection
- Cancel reservation with automatic slot release
- User booking history

### Authentication & Security
- JWT Token authentication
- User registration and login
- Profile management with avatar and phone number
- Password change with validation
- Custom permissions (Admin, Regular User)
- Request throttling

### Additional Features
- Submit reviews and ratings (1-5) for courts
- Average rating calculation for each court
- Complete Swagger/ReDoc documentation
- Advanced filtering, search, and sorting
- Payment system (in development)

---

## 🛠️ Technologies

| Tool | Version |
|------|---------|
| Python | 3.14 |
| Django | 6.0.7 |
| Django REST Framework | 3.16 |
| Simple JWT | 5.5 |
| drf-spectacular | 0.28 |
| django-filter | 25.1 |
| Pillow | 11.0 |

---

## 📦 Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/iamirrd/paddle-api.git
cd paddle-api

# 2. Create virtual environment
# Linux / Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Database setup
python manage.py makemigrations
python manage.py migrate

# 5. Create admin user
python manage.py createsuperuser

# 6. Run development server
python manage.py runserver
```

### API Access

| URL | Description |
|-----|-------------|
| `http://localhost:8000/admin/` | Admin Panel |
| `http://localhost:8000/api/schema/swagger-ui/` | Swagger Documentation |
| `http://localhost:8000/api/schema/redoc/` | ReDoc Documentation |

---

## 🔧 Development Notes

### Permissions

| Role | Access |
|------|--------|
| **Admin** | Full CRUD on courts, users, and reservations |
| **Regular User** | View courts, create/cancel reservations, manage profile |

### Throttling Limits

| Request Type | Limit |
|--------------|-------|
| Public (GET) | 100 requests per 5 minutes |
| Register/Login | 5 requests per 5 minutes |
| Create/Update | 20 requests per 5 minutes |

### Advanced Filters

```http
# Filter by type, city, and price range
GET /api/courts/?court_type=TENNIS&city=Tehran&min_price=0&max_price=500000

# Search and ordering
GET /api/courts/?search=Azadi&ordering=-base_price_per_hour
```

---

## 👥 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing`)
5. Open a Pull Request

---


## 👤 Developer

**Made with ❤️ by [iamirrd](https://github.com/iamirrd)**

---

## 🔗 Useful Links

- [Full Documentation](#)
- [Report Bug](https://github.com/iamirrd/paddle-api/issues)
- [Request Feature](https://github.com/iamirrd/paddle-api/issues)

---

<div align="center">

⭐ Star this repository if you find it useful! ⭐

</div>
