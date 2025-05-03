class car():
    def __init__ (self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, vel):
        if vel < 0:
            self._velocity = 0
        elif vel > 200:
            self._velocity = 200
        else:
            self._velocity = vel

    @property
    def fuelRate(self):
        return self._fuelRate

    @fuelRate.setter
    def fuelRate(self,fuel):
        if fuel < 0:
            self._fuelRate = 0
        elif fuel > 100:
            self._fuelRate = 100
        else:
            self._fuelRate = fuel

    def run (self, vel, dist):
        self.velocity = vel
        if self.fuelRate <= 0:
            self.stop(dist)
            return

        fuel_needed = dist / 10
        if fuel_needed > self.fuelRate:
            dist_traveled = self.fuelRate * 10
            self.fuelRate = 0
            self.stop(dist - dist_traveled)
        else:
            self.fuelRate -= fuel_needed
            self.stop(0)

    def stop(self, remain_dist):
        self.velocity = 0
        if remain_dist > 0:
            print(f"Car stopped. You still have {remain_dist} to arrive")
        else:
            print("You have arrived at your destination")

