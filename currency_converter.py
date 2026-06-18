f = open("CurrencyData.txt")
lines = f.readlines()

currencydict = {}
for line in lines:
    a = line.split("\t")
    currencydict[a[0]] = a[1]

# print(currencydict)

print("\n" + "=" * 55)
print("         💱 INDIAN RUPEE CURRENCY CONVERTER 💱")
print("=" * 55)

amount = int(input("\n💰 Enter the amount in INR: "))

print("\n🌍 Available currencies:")
print("-" * 55)

[print(f"➜ {item}") for item in currencydict.keys()]

print("-" * 55)
currency = input("\n🔹 Enter the currency name: ")

print("\n" + "=" * 55)
print(f"✅ Conversion Result:\n\n")
print(f"₹{amount} INR = {amount * float(currencydict[currency])} {currency}")

print("=" * 55)