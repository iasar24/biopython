from Bio import Phylo

# Read alignment file and create a tree
tree = Phylo.read("example.dnd", "newick")

# Visualize the tree
Phylo.draw(tree)
