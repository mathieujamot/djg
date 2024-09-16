class Battery:
    def __init__(self, capacity_mwh, charge_efficiency, discharge_efficiency):
        self.capacity_mwh = capacity_mwh
        self.charge_efficiency = charge_efficiency
        self.discharge_efficiency = discharge_efficiency
        self.current_charge = 0

    def charge(self, energy_mwh):
        """Charge the battery with a given amount of energy in MWh."""
        self.current_charge += energy_mwh * self.charge_efficiency
        if self.current_charge > self.capacity_mwh:
            self.current_charge = self.capacity_mwh

    def discharge(self, energy_mwh):
        """Discharge the battery by a given amount of energy in MWh."""
        if energy_mwh > self.current_charge:
            energy_mwh = self.current_charge
        self.current_charge -= energy_mwh
        return energy_mwh * self.discharge_efficiency
