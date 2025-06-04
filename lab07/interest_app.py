from interest import investment_value, years_to_reach_goal
import locale


print(investment_value(start=5000, years=20, interest_rate=0.20, tax_rate=0, deposit=-20))
print(years_to_reach_goal(start=10000, goal=1000000, interest_rate=0.13, tax_rate=0.25, deposit=1000))

locale.setlocale(locale.LC_ALL, 'en_US')
print(locale.currency(3552.99315, grouping=True))
