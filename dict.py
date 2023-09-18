current_movies = {
    'equalizer 3': '10:00am',
    'john wick 4': '1:00pm',
    'batman': '10:00pm'
}

movie = input("What movie would ypu like the showtime for?\n")
showtime = current_movies.get(movie.lower())

if showtime is None:
    print("movie isn't playing")
else:
    print(f"{movie.upper()} is playing at {showtime}")