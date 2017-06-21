# Import media and fresh_tomatoes
import media
import fresh_tomatoes

# Store movie attributes to movie class

school_of_rock = media.Movie(
    "School of Rock",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
    
avatar = media.Movie(
    "Avatar",
    "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8")
    
midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "http://tinyurl.com/7zebr4h",
    "https://www.youtube.com/watch?v=5nOF93SzX6s")

hunger_games = media.Movie(
    "Hunger Games",
    "http://tinyurl.com/79m8ppm",
    "https://www.youtube.com/watch?v=mfmrPu43DF8")        
    
toystory = media.Movie(
    "Toy Story",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=4KPTXpQehio")

ratatouille = media.Movie(
    "Ratatouille",
    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk")


movies = [school_of_rock, avatar, midnight_in_paris, hunger_games, toystory, ratatouille]


# Call open_movies_page to open trailer page

fresh_tomatoes.open_movies_page(movies)