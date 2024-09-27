import aiohttp
import asyncio
from datetime import datetime, timedelta


class PrivatBankAPI:
    BASE_URL = 'https://api.privatbank.ua/p24api/exchange_rates?json&date='

    async def fetch_rate(self, session, date_str):
        url = f"{self.BASE_URL}{date_str}"
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Failed to fetch data for {date_str}, status: {response.status}")
        except Exception as e:
            print(f"Error fetching data for {date_str}: {e}")
        return None

    async def fetch_rates(self, days):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(days):
                date = (datetime.now() - timedelta(days=i)).strftime('%d.%m.%Y')
                tasks.append(self.fetch_rate(session, date))
            
            return await asyncio.gather(*tasks)

