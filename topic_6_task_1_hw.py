
def total_salary(path):
    salary_total = 0
    person_count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    _, salary_str = line.split(',')
                    salary = int(salary_str)

                    salary_total += salary
                    person_count += 1
                except ValueError:
                    print(f"Помилка формату даних.")
                    continue

    except FileNotFoundError:
        print(f"Помилка: файл не знайдено.")
        return 0, 0

    if person_count == 0:
        return 0, 0

    average_salary = salary_total / person_count

    return salary_total, int(average_salary)



total, average = total_salary("salary_file_demo.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")