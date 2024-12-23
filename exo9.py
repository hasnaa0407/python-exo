cities_population = []

city_name = input("Enter the name of a city (or type 'stop' to finish): ")
while city_name.lower() != 'stop':

    population = len(city_name) * 1000000
    cities_population.append((city_name, population))
    city_name = input("Enter the name of a city (or type 'stop' to finish): ")


cities_population.sort(key=lambda x: x[1], reverse=True)

print("\nCities sorted by population (largest to smallest):")
for city, population in cities_population:
    print(f"{city}: {population:,} citizens")
