def do_Turn(pw):
    if len(pw.my_fleets()) >= 1:
        return
    if len(pw.my_planets()) == 0:
        return
    if len(pw.neutral_planets()) >= 1:
        dest = pw.neutral_planets()[0]
    elif len(pw.enemy_planets()) >= 1:
        dest = pw.enemy_planets()[0]
        source = pw.my_planets()
        num_ships = source.num_ships() / 2
        ow.issue_order(source, dest, num_ships)
             
