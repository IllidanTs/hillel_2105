import csv
file1_path = r'D:\Папка по имени папка\Hillel\QA Automation Python\random.csv'
file2_path = r'D:\Папка по имени папка\Hillel\QA Automation Python\random-michaels.csv'
result_file_path = r'D:\Папка по имени папка\Hillel\QA Automation Python\result_tsatsorin.csv'

def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    return data

data1 = read_csv(file1_path)
data2 = read_csv(file2_path)

combined_data = data1 + data2

unique_data = []
seen = set()
for row in combined_data:
    row_tuple = tuple(row)
    if row_tuple not in seen:
        seen.add(row_tuple)
        unique_data.append(row)

with open(result_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(unique_data)

print(f"Файл збережено за шляхом: {result_file_path}")
