distance_traveled_km = 150
fuel_consumption_per_100km = 8
co2_factor_g_per_l = 2392

fuel_consumption_per_km = fuel_consumption_per_100km / 100
co2_emissions_g = distance_traveled_km * fuel_consumption_per_km * co2_factor_g_per_l
co2_emissions_kg = co2_emissions_g / 1000
print(co2_emissions_kg)
# Result
# CO2 emissions: 2870.4 kg
