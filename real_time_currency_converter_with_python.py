# -*- coding: utf-8 -*-
"""Real-time Currency Converter with Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XVL3ui5Q7OjLaRWYQNOAhWPAoQ1lcSBu
"""

!pip install forex_python
from forex_python.converter import CurrencyRates
c = CurrencyRates()
amount = int(input("Enter the amount: "))
from_currency = input("From Currency: "). upper()
to_currency = input("To Currency: ").upper()
print(from_currency, " To ", to_currency, amount)
result = c. convert(from_currency, to_currency, amount)
print(result)

