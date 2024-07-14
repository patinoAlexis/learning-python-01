
# To create a dictionary you have to declare it as a json file like this:

myAcronims = {
    "LOL": "Laughing out loud",
    "IDK": "I don't know",
    "SMH": "Shaking my head",
}
# You can also create a dictionary empty and add the values later

mySeoncAcronims = {}
mySeoncAcronims["LOL"] = "Laughing out loud"
mySeoncAcronims["IDK"] = "I don't know"
mySeoncAcronims["SMH"] = "Shaking my head"
# You can also update the value just doing the same as above.
mySeoncAcronims["LOL"] = "League of Legends"

# To delete the value
del mySeoncAcronims["LOL"]

# To get values is always better to use the get method to avoid errors
# in the case the value is empty it will return 'None'
print(myAcronims.get("AAA"))
