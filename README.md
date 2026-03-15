<div align="center">

<img src="readmefile/landing_page.png" alt="Daily Dairy Shop Banner" width="100%" style="border-radius: 12px;" />

# 🥛 Daily Dairy Shop

### A Full-Stack E-Commerce Web Application for Fresh Dairy Products

<br/>

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2.7-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Cloudinary](https://img.shields.io/badge/Cloudinary-Image_Storage-3448C5?style=for-the-badge&logo=cloudinary&logoColor=white)](https://cloudinary.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Online-16a34a?style=for-the-badge)](https://dailydairyshop-3.onrender.com/)

<br/>

> **Daily Dairy Shop** is a production-ready, fully functional e-commerce platform built with Django — designed for selling fresh dairy products (milk, curd, ghee, paneer, cheese, ice cream & more) with a beautiful customer-facing storefront and a powerful custom admin dashboard.

<br/>

[🌐 View Live Demo](https://dailydairyshop-3.onrender.com/) &nbsp;·&nbsp;
[🐛 Report Bug](https://github.com/Sharatpsd/DailyDairyShop/issues) &nbsp;·&nbsp;
[✨ Request Feature](https://github.com/Sharatpsd/DailyDairyShop/issues)

</div>

---

## 📌 Table of Contents

- [📸 Screenshots](#-screenshots)
- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📁 Project Structure](#-project-structure)
- [⚙️ Installation & Setup](#️-installation--setup)
- [🌐 Access URLs](#-access-urls)
- [🔮 Future Enhancements](#-future-enhancements)
- [👨‍💻 Author](#-author)

---

## 📸 Screenshots

<br/>

### 🏠 Landing Page
<img src="readmefile/landing_page.png" alt="Landing Page" width="100%" />

> Animated full-screen welcome slider with snow effect, smooth transitions, and a modern hero section.

---

### 🗂️ Product Category
<img src="readmefile/product_category.png" alt="Product Category" width="100%" />

> Browse all dairy products organized by category — beautifully laid out with responsive card components.

---

### 🔍 Product Details
<img src="readmefile/product_details.png" alt="Product Details" width="100%" />

> Detailed product view with high-quality images, descriptions, pricing, and quick Add to Cart / Buy Now actions.

---

### ❤️ Wishlist
<img src="readmefile/wishlist.png" alt="Wishlist" width="100%" />

> Save your favorite products to your personal wishlist for easy access anytime.

---

### 🛒 Add to Cart
<img src="readmefile/add_ to cart.png" alt="Add to Cart" width="100%" />

> Seamless session-based cart with real-time item tracking, quantity control, and order summary.

---

### ℹ️ About Page
<img src="readmefile/about_page.png" alt="About Page" width="100%" />

> A clean, professional About page showcasing the brand story, mission, and team details.

---

## ✨ Features

### 👤 Customer Side
| Feature | Description |
|--------|-------------|
| 🎞️ Animated Slider | Full-screen welcome slider with snow effect & smooth transitions |
| 🗂️ Browse by Category | Filter and explore products by dairy category |
| 🔍 Product Details | Dedicated pages with images, pricing, and stock info |
| 🛒 Cart System | Session-based cart with add/remove/update quantity |
| ❤️ Wishlist | Save and manage favorite products |
| 📱 Responsive Design | Mobile-first, works on all screen sizes |
| 🎨 Modern UI | Beautiful hover effects, card layouts, elegant buttons |

### 🔧 Admin Side
| Feature | Description |
|--------|-------------|
| 📊 Dashboard | Custom admin panel with sales, order, and product analytics |
| 📦 Product Management | Add, edit, delete products with Cloudinary image uploads |
| 🗂️ Category Management | Organize and manage product categories |
| 🧾 Order Management | View and update order status in real time |
| 👥 Customer Overview | Browse registered customers and their activity |
| 💰 Revenue Tracking | Monitor total revenue and product performance |

### ⚙️ Technical
| Feature | Description |
|--------|-------------|
| 🔐 CSRF Protection | Secure form submissions with Django CSRF middleware |
| ☁️ Cloudinary Storage | Cloud-based image hosting and CDN delivery |
| 🧩 Modular Codebase | Clean separation of concerns across apps |
| 📝 Session Management | Persistent cart without requiring login |
| 🗃️ Template Engine | Django's powerful templating for dynamic pages |

---

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| 🐍 Python | 3.13+ | Core Backend Language |
| 🌐 Django | 4.2.7 | Web Framework |
| 🎨 Bootstrap | 5.3 | Responsive Frontend UI |
| ☁️ Cloudinary | Latest | Image Hosting & Management |
| 🗃️ SQLite | Default | Development Database |
| 🖼️ HTML5 / CSS3 | Modern | Templating & Styling |
| ⚡ JavaScript | ES6+ | Interactive UI Enhancements |

---

## 📁 Project Structure

```
DailyDairyShop/
│
├── 📂 adminpanel/                  # Custom Admin Panel App
│   ├── 📂 templates/adminpanel/
│   │   ├── dashboard_home.html
│   │   ├── products.html
│   │   ├── categories.html
│   │   └── ...
│   ├── urls.py
│   ├── views.py
│   └── models.py
│
├── 📂 customer/                    # Customer-Facing App
│   ├── 📂 templates/customer/
│   │   ├── home.html
│   │   ├── product_detail.html
│   │   ├── cart.html
│   │   ├── wishlist.html
│   │   └── ...
│   ├── urls.py
│   ├── views.py
│   └── models.py
│
├── 📂 DailyDairyShop/              # Project Configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── 📂 static/                      # Static Files (CSS, JS, Images)
├── 📂 media/                       # Uploaded Media Files
├── 📂 readmefile/                  # README Screenshots
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.13+
- pip
- Git

---

### Step 1 — Clone the Repository

```bash
git clone https://github.com/Sharatpsd/DailyDairyShop.git
cd DailyDairyShop
```

### Step 2 — Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Configure Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### Step 5 — Run Migrations & Create Superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Step 6 — Start the Development Server

```bash
python manage.py runserver
```

---

## 🌐 Access URLs

| Page | URL |
|------|-----|
| 🏠 Homepage | [http://127.0.0.1:8000](http://127.0.0.1:8000) |
| 🔐 Django Admin | [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) |
| 📊 Custom Admin Panel | [http://127.0.0.1:8000/adminpanel/](http://127.0.0.1:8000/adminpanel/) |
| 🌐 Live Demo | [https://dailydairyshop-3.onrender.com](https://dailydairyshop-3.onrender.com) |

---

## 🔮 Future Enhancements

- [ ] 🔐 User Registration & Login with JWT Authentication
- [ ] 💳 Payment Gateway Integration (bKash, Nagad, SSLCommerz)
- [ ] 📦 Real-time Order Tracking Page
- [ ] 📧 Email & SMS Notifications
- [ ] 🧾 PDF Invoice Generation
- [ ] 🌍 Multi-language Support (Bangla + English)
- [ ] ⭐ Product Ratings & Reviews
- [ ] 📱 Progressive Web App (PWA) Support
- [ ] 📈 Sales Analytics Dashboard with Charts
- [ ] 🔍 Advanced Product Search & Filtering

---

## 👨‍💻 Author

<div align="center">

### Sharat Acharja Mugdho

**Computer Science & Engineering**
Green University of Bangladesh

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-Sharatpsd-181717?style=for-the-badge&logo=github)](https://github.com/Sharatpsd)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit_Site-0ea5e9?style=for-the-badge&logo=google-chrome&logoColor=white)](https://mugdho-portfolio.netlify.app/)
[![Email](https://img.shields.io/badge/Email-sharatacharjee6@gmail.com-ea4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sharatacharjee6@gmail.com)

</div>

---

<div align="center">

**⭐ If you found this project helpful, please give it a star on GitHub! ⭐**

<br/>

*Made with ❤️ by [Sharat Acharja Mugdho](https://mugdho-portfolio.netlify.app/)*

</div>
