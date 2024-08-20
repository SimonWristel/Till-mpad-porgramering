def calculate_monthly_payment(principal, annual_rate, years):
    monthly_rate = annual_rate /100 / 12
    total_payment = years * 12
    montly_payment = (principal * monthly_rate * (1 + monthly_rate) **total_payment) / ((1 + monthly_rate) ** total_payment -1)
    return montly_payment

principal = float(input("Lånebelopp: "))
annual_rate = float(input("Årsränta (%): "))
years = int(input("Löptid (år): "))
payment = calculate_monthly_payment(principal, annual_rate, years)

payment = calculate_monthly_payment(principal, annual_rate, years)

print(f"Din månatliga betalning är: {payment:.2f} kr")
