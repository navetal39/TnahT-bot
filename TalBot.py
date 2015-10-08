''' def do_turn(pw):
    if len(pw.my_fleets()) >= 1:
        return
    if len(pw.my_planets()) == 0:
	return
    if len(pw.neutral_planets()) >= 1:
        dest = pw.neutral_planets()[0]
    elif len(pw.enemy_planets()) >= 1:
        dest = pw.enemy_planets()[0]
        source = pw.my_planets()
        num_ships = source.num_ships() / 2
        pw.issue_order(source, dest, num_ships) '''


def do_turn(game):
    planets = game.not_my_planets()
    for source in game.my_planets():
        good_planets = [p for p in planets if will_win(game, p, source)]
        good_planets.sort(key = lambda planet: game.distance(planet, source))
        growth = [p.growth_rate() for p in good_planets]
        if len(growth) == 0:
            return
        max_planet = good_planets[growth.index(max(growth))]
        num_ships = int(0.75 * source.num_ships())
        game.issue_order(source, max_planet, num_ships)



def will_win(game, p, source):
    distance = game.distance(source, p)
    my_rel_fleets = [f.num_ships() for f in game.my_fleets() if f.destination_planet() == p and f.turns_remaining() <= distance]
    enemy_rel_fleets = [f.num_ships() for f in game.enemy_fleets() if f.destination_planet() == p and f.turns_remaining() <= distance]
    my_arr_fleets = sum(my_rel_fleets)
    enemy_arr_fleets = sum(enemy_rel_fleets)
    if p.owner() == 0:
        if p.num_ships() - my_arr_fleets + enemy_arr_fleets < int(0.75 * source.num_ships()):
            return True
    else:
        if p.num_ships() - my_arr_fleets + enemy_arr_fleets + p.growth_rate() * distance < int(0.75 * source.num_ships()):
            return True
    return False

#def will_die(game, source
