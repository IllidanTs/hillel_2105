import requests

base_url = 'http://127.0.0.1:8080'

def upload_image(image_path):
    url = f'{base_url}/upload'
    files = {'image': open(image_path, 'rb')}
    response = requests.post(url, files=files)
    if response.status_code == 201:
        print(f'Зображення успішно завантажене: {response.json()["image_url"]}')
        return response.json()["image_url"]
    else:
        print('Помилка завантаження зображення')
        return None

def get_image_url(filename):
    url = f'{base_url}/image/{filename}'
    headers = {'Content-Type': 'text'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f'URL зображення: {response.json()["image_url"]}')
        return response.json()["image_url"]
    else:
        print('Помилка отримання URL зображення')
        return None

def delete_image(filename):
    url = f'{base_url}/delete/{filename}'
    response = requests.delete(url)
    if response.status_code == 200:
        print(f'Зображення успішно видалене: {response.json()["message"]}')
    else:
        print('Помилка видалення зображення')

image_path = r'D:\Папка по имени папка\П\us_ikeCFJpA.jpg'

uploaded_image_url = upload_image(image_path)
if uploaded_image_url:
    filename = uploaded_image_url.split('/')[-1]
    get_image_url(filename)
    delete_image(filename)

