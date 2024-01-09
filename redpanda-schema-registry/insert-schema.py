import requests
import json


schema = {
    "type": "record",
    "name": "BenthosExample",
    "fields": [
      { "name": "ID", "type": "string" },
      { "name": "Name", "type": "string" },
      { "name": "Gooeyness", "type": "double", "default": 0 },
      { "name": "Bouncing", "type": "boolean", "default": True }
    ]
}
base_uri = "http://localhost:8081"

def pretty(text):
  print(json.dumps(text, indent=2))
  
res = requests.post(
    url=f'{base_uri}/subjects/benthos_example/versions',
    data=json.dumps({
      'schema': json.dumps(schema)
    }),
    headers={'Content-Type': 'application/vnd.schemaregistry.v1+json'}).json()
pretty(res)


