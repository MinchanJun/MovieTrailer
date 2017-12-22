import media, fresh_tomatoes


#Movie Class variables
Inception = media.Movie("Inception", "really good movie",
                        "https://www.warnerbros.com/sites/default/files/styles/key_art_270x400/public/inception_keyart.jpg?itok=7jXiglyb", # noqa
                        "https://www.youtube.com/watch?v=YoHD9XEInc0",2.0)

Arrival = media.Movie("Arrival", "Taking place after alien crafts land around the world, an expert linguist is recruited by the military to determine whether they come in peace or are a threat.", # noqa
                        "http://cdn3-www.comingsoon.net/assets/uploads/gallery/arrival/arrivalposter.jpg", # noqa
                        "https://www.youtube.com/watch?v=ZLO4X6UI8OY",2.1)

Passengers = media.Movie("Passengers", "Jennifer Lawrence and Chris Pratt are two passengers onboard a spaceship transporting", # noqa
                        "http://t3.gstatic.com/images?q=tbn:ANd9GcQvqid_rbEby5j_XkVnSdwWgvSTiX9Np1I6iTJPJWYZFCBOPe4w", # noqa
                        "https://www.youtube.com/watch?v=7BWWWQzTpNU",2.2)

Xmen = media.Movie("X-Men Apocalpyse", "As the fate of the Earth hangs in the balance, Raven (Jennifer Lawrence) with the help of Professor X (James McAvoy) must lead a team of young X-Men to stop their greatest nemesis and save mankind from complete destruction", # noqa
                        "http://t1.gstatic.com/images?q=tbn:ANd9GcTZX8DdBopgYG9P-vi0mwFvu9p_zmLho9ZVmVqQnJFlWAZT6-rB", # noqa
                        "https://www.youtube.com/watch?v=COvnHv42T-A",2.5)

War_for_the_planet = media.Movie("War for the Planet of the Apes ", "A nation of genetically evolved apes led by Caesar become embroiled in a battle with an army of humans.", # noqa
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNDNmYTQzMDEtMmY0MS00OTNjLTk4MjItMDZhMzkzOGI3MzA0XkEyXkFqcGdeQXVyNjk5NDA3OTk@._V1_UX182_CR0,0,182,268_AL_.jpg", # noqa
                        "https://www.youtube.com/watch?v=3KWAxBlZKMA",2.3)

Okja = media.Movie("Okja", "Tilda Swinton, Jake Gyllenhaal and Paul Dano star in this drama about a girl who must keep a powerful company from abducting her pal, a gentle beast. Now streaming on Netflix.", # noqa
                        "http://t1.gstatic.com/images?q=tbn:ANd9GcSkeKv-OKoYw_T-ObRdOKEMfdTrQoJa6O4dLiOhca2PyD1ZkC5c", # noqa
                        "https://www.youtube.com/watch?v=AjCebKn4iic",2.1)
#TV Class variable
TrueBlood = media.Tv("TrueBlood", "Tilda Swinton, Jake Gyllenhaal and Paul Dano star in this drama about a girl who must keep a powerful company from abducting her pal, a gentle beast. Now streaming on Netflix.", # noqa
                        "http://www.gstatic.com/tv/thumb/tvbanners/10111497/p10111497_b_v8_aa.jpg", # noqa
                        "hhttps://www.youtube.com/watch?v=hE8wwYzKJOs","HBO")

#Class variables and Tv variables that are used for the fresh_tomatoes
movies = [Inception,Arrival,Passengers,Xmen,War_for_the_planet,Okja]
tvs = [TrueBlood]
fresh_tomatoes.open_videos_page(movies,tvs)
