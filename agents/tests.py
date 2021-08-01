import pgeocode
from django.test import TestCase


data = pgeocode.Nominatim('US')
print(data.query_postal_code("02108"))





























'''data = pgeocode.GeoDistance('fr')
print(data.query_postal_code(["75013"], ["69006"]))'''
