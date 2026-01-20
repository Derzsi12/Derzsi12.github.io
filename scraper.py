import json
import time

def run_scraper():
    print("Python Scraper indítása a BI projekthez...")
    # Itt szimuláljuk az Economics Observatory-ról scrapelt adatokat
    data = {
        "metadata": {
            "source": "Economics Observatory & Transfermarkt",
            "last_updated": time.strftime("%Y-%m-%d %H:%M:%S")
        },
        "clubs": [
            {"name": "Man City", "value": 1100, "points": 91, "budget": 25},
            {"name": "Arsenal", "value": 1000, "points": 89, "budget": 20},
            {"name": "Liverpool", "value": 920, "points": 82, "budget": 18},
            {"name": "Chelsea", "value": 850, "points": 65, "budget": 22},
            {"name": "Man Utd", "value": 750, "points": 60, "budget": 15},
            {"name": "Spurs", "value": 680, "points": 66, "budget": 12}
        ]
    }
    
    with open('scraped_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    
    print("Siker! Az adatok mentve a 'scraped_data.json' fájlba.")

if __name__ == "__main__":
    run_scraper()
