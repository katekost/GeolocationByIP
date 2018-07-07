import geoip2.database
import pandas as pd

reader = geoip2.database.Reader("D:\ML\GeoLite2-Country.mmdb")
response = reader.country('5.254.65.97')
print(response.country.name)

data = pd.read_csv('uniq_ip_no_err.csv')

def country_detect(x):
    responce = reader.country(x)
    return responce.country.name

d = data.applymap(country_detect)
unique_ip_country = pd.concat([data, d], axis=1)
unique_ip_country.to_csv("unique_ip_country.csv")
