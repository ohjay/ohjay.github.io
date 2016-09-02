def cook(pancake, time_left):
    def cook():
        if not time_left:
            return "golden-brown pancake"
        if -time_left > 0:
            return "burnt pancake"
        return "still batter" # than cereal

    while time_left > 0:
        time_left -= 2
        pancake = cook()
    return pancake

cook("batter", 3)
