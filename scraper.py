import csv
import json
import time

def process_big6_minileague():
    print("A Big 6 Mini-League adatok kinyerése a fixtures.csv-ből...")
    
    # A pontos csapatnevek a beküldött CSV fájl alapján
    big_6 = [
        "Manchester Utd", 
        "Liverpool", 
        "Arsenal", 
        "Manchester City", 
        "Chelsea", 
        "Tottenham"
    ]
    
    # Kezdőértékek: minden csapat 0 pontról indul
    stats = {team: 0 for team in big_6}
    
    try:
        # Megnyitjuk a feltöltött adatfájlt
        with open('fixtures.csv', mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                home_team = row['Home']
                away_team = row['Away']
                
                # Csak akkor számolunk, ha mindkét csapat a Big 6 tagja
                if home_team in big_6 and away_team in big_6:
                    # Gólok beolvasása (egész számként)
                    h_score = int(row['HomeScore'])
                    a_score = int(row['AwayScore'])
                    
                    if h_score > a_score:
                        # Hazai győzelem: a hazai csapat kap 3 pontot
                        stats[home_team] += 3
                    elif a_score > h_score:
                        # Vendég győzelem: a vendég csapat kap 3 pontot
                        stats[away_team] += 3
                    else:
                        # Döntetlen: mindkét csapat kap 1 pontot
                        stats[home_team] += 1
                        stats[away_team] += 1
        
        # Adatok sorbarendezése pontszám szerint (Data Storytelling szempont)
        sorted_stats = sorted(
            [{"team": t, "points": p} for t, p in stats.items()],
            key=lambda x: x['points'], 
            reverse=True
        )

        # JSON kimenet összeállítása a Dashboard számára
        output = {
            "metadata": {
                "title": "Big 6 Head-to-Head Mini League",
                "source": "fixtures.csv (Direct Analysis)",
                "last_updated": time.strftime("%Y-%m-%d %H:%M:%S")
            },
            "minileague": sorted_stats
        }
        
        # Mentés a weboldal által beolvasható fájlba
        with open('scraped_data.json', 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=4)
            
        print("Siker! A 'scraped_data.json' elkészült a valódi mérkőzésadatok alapján.")

    except FileNotFoundError:
        print("Hiba: Nem találom a 'fixtures.csv' fájlt a mappában!")
    except Exception as e:
        print(f"Váratlan hiba történt: {e}")

if __name__ == "__main__":
    process_big6_minileague()
