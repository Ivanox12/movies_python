import fresh_tomatoes
import media

wall_e = media.Movie("Wall-E",
			"A story of robot that hides a great treasure, for humanity.",
			"https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
			"https://www.youtube.com/watch?v=ZisWjdjs-gM")


rocky = media.Movie("Rocky",
		     "The sotry of Rocky Balboa n uneducated but kind-hearted working class Italian-American boxer working as a debt collector for a loan shark in the slums of Philadelphia",
		     "https://upload.wikimedia.org/wikipedia/en/1/18/Rocky_poster.jpg",
		     "https://www.youtube.com/watch?v=3VUblDwa648")


the_walk = media.Movie("The Walk",
		      "In 1974, high-wire artist Philippe Petit recruits a team of people to help him realize his dream",
		      "https://upload.wikimedia.org/wikipedia/en/5/57/The_Walk_%282015_film%29_poster.jpg",
		      "https://www.youtube.com/watch?v=rBicCZG4vg0")


seven_pounds = media.Movie("Seven Pounds",
			     "Tim Thomas (Will Smith), while carelessly sending a text message while driving, veers across the center line into oncoming traffic and causes a multi-car crash in which seven people die",
			     "https://upload.wikimedia.org/wikipedia/en/2/2d/Seven_Pounds_poster.jpg",
			     "https://www.youtube.com/watch?v=7kpK1fKzoDs")

ratatouille = media.Movie ("Ratatouille",
			   "A rat named Remy dreams of becoming a great French chef despite his family's wishes and the obvious problem of being a rat in a decidedly rodent-phobic profession.",
			   "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
			   "https://www.youtube.com/watch?v=c3sBBRxDAqk")

match_point = media.Movie("Match Point",
				"While on a trip to Paris with his fiancée's family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s every day at midnight",
				"https://upload.wikimedia.org/wikipedia/en/0/0a/MatchPointPoster.jpg",
				"https://www.youtube.com/watch?v=wISRAOb6xm0")
movies = [wall_e, rocky, the_walk, seven_pounds, ratatouille, match_point]
fresh_tomatoes.open_movies_page(movies)
