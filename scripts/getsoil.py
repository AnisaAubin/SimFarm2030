# Python 3
import requests
from pprint import pprint


url = "https://api.agrimetrics.co.uk/graphql"

payload = {"query":("query getFieldIdsNearLocation { fields(geoFilter: {location: {"
         'type: Point, coordinates: [ -3.7775, 50.2839]}, distance: {LE: 500}})'
         '{ id soil { subSoil { texture { type clayPercentage sandPercentage siltPercentage } } '
         'topSoil { chemicalProperties { pH { unit value } } } } '
         "sownCrop { harvestYear cropType } } } ")}
headers = {
    'Accept': "application/json",
    'Ocp-Apim-Subscription-Key': "inlastpass",
    'Content-Type': "application/json",
    'Accept-Encoding': "gzip, deflate, br",
}

response = requests.post(url, json=payload, headers=headers)

pprint(response.json()['data']['fields'])


