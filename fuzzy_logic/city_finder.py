import fuzzywuzzy as fuzz
from fuzzywuzzy import process

cities = ['Chennai', 'Coimbatore', 'Madurai', 'Tiruchirapalli', 'Tiruppur', 'Salem', 'Erode', 'Tirunelveli', 'Karur',
          'Theni']


def matching(query, m_list, limit=2):
    result = process.extract(query, m_list, limit=limit)
    return result


print(matching('Trichy', cities))
