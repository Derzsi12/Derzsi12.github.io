import json
import time

def run_scraper():
    print("Python Scraper indítása: Big 6 hatékonysági adatok...")
    
    # Szimulált scrapelt adatok a Big 6-ról
    data = {
        "metadata": {
            "source": "Economics Observatory & Transfermarkt",
            "last_updated": time.strftime("%Y-%m-%d %H:%M:%S")
        },
        "efficiency_data": [
            {"team": "Man City", "cost_per_point": 1.49},
            {"team": "Arsenal", "cost_per_point": 3.17},
            {"team": "Liverpool", "cost_per_point": 3.20},
            {"team": "Tottenham", "cost_per_point": 2.54},
            {"team": "Chelsea", "cost_per_point": 5.10},
            {"team": "Man Utd", "cost_per_point": 4.16}
        ]
    }
    
    with open('scraped_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    
    print("Siker! 'scraped_data.json' létrehozva.")

if __name__ == "__main__":
    run_scraper()
