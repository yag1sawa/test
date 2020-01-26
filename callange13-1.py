class Horse:
    def __init__(self, rider):
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

rider_i = Rider("yuji")

horse_i = Horse(rider_i)
print(horse_i.rider.name)