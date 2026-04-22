import random

class QuantumBrain:
    def __init__(self):
        self.version = "1.0.1"
        self.name = "Acient Sub-Quantum"

    def get_signal(self):
        # Simulasi Neutrino Sinyal
        neutrino_flux = random.random()
        if neutrino_flux > 0.8:
            return random.choice(["BUY", "SELL"])
        return "WAIT"
