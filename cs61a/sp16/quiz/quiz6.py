def red(orange, yellow, green):
    def blue():
        if 1 > 2:
            nonlocal orange # this does get executed
        else:
            nonlocal yellow # so does this!
        
        orange, yellow = orange + yellow * 3, orange * 4
        green = lambda indigo: int(orange ** 0.5)
        
        if yellow < orange:
            green = lambda violet: int(orange ** 2)
        
        return green(orange)
    return blue

gatsby = red(3, 2, 1)()
