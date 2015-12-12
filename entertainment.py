import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story", "Toys come to life", "/home/rajat/Pictures/toystory.jpg"," URL ")
avatar = media.Movie("Avatar", "Marine on an alien planet", "/home/rajat/Pictures/avatar.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")
star_wars = media.Movie("Star Wars", "Good vs Evil!", "/home/rajat/Pictures/starwars.jpg","https://www.youtube.com/watch?v=E2MFaxIHTUQ")
creed = media.Movie("Creed", "Rocky inspires Apollo Creed's son.", "/home/rajat/Pictures/creed-movie-poster.jpg","https://www.youtube.com/watch?v=ITQllJPB6nI")

movies = [toy_story, avatar, star_wars, creed]
fresh_tomatoes.open_movies_page(movies)


