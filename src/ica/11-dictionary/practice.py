# creating and editing dictionaries income, years, and years2

income = {}
years = {"Sylvia": 1978, "Thomas": 2000, "Susan": 1968}
years2 = years.copy()
years2["Henry"] = 2004
del years2["Susan"]

print(years.get("Susan"))
print(years2.get("Henry"))
print(years2.get("Susan"))