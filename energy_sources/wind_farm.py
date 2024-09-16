class WindFarm:
    def __init__(self, capacity_mw, wind_speed):
        self.capacity_mw = capacity_mw
        self.wind_speed = wind_speed

    def production(self, hours):
        """Calculate energy production in MWh for a given number of hours."""
        return self.capacity_mw * hours
