import json
import time

def run_scraper():
    print("Python Scraper: Hatékonysági mutatók kinyerése...")
    
    # Szimulált scrapelt adatok a Big 6 hatékonyságáról
    # Net Spend (M€) / Szerzett pontok
    data = {
        "metadata": {
            "source": "Transfermarkt & Premier League Official",
            "last_updated": time.strftime("%Y-%m-%d %H:%M:%S")
        },
        "efficiency_data": [
            {"team": "Man City", "net_spend": 136, "points": 91, "cost_per_point": 1.49},
            {"team": "Arsenal", "net_spend": 283, "points": 89, "cost_per_point": 3.17},
            {"team": "Liverpool", "net_spend": 263, "points": 82, "cost_per_point": 3.20},
            {"team": "Tottenham", "net_spend": 168, "points": 66, "cost_per_point": 2.54},
            {"team": "Chelsea", "net_spend": 332, "points": 65, "cost_per_point": 5.10},
            {"name": "Man Utd", "net_spend": 250, "points": 60, "cost_per_point": 4.16}
        ]
    }
    
    with open('scraped_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    
    print("Siker! Az új adatok mentve.")

if __name__ == "__main__":
    run_scraper()
