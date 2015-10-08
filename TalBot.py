def do_Turn(game):
    planets = game.not_my_planets()
    growth = [p.growth_rate() for p in planets]
    max_planet = planet[growth.index(max(growth))]
