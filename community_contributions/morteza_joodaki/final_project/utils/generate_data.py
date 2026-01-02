import json
import random

def generate(file, kind):
    data = []
    for i in range(1, 101):
        data.append({
            "id": i,
            "description": f"{kind} نمونه شماره {i} برای سفر داخلی",
            "price": random.randint(500000, 5000000)
        })

    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

generate("data/flights.json", "پرواز")
generate("data/trains.json", "قطار")
generate("data/buses.json", "اتوبوس")
generate("data/hotels.json", "هتل")
generate("data/motels_eco.json", "اقامتگاه بوم‌گردی")
generate("data/weather.json", "وضعیت آب‌وهوا")
