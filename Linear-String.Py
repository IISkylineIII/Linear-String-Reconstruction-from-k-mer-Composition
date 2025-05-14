def find_linear_string(kmer_composition):
    string = kmer_composition[0][0]

    for i in range(1, len(kmer_composition)):
        string += kmer_composition[i][0][-1]

    return string

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

result = find_linear_string(kmer_composition)
print(result)
