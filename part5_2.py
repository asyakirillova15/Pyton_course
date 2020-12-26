line_count = 0
with open('5_2.txt', 'r', encoding='utf-8') as new_file:
    for line in new_file:
        line_count += 1
        print(f"Слов с строке {line_count}: {len(line.split())}")

print(f"Количество строк в файле: {line_count}")
