# Daily Dairy Shop - E-Commerce Django Project



[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2.7-green)](https://www.djangoproject.com/)


## Project Overview
This is a Django-based e-commerce web application for a **Daily Dairy Shop**. It allows users to browse products, add them to cart/wishlist, and buy them online. Admin can manage products and orders. Images are stored on **Cloudinary**.

**Live Demo:** [Daily Dairy Shop](https://dailydairyshop-3.onrender.com/)

---

## Features
- User authentication (login/signup)
- Product catalog with categories
- Product detail page with image, description, composition
- Cart & Buy Now functionality
- Wishlist
- Order tracking
- Payment integration (bKash, Nagad)
- Admin panel for managing products, orders, and transactions
- Cloudinary integration for media storage

---

## Tech Stack
- Python 3.13.x  
- Django 4.2.7  
- Cloudinary for media storage  
- SQLite (development database)  
- Bootstrap for frontend  

---

## Installation

1. **Clone the repository:**

git clone <https://github.com/Sharatpsd/DailyDairyShop.git>
cd ec
Create virtual environment:


python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux/Mac
Install dependencies:


pip install -r requirements.txt
Configure settings:

Open settings.py and add your Cloudinary credentials:

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': '<your_cloud_name>',
    'API_KEY': '<your_api_key>',
    'API_SECRET': '<your_api_secret>',
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
Apply migrations:


python manage.py makemigrations
python manage.py migrate
Create superuser (admin):

python manage.py createsuperuser
Run the server:


python manage.py runserver
Open in browser:
Go to http://127.0.0.1:8000/

Project Structure

ec/
├── app/                   # Main Django app
│   ├── admin.py           # Admin panel configuration
│   ├── models.py          # Product, Cart, Wishlist, Order, Transaction models
│   ├── views.py           # Views for frontend and cart/wishlist
│   └── templates/app/     # HTML templates
├── ec/                    # Django project folder
│   ├── settings.py        # Project settings (Cloudinary, Media, etc.)
│   └── urls.py            # URL routing
├── media/                 # Local media files (for development)
├── static/                # Static files
├── db.sqlite3             # SQLite database
└── manage.py              # Django management
Notes
Media Files:
In development, local media can be stored in media/. In production, Cloudinary is used.

Template Fix for Images:
Always check if image exists to avoid errors:

html
Copy code
{% if product.image and product.image.url %}
  <img src="{{ product.image.url }}" alt="{{ product.title }}">
{% else %}
  <p>No image available</p>
{% endif %}
Admin Panel Issue:
Make sure list_display fields in admin.py refer to correct model fields:

python
Copy code
list_display = ['id', 'title', 'selling_price', 'discounted_price', 'category']
Future Improvements
Add order email notifications

Add product search and filters

Implement payment callbacks

Improve frontend UI

Author
Sharat Acharja Mugdho
Email:sharatacharjee6@gmail.com
Green University of Bangladesh (GUB)

