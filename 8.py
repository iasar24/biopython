from Bio.PopGen.SimCoal.Controller import SimCoalController

# Simulate population genetics
sim = SimCoalController(simcoal_dir="path/to/simcoal", template_dir="path/to/template")
sim.run_simulation("example.par", "output_folder")

print("Simulation completed.")