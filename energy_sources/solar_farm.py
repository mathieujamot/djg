class SolarFarm:
    def __init__(self, capacity_mw, sunlight_hours):
        self.capacity_mw = capacity_mw
        self.sunlight_hours = sunlight_hours

    def production(self, hours):
        """Calculate energy production in MWh for a given number of hours."""
        # Assume an efficiency factor for solar panels
        efficiency = 0.2  # Example efficiency factor
        # Improved model: production is limited by the capacity of the solar farm
        return min(self.capacity_mw * efficiency * min(hours, self.sunlight_hours), self.capacity_mw * hours)
