import os
import django
import requests
from io import BytesIO
from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # ← змінити
django.setup()

from shop.models import Category, Product

# ---------- Категорії ----------
categories_data = [
    "Електроніка",
    "Одяг",
    "Книги",
    "Спорт",
]

categories = {}
for name in categories_data:
    cat, _ = Category.objects.get_or_create(name=name)
    categories[name] = cat
    print(f"Категорія: {cat.name}")

# ---------- Зображення з placeholder ----------
def get_image(width=400, height=400, color="999"):
    url = f"https://placehold.co/{width}x{height}/{color}/fff/png"
    resp = requests.get(url)
    return ContentFile(resp.content)

# ---------- Товари ----------
products_data = [
    {"title": "Навушники Sony WH-1000XM5", "content": "Бездротові навушники з шумопоглинанням.", "price": 8999, "category": "Електроніка"},
    {"title": "Смартфон Samsung Galaxy A55", "content": "Смартфон з AMOLED екраном 6.6\".", "price": 14999, "category": "Електроніка"},
    {"title": "Футболка Adidas", "content": "Спортивна футболка з дихаючої тканини.", "price": 799, "category": "Одяг"},
    {"title": "Куртка Nike Windrunner", "content": "Легка вітрозахисна куртка.", "price": 2499, "category": "Одяг"},
    {"title": "Кобзар — Тарас Шевченко", "content": "Класика української літератури.", "price": 299, "category": "Книги"},
    {"title": "Чистий код — Роберт Мартін", "content": "Посібник з розробки програмного забезпечення.", "price": 549, "category": "Книги"},
    {"title": "Гантелі 2х10 кг", "content": "Прогумовані гантелі для домашніх тренувань.", "price": 1199, "category": "Спорт"},
    {"title": "Килимок для йоги", "content": "Нековзний килимок 183x61 см.", "price": 699, "category": "Спорт"},
]

for data in products_data:
    product = Product(
        title=data["title"],
        content=data["content"],
        price=data["price"],
        category=categories[data["category"]],
    )
    img_content = get_image()
    product.image.save(f"{product.title[:20]}.png", img_content, save=False)
    product.save()
    print(f"Товар: {product.title}")

print("\nГотово! Всі дані заповнено.")