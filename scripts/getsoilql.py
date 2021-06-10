# Python 3
import requests
from pprint import pprint
from simfarm.utils.pandas import extract_cultivar
import json
import pandas as pd

# def getvalue()
# for x in lat long
#     coordinate = x
cult = 'Skyfall'
df = extract_cultivar(cult)
# print(df[['Lat', 'Long']].head(10))

apiresults = []
url = "https://api.agrimetrics.co.uk/graphql"



headers = {
    'Accept': "application/json",
    'Ocp-Apim-Subscription-Key': "inlastpass",
    'Content-Type': "application/json",
    'Accept-Encoding': "gzip, deflate, br",
}


# for _ , row in list(df[['Lat', 'Long']].unique().iterrows()):
for _ , row in df[['Lat', 'Long']].drop_duplicates().iterrows():
    # print(type(row))
    lat = row['Lat']
    lon = row['Long']
    query = f'''
    query getFieldIdsNearLocation {{fields(geoFilter: {{location: {{type: Point, coordinates: [{lon}, {lat}]}}, distance: {{LE: 500}}}})
    {{id soil {{
        subSoil {{
                texture {{ type clayPercentage sandPercentage siltPercentage}}
            }}
        topSoil {{
                chemicalProperties {{ pH {{ unit value }} }}
            }}
        }}    
        sownCrop {{ harvestYear cropType }} 
            }}
        }}
    '''
    response = requests.post(url, json={"query": query}, headers=headers)
    j = response.json()
    j['coords'] = [lon, lat]
    apiresults.append(j)
    

output = {
    'total': len(apiresults),
    'fields': apiresults
}
with open(f'apiresults{cult}.json', 'w') as f:
    json.dump(output, f, indent=2)

pprint(apiresults[0:10])
