from datetime import date
a=date(2005,2,20)
b=date(2026,4,28)
print("No. of days he lived:",(b-a).days)



from datetime import date
a=date(2005,2,20)
b=date(2026,4,28)
print("No. of days he lived:",(b-a).total_seconds())
