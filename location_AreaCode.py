##If you don't have it already, do "pip install phonenumbers" to download the phonenumbers moudle ##
##for the location feature and change Python Interpreter                                          ##

import phonenumbers
import pycountry 
from phonenumbers.phonenumberutil import region_code_for_number 
from phonenumbers import timezone
from phonenumbers import geocoder, carrier

###Converting the string into a phone format###
phoneNumber = phonenumbers.parse("+91987654321")

###Getting the timezone from the phonenumber###
timeZone = timezone.time_zones_for_number(phoneNumber) 

###Extracting Phonenumbers from text###
text = "Contact us at +919876543210 or + 14691234567"
numbers = phonenumbers.PhoneNumberMatcher(text, "IN")

###Carrier and Region of Phonenumber###
Carrier = carrier.name_for_number(phoneNumber, 'en')
Region = geocoder.description_for_number(phoneNumber, 'en')

###Validation of PhoneNumber
valid = phonenumbers.is_valid_number(phoneNumber)
possible = phonenumbers.is_possible_number(phoneNumber)


#print(phoneNumber)
#print(timeZone)
#for number in numbers:
#    print(number) 
#print(Carrier)
#print(Region)
print(valid)
print(possible)
