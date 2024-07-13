import re
from typing import Callable

def generator_numbers(text: str):
    # Регулярний вираз для пошуку дійсних чисел, що відокремлені пробілами
    pattern = r'(?<=\s)(-?\d+\.\d+)(?=\s)'
    matches = re.finditer(pattern, text)
    for match in matches:
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    return sum(func(text))

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 28.45 і 304.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
