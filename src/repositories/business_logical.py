import ast
import json

import requests
from requests_oauthlib import OAuth1
from src.config.settings import Setting
from src.enums.token_fixed import Polygon


def available_companies():
    url = Polygon('available_companies')
    url_auth = f'{url}?apiKey={Setting.polygon_auth}'
    info_companies = requests.get(url_auth)
    companies = []

    utf_string = info_companies.content.decode("UTF-8")
    info_companies = json.loads(info_companies.content)['results']

    if info_companies.status_code == 200:
        for company in info_companies.keys():
            company_tracker = info_companies.get('ticker', False)
            if company_tracker:
                companies.append(company_tracker)
        return companies
    else:
        return "Intente nuevamente"


