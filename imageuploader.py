import requests, base64




def upload_image(img):
    try:
        encoded_string = ""
        with open("img.jpg", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())


        url = 'https://api.imgur.com/3/image'
        payload = {'image': encoded_string}
        files = {}
        headers = {
          'Authorization': 'Client-ID 143d50448d9154f'
        }
        response = requests.request('POST', url, headers = headers, data = payload, files = files, allow_redirects=False).json()
        img_id = response["data"]["id"]
        img_link = "http://i.imgur.com/" + img_id + ".png"
    except Exception as e:
        print("error: " + str(e))
        return False
