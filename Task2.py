# Завдання 2

# Реалізувати двійковий пошук для відсортованого масиву з дробовими числами.
# Написана функція для двійкового пошуку повинна повертати кортеж,
# де першим елементом є кількість ітерацій, потрібних для знаходження елемента.
# Другим елементом має бути "верхня межа" — це найменший елемент,
# який є більшим або рівним заданому значенню.

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    i = 1
    current_top_limit = max(arr)
    while low <= high:
 
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
            if arr[mid] < current_top_limit:
                current_top_limit = arr[mid]
 
        # інакше x присутній на позиції і повертаємо його
        else:
            return (i, arr[mid])
        
        i += 1
    # якщо елемент не знайдений
    return (i, current_top_limit)

arr = [2.5, 3.9, 4.1, 5.0, 6.8, 7.4, 10.15, 40.6]
x = 7
y = 5
result = binary_search(arr, x)
print(f"For x = {x} found {result}")

result = binary_search(arr, y)
print(f"For y = {y} found {result}")