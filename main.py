import sys
from currency_service import CurrencyService


def main():
    if len(sys.argv) != 2:
        print("Usage: py main.py <days>")
        return
    
    try:
        days = int(sys.argv[1])
        if days < 1 or days > 10:
            raise ValueError("Days must be between 1 and 10")
    except ValueError as e:
        print(f"Error: {e}")
        return

    service = CurrencyService()
    rates = service.get_rates_for_last_days(days)
    
    if rates:
        print(rates)


if __name__ == "__main__":
    main()