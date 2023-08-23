# Exchange rates to USD
colombian_peso = 0.00025
peruvian_sol = 0.27
brazilian_real = 0.21


# Ask user for left over non-usd currency
users_peso = float(input('How many pesos do you have left? '))
users_sol = float(input('How many sols do you have left? '))
users_real = float(input('How many reals do you have left? '))

# Calculate left over non-usd to usd
calc_peso = users_peso * colombian_peso
calc_sol = users_sol * peruvian_sol
calc_real = users_real * brazilian_real

# Calculate total in usd
total = calc_peso + calc_sol + calc_real

# Print total
print(total)
