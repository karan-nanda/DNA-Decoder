# DNA-Decoder

## Gene Sequence to Amino Acid Converter

### This Python script converts a gene sequence into its corresponding amino acid sequence. It provides the following functionalities:

- is_nucleotide(sequence): Checks if the given sequence consists only of valid nucleotide characters (A, C, G, T). Returns True if all characters are valid nucleotides; otherwise, returns False.

- complement_strand(sequence): Generates the complement strand for a given DNA sequence. Replaces each nucleotide with its complementary base (A with T, C with G, T with A, and G with C). Returns the complement strand sequence. If an invalid nucleotide is encountered, it returns the string "Sequencing Error".

- mRNA(sequence): Converts a DNA sequence into its corresponding mRNA sequence. Replaces each occurrence of T with U (Thymine with Uracil) and leaves other nucleotides unchanged. Returns the mRNA sequence.

- chunk_amino_acid(sequence): Breaks down an input sequence into three-character chunks and stores them in a list. Returns the list of chunks.

- amino_acid_chunks(threecharsSeq): Converts a three-character DNA or mRNA sequence into its corresponding amino acid using a predefined dictionary. Returns the amino acid symbol. If the input sequence is not found in the dictionary, it returns "?".

- sequence_gene(sequence): Takes a gene sequence as input and converts it into an amino acid sequence. It performs the following steps:
    - Checks if the input sequence is a valid nucleotide sequence using the is_nucleotide function.
    - Generates the complement strand using complement_strand.
    - Converts the complement strand into mRNA using mRNA.
    - Breaks down the mRNA sequence into three-character chunks using chunk_amino_acid.
    - Converts each chunk into an amino acid using amino_acid_chunks and concatenates the results to form the final amino acid sequence.
    - Returns the amino acid sequence.
  
- main(): The entry point of the script. It prompts the user to enter a gene sequence and prints the corresponding amino acid sequence.
