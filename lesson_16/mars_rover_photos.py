import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    photos = data['photos']

    idx = 1
    for photo in photos:
        img_url = photo['img_src']
        img_data = requests.get(img_url).content

        with open(f'mars_photo{idx}.jpg', 'wb') as file:
            file.write(img_data)

        print(f'Завантажено фото: mars_photo{idx}.jpg')
        idx += 1
else:
    print(f'Не вдалося отримати дані з API. Статус: {response.status_code}')
