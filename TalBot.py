def do_turn(game):
    planets = game.not_my_planets()
    for source in game.my_planets():
        if will_die(game, source):
            good_planets = [p for p in planets if will_win_desp(game, p, source)]
            good_planets.sort(key = lambda planet: game.distance(planet, source))
            growth = [p.growth_rate() for p in good_planets]
            if len(growth) == 0:
                my_planets = game.my_planets()
                my_planets.sort(key = lambda planet: planet.num_ships())
                if len(my_planets) > 0:
                    issue_order(source, my_planets[0], source.num_ships())
            else:
                max_planet = good_planets[growth.index(max(growth))]
                num_ships = source.num_ships()
                game.issue_order(source, max_planet, num_ships)
        else:
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

def will_win_desp(game, p, source):
    distance = game.distance(source, p)
    my_rel_fleets = [f.num_ships() for f in game.my_fleets() if f.destination_planet() == p and f.turns_remaining() <= distance]
    enemy_rel_fleets = [f.num_ships() for f in game.enemy_fleets() if f.destination_planet() == p and f.turns_remaining() <= distance]
    my_arr_fleets = sum(my_rel_fleets)
    enemy_arr_fleets = sum(enemy_rel_fleets)
    if p.owner() == 0:
        if p.num_ships() - my_arr_fleets + enemy_arr_fleets < source.num_ships():
            return True
    else:
        if p.num_ships() - my_arr_fleets + enemy_arr_fleets + p.growth_rate() * distance < source.num_ships():
            return True
    return False

def will_die(game, p):
    my_rel_fleets = [f.num_ships() for f in game.my_fleets() if f.destination_planet() == p and f.turns_remaining() == 1]
    enemy_rel_fleets = [f.num_ships() for f in game.enemy_fleets() if f.destination_planet() == p and f.turns_remaining() == 1]
    my_arr_fleets = sum(my_rel_fleets)
    enemy_arr_fleets = sum(enemy_rel_fleets)
    if enemy_arr_fleets > p.num_ships() + p.growth_rate() + my_arr_fleets:
        return True
    return False
