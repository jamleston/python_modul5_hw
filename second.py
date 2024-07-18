import re

def generator_numbers(text: str):
    pattern = r'^\s\d$\d\s'
    num = re.search(pattern, text).group()
    return num

def sum_profit(text: str, func: callable):
    pass

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# total_income = sum_profit(text, generator_numbers)
# print(f"Загальний дохід: {total_income}")

a = generator_numbers(text)
print(a)