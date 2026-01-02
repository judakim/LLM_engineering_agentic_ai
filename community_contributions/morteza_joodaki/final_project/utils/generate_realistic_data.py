import json
import random

cities = [
    "تهران", "مشهد", "اصفهان", "شیراز", "تبریز",
    "رشت", "یزد", "کیش", "قشم", "اهواز"
]

airlines = ["ایران‌ایر", "ماهان", "آسمان", "قشم‌ایر"]
hotels = ["هتل پارسیان", "هتل هما", "هتل سنتی", "هتل آپارتمان"]
providers = ["علی‌بابا", "جاباما", "اسنپ‌تریپ"]
bus_companies = [
    "رویال سفر", "همسفر", "ایران‌پیما", "سیروسفر"
]
train_types = [
    "۴ ستاره", "۳ ستاره", "سالنی", "لوکس"
]
eco_types = [
    "اقامتگاه بوم‌گردی",
    "کلبه سنتی",
    "خانه روستایی",
    "مهمانسرای محلی"
]

def generate_motels_eco():
    data = []
    for i in range(1, 101):
        city = random.choice(cities)
        price = random.randint(600_000, 2_000_000)
        eco = random.choice(eco_types)

        data.append({
            "id": i,
            "type": "eco_lodge",
            "title": f"{eco} در {city}",
            "city": city,
            "price": price,
            "provider": "جاباما",
            "description": (
                f"اقامت در {eco} واقع در {city} با فضای سنتی، "
                f"مناسب گردشگران طبیعت‌گرد با قیمت حدود {price} تومان"
            ),
            "tags": ["بوم‌گردی", "طبیعت"]
        })
    return data

def generate_trains():
    data = []
    for i in range(1, 101):
        frm, to = random.sample(cities, 2)
        price = random.randint(500_000, 2_500_000)
        ttype = random.choice(train_types)

        data.append({
            "id": i,
            "type": "train",
            "title": f"قطار {ttype} از {frm} به {to}",
            "from": frm,
            "to": to,
            "price": price,
            "duration": f"{random.randint(6, 14)} ساعت",
            "provider": "راه‌آهن جمهوری اسلامی",
            "description": (
                f"قطار {ttype} مسیر {frm} به {to} "
                f"مناسب سفر راحت و اقتصادی با قیمت حدود {price} تومان"
            ),
            "tags": ["قطار", "اقتصادی"]
        })
    return data

def generate_buses():
    data = []
    for i in range(1, 101):
        frm, to = random.sample(cities, 2)
        price = random.randint(300_000, 1_200_000)
        company = random.choice(bus_companies)

        data.append({
            "id": i,
            "type": "bus",
            "title": f"اتوبوس {company} از {frm} به {to}",
            "from": frm,
            "to": to,
            "price": price,
            "duration": f"{random.randint(4, 10)} ساعت",
            "provider": "پایانه مسافربری",
            "description": (
                f"سفر زمینی با اتوبوس {company} از {frm} به {to} "
                f"با صندلی راحت و توقف بین راهی، قیمت حدود {price} تومان"
            ),
            "tags": ["اتوبوس", "سفر زمینی"]
        })
    return data

def generate_flights():
    data = []
    for i in range(1, 101):
        frm, to = random.sample(cities, 2)
        price = random.randint(2_000_000, 6_000_000)
        airline = random.choice(airlines)

        data.append({
            "id": i,
            "type": "flight",
            "title": f"پرواز {airline} از {frm} به {to}",
            "from": frm,
            "to": to,
            "price": price,
            "duration": f"{random.randint(1, 2)} ساعت",
            "provider": random.choice(providers),
            "description": f"پرواز مستقیم {airline} از شهر {frm} به {to} با خدمات استاندارد و قیمت حدود {price} تومان",
            "tags": ["پرواز", "داخلی"]
        })
    return data


def generate_hotels():
    data = []
    for i in range(1, 101):
        city = random.choice(cities)
        price = random.randint(1_200_000, 4_000_000)

        data.append({
            "id": i,
            "type": "hotel",
            "title": f"{random.choice(hotels)} در {city}",
            "city": city,
            "price": price,
            "provider": random.choice(providers),
            "description": f"اقامت در {city} با امکانات رفاهی مناسب، دسترسی خوب به مرکز شهر و قیمت حدود {price} تومان برای هر شب",
            "tags": ["هتل", "اقامت"]
        })
    return data


def generate_weather():
    data = []
    for i, city in enumerate(cities, 1):
        data.append({
            "id": i,
            "type": "weather",
            "city": city,
            "temperature": random.randint(5, 40),
            "condition": random.choice(["آفتابی", "ابری", "بارانی"]),
            "description": f"وضعیت آب‌وهوای شهر {city} امروز {random.choice(['مناسب', 'نسبتاً گرم', 'خنک'])} است",
            "tags": ["آب‌وهوا"]
        })
    return data


def save(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


save("data/flights.json", generate_flights())
save("data/hotels.json", generate_hotels())
save("data/weather.json", generate_weather())
save("data/buses.json", generate_buses())
save("data/motels_eco.json", generate_motels_eco())
save("data/trains.json", generate_trains())