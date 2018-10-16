def city_country(city,country):
    pt=str(city)+','+str(country)
    return pt.title()
ct=input('city:')
cty=input('country:')
ptt=city_country(ct,cty)
print(ptt)

