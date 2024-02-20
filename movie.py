import sys
import time
import json

with open('names.json', 'r') as names_file:
    hodnoceni_uzivatelu = json.load(names_file)

with open('films.json', 'r') as films_file:
    filmy = json.load(films_file)

with open('reviews.json', 'r') as reviews_file:
    reviews = json.load(reviews_file)

oddelovac = "=" * 62
sluzby = ("dostupne filmy", "detaily filmu", "doporuc film", "recenze")

nickname = input("ZADEJ JMENO:")
time.sleep(1)

if not nickname in hodnoceni_uzivatelu:
    print("neregistrovany uzivatel!")
    sys.exit()
    
else:
    print("V PORADKU")
    time.sleep(1)
    print("\n", oddelovac, "\n")
    print(("VITEJTE V NASEM FILMOVEM SLOVNIKU ").center(60),"\n"*2,oddelovac, "\n")
    print(("dostupne filmy | detaily filmu | doporuc film | recenze ").center(60),"\n")
    print(oddelovac)
time.sleep(1)    

choice = input("Vyber sluzbu:")
time.sleep(1)

if choice in sluzby and choice == "dostupne filmy":
    print("DOSTUPNE FILMY:", ', '.join(tuple(filmy.keys())), "\n",oddelovac)

elif choice in sluzby and choice == "detaily filmu":
    print("Detaily filmu:", ', '.join(tuple(filmy.keys())), "\n")
    film = input("Vyber film:").lower()

    if film in filmy:
        print(oddelovac)
        details = filmy[film]

        for key, value in details.items():
            if key == "HRAJI":
                print(f"{key}: {', '.join(value)}")
            else:
                print(f"{key}: {value}")

        print("\n" + oddelovac)
    else:
        print("Zvoleny film neni v nasem slovniku.")
        sys.exit()  

elif choice in sluzby and choice == "doporuc film":

    movie_counts = {}
    for user_ratings in hodnoceni_uzivatelu.values():
        for movie in user_ratings:
            movie_counts[movie] = movie_counts.get(movie, 0) + 1

    max_count = 0
    recommended_movies = []

    for movie, count in movie_counts.items():
        if count > max_count:
            max_count = count
            recommended_movies = [movie]
        elif count == max_count:
            recommended_movies.append(movie)

    if recommended_movies:
        print("Nejvice doporucovane filmy:")
        for movie in recommended_movies:
            print(f"- {movie}")
    else:
        print("Zadne filmy nebyly doporuceny.")
        sys.exit()

elif choice in sluzby and choice == "recenze":
    print("DOSTUPNE FILMY:", ', '.join(tuple(filmy.keys())))
    chosen_film = input("Vyber film z dostupnych filmu: ").lower()

    if chosen_film in reviews:
        print(f"\nRecenze pro film '{chosen_film}':")
        for user, review in reviews[chosen_film].items():
            print(f"  - {user}: {review}")
        print(oddelovac)
    else:
        print("Recenze pro vybrany film nejsou k dispozici.")
        sys.exit()

else:
    print("vybrana sluzba neni v nabidce")
    sys.exit()