def flip(pancake):
    if pancake == 'cakepan':
        return 'pancake'
    elif heat != 4:
        return 'cakepan'
    return 'flipped'
        
def cook(pancake, heat, flip):
    if heat // 10:
        return 'burnt'
    heat += 3
    pancake = flip(pancake)
    
    def cook(pancake, heat, flip):
        if heat >= 5:
            return 'done'
        heat += 1
        pancake = flip(pancake)
        return cook(pancake, heat, lambda p: flip(p))
        
    return cook(pancake, heat, lambda p: flip(p) \
            if heat % 2 == 0 else p)
    
pancake, heat = 'batter', 1
cook(pancake, heat, flip)
