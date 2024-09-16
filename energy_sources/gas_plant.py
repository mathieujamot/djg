class GasPlant:
    def __init__(self, capacity_mw, efficiency):
        self.capacity_mw = capacity_mw
        self.efficiency = efficiency

    def production(self, hours):
        """Calculate energy production in MWh for a given number of hours."""
        return self.capacity_mw * self.efficiency * hours
