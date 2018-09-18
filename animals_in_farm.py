def animal_in_farm(HEADS,LEGS):
    Dog=((1/2)*LEGS)-HEADS
    Chicken=(2*HEADS)-((1/2)*LEGS)
    if Dog<HEADS and Chicken<HEADS:
        return [int(Chicken),int(Dog)]
    else:
        return None
