import phonenumbers
from test import number
from phonenumbers import geocoder
country=phonenumbers.parse(number,"ch")
print(geocoder.description_for_number(country,"en"))

from phonenumbers import carrier
ser=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(ser,"en"))
