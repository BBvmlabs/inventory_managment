# 🛒 **Inventory Management System**

This is a simple **Flask**-based project for managing categories in an inventory system. You can **add, update, and delete** categories using a CRUD interface. The project uses **SQLite** as the database and has a simple web-based UI.

---

## **Technologies Used**
- **Flask**
- **SQLAlchemy**

---

## **Installation Instructions**

1. **Clone the Repo**
```
git clone https://github.com/yourusername/inventory-management.git
```

2. **Navigate into the project folder**
```
cd inventory-management
```

3. **Create a Virtual Environment**
```
python -m venv venv
```

4. **Activate the Environment**
- On Windows:
```
venv\Scripts\activate
```
- On Linux/Mac:
```
source venv/bin/activate
```

5. **Install Dependencies**
```
pip install -r requirements.txt
```

---

## **How to Run the App**

1. **Make sure you have activated the environment.**
2. **Run the Flask server**
```
python main.py
```
3. Open your browser and visit:
```
http://127.0.0.1:5000
```

---

## **Features**

- Add new categories
- Update existing categories
- Delete categories
- Avoid duplicate names with validation
- Persistent data storage using SQLite

---
