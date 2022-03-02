from Yektanet.tasks import add

r = add(5, 5)
print(r)
r = add.delay(5, 5)
print(r.get())
