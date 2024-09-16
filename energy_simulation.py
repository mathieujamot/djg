from energy_sources.battery import Battery
from energy_sources.gas_plant import GasPlant
from energy_sources.hydro_plant import HydroPlant
from energy_sources.nuclear_plant import NuclearPlant
from energy_sources.solar_farm import SolarFarm
from energy_sources.wind_farm import WindFarm

class EnergySimulation:
    def __init__(self, energy_sources):
        self.energy_sources = energy_sources

    def simulate(self, hours):
        total_production = 0
        for source in self.energy_sources:
            if hasattr(source, 'production'):
                total_production += source.production(hours)
        return total_production

# Example usage
if __name__ == "__main__":
    sources = [
        NuclearPlant(capacity_mw=1000, efficiency=0.9),
        GasPlant(capacity_mw=500, efficiency=0.8),
        HydroPlant(capacity_mw=300, water_flow_rate=100),
        SolarFarm(capacity_mw=200, sunlight_hours=5),
        WindFarm(capacity_mw=150, wind_speed=10),
        Battery(capacity_mwh=100, charge_efficiency=0.95, discharge_efficiency=0.9)
    ]

    simulation = EnergySimulation(sources)
    total_energy = simulation.simulate(hours=24)
    print(f"Total energy production over 24 hours: {total_energy} MWh")
