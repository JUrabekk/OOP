class Transport:
    def move(self):
        pass
class WaterTransport(Transport):
    pass
class AirTransport(Transport):
    pass
class GroundTransport(Transport):
    pass
class SpaceTransport(Transport):
    pass
class Ship(WaterTransport):
    def sail(self):
        pass
class Submarine(WaterTransport):
    def dive(self):
        pass
class Airplane(AirTransport):
    pass
class Helicopter(AirTransport):
    pass
class Balloon(AirTransport):
    pass
class Train(GroundTransport):
    pass
class Car(GroundTransport):
    pass
class Bicycle(GroundTransport):
    pass
class HorseCarriage(GroundTransport):
    pass
class Rocket(SpaceTransport):
    pass
class Spaceship(SpaceTransport):
    pass