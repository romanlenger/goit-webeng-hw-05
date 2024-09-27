import asyncio
from private_api import PrivatBankAPI
from utils import parse_rates


class CurrencyService:
    def __init__(self):
        self.api = PrivatBankAPI()

    def get_rates_for_last_days(self, days):
        loop = asyncio.get_event_loop()
        data = loop.run_until_complete(self.api.fetch_rates(days))
        rates = parse_rates(data)
        return rates
