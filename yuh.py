import requests, json

url = "https://vision.googleapis.com/v1/images:annotate?key=AIzaSyB56eOzBjuyDxgTaAhYxyc2eVgmXqYqoKI"
image_url = "https://i.imgur.com/22SfkjT.jpg"
body = {'requests': [{'image': {'source': {'imageUri': image_url}},'features': [{'type': 'DOCUMENT_TEXT_DETECTION'}]}]}
headers = {"Content-Type": "application/json",
		   "Authorization": "Bearer $(gcloud auth application-default print-access-token)"}


r = requests.post(url, data=json.dumps(body), headers=headers)

print(r.read())