class HydroPlant:
    def __init__(self, capacity_mw, water_flow_rate):
        self.capacity_mw = capacity_mw
        self.water_flow_rate = water_flow_rate

    def production(self, hours):
        """Calculate energy production in MWh for a given number of hours."""
        # Simplified model: production is proportional to water flow rate
        return self.capacity_mw * (self.water_flow_rate / 100) * hours
