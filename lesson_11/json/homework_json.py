import json
import os

folder_path = r'D:\Папка по имени папка\Hillel\QA Automation Python'
result_log_path = r'D:\Папка по имени папка\Hillel\QA Automation Python\json_tsatsorin.log'

files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

invalid_files = []

for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json.load(file)
    except json.JSONDecodeError as e:
        invalid_files.append(f"Файл {file_name} не є валідним JSON: {e}\n")

if invalid_files:
    with open(result_log_path, 'w', encoding='utf-8') as log_file:
        log_file.writelines(invalid_files)

print("Перевірка завершена.")
