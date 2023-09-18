def getLength(e):
    return len(e)

countries = ['Thailand', 'USA', 'Singapore']

print(countries[0])

# Insert into countries
countries.append('Malaysia')
countries.insert(0, 'Lao')

# Remove from countries
del countries[0]
countries.remove('Malaysia')

for country in countries:
    print(country)

print(countries[::-1])
countries.reverse()
countries.sort(reverse=True)
countries.sort(key=len)
pass

# for i in range(len(countries)):
#     print(countries[i])
