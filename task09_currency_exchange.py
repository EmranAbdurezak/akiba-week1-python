usd_amount=float(input("Enter the amount(USD): "))
exchange_rate=150
choice=input("Do you want to use the default exchange rate? (yes/no): ")
if choice.lower()=="no":
    exchange_rate=float(input("Enter new exchange rate: "))
etb_amount =exchange_rate*usd_amount
print("===============================================")
print("             CURRENCY EXCHANGE") 
print("===============================================") 
print(f"\nUSD Amount: {usd_amount}")
print(f"Exchange Rate: 1 USD = {exchange_rate} ETB")
print(f"\nETB Amount: {etb_amount:,.1f} ETB")
print("===============================================")
