import random

# Step 1: Define population parameters
population_size = 100  # Number of individuals
num_loci = 10          # Number of genetic loci (genes)
num_alleles = 2        # Number of alleles at each locus

# Step 2: Simulate genetic variation
population = []  # List to hold genotypes of all individuals

for i in range(population_size):
    # Simulate a genotype for each individual
    genotype = [random.choice([0, 1]) for _ in range(num_loci)]
    population.append(genotype)

# Step 3: Display the genetic variation for the first 5 individuals
print("Simulated Genetic Data for First 5 Individuals:")
for i in range(5):  # Display the first 5 individuals
    print(f"Individual {i+1}: {population[i]}")

# Step 4: Calculate basic allele frequencies
allele_frequencies = []
for locus in range(num_loci):
    alleles_at_locus = [ind[locus] for ind in population]
    freq = sum(alleles_at_locus) / len(alleles_at_locus)
    allele_frequencies.append(freq)

print("\nAllele Frequencies at Each Locus:")
for i, freq in enumerate(allele_frequencies):
    print(f"Locus {i+1}: Frequency of allele '1' = {freq:.2f}")
