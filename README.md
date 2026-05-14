# 🚀 Store Search Engine

A scalable product search backend built with  
:contentReference[oaicite:0]{index=0}, :contentReference[oaicite:1]{index=1}, and :contentReference[oaicite:2]{index=2}.

This project provides a high-performance search system for e-commerce platforms with support for:

- Full-text search
- Fuzzy matching
- Autocomplete
- Pagination
- Filtering
- Sorting
- Elasticsearch indexing
- REST APIs
- Kibana analytics

---

<p align="center">

<img src="https://img.shields.io/badge/Django-5.x-092E20?style=for-the-badge&logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/DRF-REST%20API-red?style=for-the-badge" />
<img src="https://img.shields.io/badge/Elasticsearch-8.x-005571?style=for-the-badge&logo=elasticsearch" />
<img src="https://img.shields.io/badge/Kibana-Analytics-652D90?style=for-the-badge&logo=kibana" />
<img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python" />

</p>

---

# ✨ Features

## 🔎 Search Engine

- Full-text product search
- Typo-tolerant fuzzy search
- Multi-field search
- Relevance scoring
- High-speed Elasticsearch queries

---

## ⚡ Performance

- Elasticsearch indexing
- Cached API responses
- Optimized pagination
- Scalable architecture
- Supports millions of products

---

## 🛒 Product APIs

- Product listing API
- Search API
- Autocomplete API
- Price filtering
- Sorting support

---

## 📊 Analytics

Integrated with  
:contentReference[oaicite:3]{index=3}  
for search monitoring and analytics.

---

# 🏗️ Tech Stack

| Technology | Purpose |
|---|---|
| Django | Backend framework |
| Django REST Framework | REST APIs |
| Elasticsearch | Search engine |
| Kibana | Analytics dashboard |
| SQLite / PostgreSQL | Database |
| Python | Programming language |

---

# 📁 Project Structure

```bash
store/
│
├── store/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── documents.py
│   ├── urls.py
│   └── autocomplete_views.py
│
├── manage.py
└── requirements.txt
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/your-username/store.git
cd store
```

---

## 2. Create virtual environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔧 Elasticsearch Setup

## Start Elasticsearch

Default URL:

```text
http://localhost:9200
```

---

## Start Kibana

Default URL:

```text
http://localhost:5601
```

---

# 🗄️ Database Migration

```bash
python manage.py migrate
```

---

# 🔍 Elasticsearch Indexing

Create or rebuild the search index:

```bash
python manage.py search_index --rebuild
```

---

# ▶️ Run Development Server

```bash
python manage.py runserver
```

Server:

```text
http://127.0.0.1:8000
```

---

# 📡 API Endpoints

# Product Search

```http
GET /search/?q=iphone
```

Example:

```http
/search/?q=macbook
```

---

# 💡 Autocomplete

```http
GET /autocomplete/?q=iph
```

---

# 💰 Price Filtering

```http
GET /search/?min_price=1000&max_price=5000
```

---

# ↕️ Sorting

## Cheapest

```http
/search/?ordering=cheap
```

## Most Expensive

```http
/search/?ordering=expensive
```

## Newest

```http
/search/?ordering=newest
```

---

# 📄 Pagination

```http
/search/?page=2&size=20
```

---

# 📦 Example Response

```json
{
  "count": 1100103,
  "page": 1,
  "size": 20,
  "results": [
    {
      "id": 1,
      "title": "iPhone 15 Pro",
      "description": "Apple flagship phone",
      "price": 2500,
      "is_active": true,
      "created_at": "2026-05-14T12:00:00Z"
    }
  ]
}
```

---

# 🧠 Elasticsearch Features Used

- Full-text search
- Fuzzy search
- Completion suggester
- Multi-match query
- Range filtering
- Search pagination
- Relevance boosting

---

# 🚀 Scalability

This architecture is designed for:

- Large-scale e-commerce systems
- Millions of products
- High query throughput
- Fast search response times

---

# 📈 Recommended Production Stack

- PostgreSQL
- Redis
- Celery
- Nginx
- Gunicorn
- Docker
- OpenSearch
- Kibana

---

# 🔒 Production Notes

Do not use Django development server in production.

Recommended deployment stack:

```text
Nginx + Gunicorn + PostgreSQL + Elasticsearch
```

---

# 🧪 Performance Tips

- Use SSD/NVMe storage
- Limit pagination size
- Use Elasticsearch filters
- Enable Redis caching
- Separate read/write workloads

---

# 📜 License

MIT License

---

# 👨‍💻 Author

Developed with mohammadrezachizari using Django & Elasticsearch.