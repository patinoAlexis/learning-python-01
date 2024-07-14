

currentMovies = {
    "The Grinch": "11:00am",
    "Rudolph": "1:00pm",
    "Frosty the Snowman": "3:00pm",
    "Christmas Vacation": "5:00pm"
}

print("We're showing the following movies:")
for key in currentMovies:
    print(key)

movie = input("What movie would you like the showtime for?\n")

availableTime = currentMovies.get(movie)

if availableTime:
    print(f"{movie} is playing at {availableTime}")
else:
    print("Requested movie is not playing at the moment.")
