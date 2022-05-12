from datetime import date, timedelta
from pprint import pprint

import requests


def get_rates(currencies, days=30):
    end_date = date.today()
    start_date = end_date - timedelta(days=days)

    symbols = ','.join(currencies)
    requete = f"http://api.exchangerate.host/timeseries?start_date={start_date}&end_date={end_date}&symbols={symbols}"
    req = requests.get(requete)
    if not req and not req.json():
        return False, False
    
    api_rates = req.json().get("rates")
    all_rates = {currency: [] for currency in currencies}

    all_days = api_rates.keys()

    for each_day in all_days:
        [all_rates[currency].append(rate) for currency, rate in api_rates[each_day].items()]

    return all_days, all_rates

if __name__ == '__main__':
    days, rates = get_rates(currencies=["USD", "CAD"])
    pprint(days)
    pprint(rates)