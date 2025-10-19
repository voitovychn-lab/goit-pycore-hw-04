def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    cat_id, name, age = line.split(',')

                    cat_dict = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats_info.append(cat_dict)

                except ValueError:
                    print(f"Помилка формату даних.")
                    continue

    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено.")
        return []

    return cats_info


cats_info = get_cats_info("cats_file_demo.txt")
print(cats_info)