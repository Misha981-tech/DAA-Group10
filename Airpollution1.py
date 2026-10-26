# AIR POLUTION AND WEATHER DATA ANALYSIS USING ARRAY
#Monthly data
months = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
]
#PM2.5 values in ug/m3
pm25 = [23, 31, 34, 42, 40, 42, 27, 23, 27, 26, 23, 31]

#Temperature values in Fahrenheit
temperature = [40, 43, 48, 53, 64, 68, 75, 48, 60, 53, 40]

#humidity values in percentage
humidity = [26, 25, 29, 38, 42, 38, 34, 42, 38, 32, 31, 26]

#PART 1:HIGHEST PM2.5 CONCENTRATION

highest_pm25 = max(pm25)#get the maximum value in the pm25 list
highest_pm25_index = pm25.index(highest_pm25)

print("1. Month with the highest PM2.5 concentration:")
print(months[highest_pm25_index],"-", highest_pm25, "ug/m3")

#PART 2: AVERAGE PM2.5

average_pm25 = sum(pm25) / len(pm25)#calculate the average of the pm25 list
print("\n2. Average PM2.5 concentration:")
print(round(average_pm25, 2), "ug/m3")

#PART 3: HIGHEST HUMIDITY
highest_humidity = max(humidity)
highest_humidity_index = humidity.index(highest_humidity)

print("\n3. Month with the highest humidity:")
print(months[highest_humidity_index], "-", highest_humidity, "%")

#PART 4: AVERAGE TEMPERATURE
average_temperature = sum(temperature) / len(temperature)
print("\n4. Average temperature:")
print(round(average_temperature, 2), "F")

#PART 5: LOWEST PM2.5
lowest_pm25 = min(pm25)
print("\n5. Month with the lowest PM2.5 concentration:")
for i in range(len(pm25)):
    if pm25[i] == lowest_pm25:
        print(months[i], "-", pm25[i], "ug/m3")
        
#PART 6: MONTHS ABOVE ANNUAL PM2.5 AVERAGE
print("\n6. Months where PM2.5 is above the annual average:")
for i in range(len(pm25)):
    if pm25[i] > average_pm25:
        print(months[i], "-", pm25[i], "ug/m3")
        
#PART7: DICTIONARY
pm25_dictionary = {}
for i in range(len(months)):
    pm25_dictionary[months[i]] = pm25[i]
print("\n7(i) PM2.5 Dictionary:")
print(pm25_dictionary)

user_month = input("\nEnter a month to find its PM2.5 concentration:")
if user_month in pm25_dictionary:
    print(
        user_month,
        "has a PM2.5 concentration of",
        pm25_dictionary[user_month], "ug/m3"
    )
else:
    print("Month not found.")
    
max_pm25_val=max(pm25_dictionary.values())    
highest_pm25_dict = {month:val for month, val in pm25_dictionary.items() if val==max_pm25_val}
print("\n7(iii) Month with the highest PM2.5:")
print(
    highest_pm25_dict
)

dictionary_average = sum(pm25_dictionary.values()) / len(pm25_dictionary)
print("\n7(iv) Average PM2.5:")
print(round(dictionary_average, 2), "ug/m3")

#PART 8
pm25_set = set(pm25)
temperature_set = set(temperature)
humidity_set = set(humidity)

print("\nUNIQUE VALUES")
print("Unique PM2.5 values:")
print(pm25_set)

print("\nUnique temperature values:")
print(temperature_set)

print("\nUnique humidity value:")
print(humidity_set)

number_pm25_unique = len(pm25_set)
number_temperature_unique = len(temperature_set)
number_humidity_unique = len(humidity_set)
print("NUMBER OF UNIQUE VALUES")

print("PM2.5:", number_pm25_unique)
print("Temperature:", number_temperature_unique)
print("Humidity:", number_humidity_unique)

pm25_repeated = len(pm25) - len(pm25_set)
temperature_repeated = len(temperature) - len(temperature_set)
humidity_repeated = len(humidity) - len(humidity_set)
print("REPEATED VALUES")

print("PM2.5 repeated occurrences:", pm25_repeated)
print("Temperature repeated occurrences:", temperature_repeated)
print("Humidity repeated occurrences:", humidity_repeated)

highest_repeated = max(pm25_repeated, temperature_repeated,
humidity_repeated
)
print("\nVariable with the highest number of repeated values:")
if pm25_repeated == highest_repeated:
    print("PM2.5")
if temperature_repeated == highest_repeated:
    print("Temperature")
    
if humidity_repeated == highest_repeated:
    print("Humidity")
    
