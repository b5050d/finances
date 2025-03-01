"""

"""


from matplotlib import pyplot as plt

def compounding(starting_amount, interest_rate, amount_per_mo, years):
    totals = [starting_amount]

    for i in range(years):
        totals.append(totals[-1]*(1+(interest_rate/100)) + (amount_per_mo*12))

    totals = totals[1:]

    assert len(totals) == years
    return totals

starting_amount = 200000
interest_rate = 5
amount_per_mo = 3000
years = 30

ans = compounding(starting_amount, interest_rate, amount_per_mo, years)
print(ans)
plt.plot([i for i in range(years)], ans)
plt.grid()
plt.xlabel("Years")
plt.ylabel("Money :)")
plt.title("Ben and Teige <3")
plt.show()





