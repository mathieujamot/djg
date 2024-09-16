class WindFarm:
    def __init__(self, capacity_mw, wind_speed):
        self.capacity_mw = capacity_mw
        self.wind_speed = wind_speed

    def production(self, hours):
        """Calculate energy production in MWh for a given number of hours."""
        # Improved model: production is proportional to the cube of wind speed
        # and limited by the capacity of the wind farm
        wind_speed_factor = (self.wind_speed / 10) ** 3
        return min(self.capacity_mw * wind_speed_factor * hours, self.capacity_mw * hours)
