"""
print(json.dumps(response, indent=4, ensure_ascii=False))

"""
import requests
import json

nasa_url = "https://api.nasa.gov/planetary/apod?start_date=2026-04-01&end_date=2026-04-26&api_key=DEMO_KEY"

response = requests.get(nasa_url).json()

nasa_data = []
# nasa_data = dict()

for obj in response:
    # test = (obj.get('date'), obj.get('title'), obj.get('hdurl'))
    # nasa_data.append(test)



    nasa_data.append({'date': obj['date'], 'title': obj['title'], 'hdurl': obj.get('hdurl')})


print(nasa_data)
# print(json.dumps(response, indent=4, ensure_ascii=False))


