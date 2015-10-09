###  Wzorowane na przykÅ‚adzie Rona Zacharskiego
##
##
##from math import sqrt
##
##users = {"Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
##         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
##         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
##         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
##         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
##         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
##         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
##         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
##        }
##
##
##
##def manhattan(rating1, rating2):
##    """Oblicz odlegÅ‚oÅ›Ä‡ w metryce taksÃ³wkowej miÄ™dzy dwoma  zbiorami ocen
##       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
##       ZwrÃ³Ä‡ -1, gdy zbiory nie majÄ… wspÃ³lnych elementÃ³w"""
##       
##    # TODO: wpisz kod
##    pass
##
##
##def computeNearestNeighbor(username, users):
##    """dla danego uÅ¼ytkownika, zwrÃ³Ä‡ listÄ™ innych uÅ¼ytkownikÃ³w wedÅ‚ug bliskoÅ›ci preferencji"""
##    distances = []
##    # TODO: wpisz kod
##    return distances
##
##def recommend(username, users):
##    """ZwrÃ³Ä‡ listÄ™ rekomendacji dla uÅ¼ytkownika"""
##    # znajdÅº preferencje najbliÅ¼szego sÄ…siada
##    nearest = computeNearestNeighbor(username, users)[0][1]
##
##    recommendations = []
##    # zarekomenduj uÅ¼ytkownikowi wykonawcÄ™, ktÃ³rego jeszcze nie oceniÅ‚, a zrobiÅ‚ to jego najbliÅ¼szy sÄ…siada
##    # TODO: wpisz kod
##    # using the fn sorted for variety - sort is more efficient
##    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)
##
### przykÅ‚ady
##
##print( recommend('Hela', users))
###print( recommend('Celina', users))

print ("Nazywam siê Natalia Dymarska. Login github: natalkadym. Piszê pracê magistersk¹ z zakresu Meteorologii GNSS")
print ("Wed³ug mnie chodzi w kodzie o to, by ka¿demu u¿ytkownikowi na podstawie ocen wykonawców, których udzieli³, znaleŸæ listê u¿ytkowników o najlbi¿szych preferencjach; jeœli u¿ytkownik nie oceni³ wykonawcy - na podstawie najbli¿szych preferencji innych u¿ytkowników zostanie mu zarokemendowany.")
