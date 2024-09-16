class SolarFarm:
    def __init__(self, capacity_mw, sunlight_hours):
        self.capacity_mw = capacity_mw
        self.sunlight_hours = sunlight_hours

    def production(self, hours):
        """Calculate energy production in MWh for a given number of hours."""
        return self.capacity_mw * min(hours, self.sunlight_hours)
