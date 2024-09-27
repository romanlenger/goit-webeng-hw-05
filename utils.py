import json
from pathlib import Path

def parse_rates(data):
    result = []
    for day_data in data:
        if day_data and 'exchangeRate' in day_data:
            date = day_data.get('date', 'Unknown Date')
            eur_rate = next((rate for rate in day_data['exchangeRate'] if rate['currency'] == 'EUR'), None)
            usd_rate = next((rate for rate in day_data['exchangeRate'] if rate['currency'] == 'USD'), None)
            if eur_rate and usd_rate:
                result.append({
                    date: {
                        'EUR': {
                            'sale': eur_rate['saleRate'],
                            'purchase': eur_rate['purchaseRate']
                        },
                        'USD': {
                            'sale': usd_rate['saleRate'],
                            'purchase': usd_rate['purchaseRate']
                        }
                    }
                })
    
    # Визначаємо шлях до файлу result.json у поточному каталозі
    current_dir = Path(__file__).parent  # Отримуємо каталог, де знаходиться цей файл
    result_file = current_dir / 'result.json'
    
    # Збереження у файл result.json
    with open(result_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    return result
