import re
from typing import Callable

def generator_numbers(text: str):
    pattern =  r" \d+.\d+ "
    nums = re.findall(pattern, text)
    for num in nums:
        num = float(num.strip())
        yield num

def sum_profit(text: str, func: Callable):
    nums = func(text)
    sum = 0
    for num in nums:
        sum = sum+num
    return sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")