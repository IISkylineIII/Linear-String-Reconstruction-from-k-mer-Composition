# Linear-String-Reconstruction-from-k-mer-Composition

# Description
This Python script reconstructs a linear string from a given list of overlapping (k, d)-mers. Each tuple in the input represents a pair of overlapping k-mers, and the algorithm attempts to rebuild the original string by stitching together the overlapping segments. It is a simplified implementation useful for understanding basic concepts in bioinformatics, such as sequence assembly.

The method implemented here assumes that the (k, d)-mers are ordered and form a continuous linear path, which allows reconstruction by concatenating only the last character of each subsequent k-mer.


# Usage
Example

```

def find_linear_string(kmer_composition):
    string = kmer_composition[0][0]

    for i in range(1, len(kmer_composition)):
        string += kmer_composition[i][0][-1]

    return string

# Given (3,1)-mer composition
kmer_composition = [
    ("AAT", "CCA"),
    ("ATG", "CAT"),
    ("ATG", "GAT"),
    ("CAT", "GGA"),
    ("CCA", "GGG"),
    ("GCC", "TGG"),
    ("GGA", "GTT"),
    ("GGG", "TGT"),
    ("TAA", "GCC"),
    ("TGC", "ATG"),
    ("TGG", "ATG")
]

# Find the linear string
result = find_linear_string(kmer_composition)
print(result)

```

Output
AATGGTACAGACG

# Function Description
* find_linear_string(kmer_composition)
Parameters:
A list of tuples, where each tuple contains a pair of overlapping k-mers (strings).

# Returns:
* A reconstructed linear string assembled from the overlapping segments of the input k-mers.

# Applications
* Bioinformatics: Simplified DNA sequence assembly from short reads or k-mer compositions.
* Education: Demonstrating basic graph traversal and string assembly techniques in genomics.
* Data Reconstruction: Useful in understanding string assembly in error-free environments.

# License
This project is licensed under the MIT License.




