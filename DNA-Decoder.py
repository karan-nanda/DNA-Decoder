def is_nucleotide(sequence):
   
    valid_string = ["A", "C", "G", "T"]
    for letter in sequence:
        if letter not in valid_string:
            return False
    return True


def complement_strand(sequence):
    

    complement = ""     

    letter_dictionary = {"A": "T", "C": "G", "T": "A", "G": "C"}
    for letter in sequence:
        if letter in letter_dictionary:
            complement += letter_dictionary[letter]
        else:
            return "Sequencing Error"

    return complement


def mRNA(sequence):
   

    mrna = ""

    for letter in sequence:
        if letter == "T":
            mrna += "U"
        else:
            mrna += letter

    return mrna


def chunk_amino_acid(sequence):
    

    list_of_chunks = []

    for i in range(len(sequence)//3):
        list_of_chunks.append(sequence[i*3:i*3+3])

    return list_of_chunks


def amino_acid_chunks(threecharsSeq):

    translator = translator = {"GCA": "A", "GCC": "A", "GCG": "A", "GCU": "A", #Alanine
                  "AGA": "R", "AGG": "R", "CGA": "R", "CGC": "R", "CGG": "R", "CGU": "R", #Arginine
                  "GAC": "D", "GAU": "D", #Aspartic acid
                  "AAC": "N", "AAU": "N", #Asparagine
                  "UGC": "C", "UGU": "C", #Cysteine
                  "GAA": "E", "GAG": "E", #Glutamic Acid
                  "CAA": "Q", "CAG": "Q", #Glutamine
                  "GGA": "G", "GGC": "G", "GGU": "G", "GGG": "G", ##Glycine
                  "CAC": "H", "CAU": "H", #Histidine
                  "AUA": "I", "AUC": "I", "AUU": "I", #Isoleucine
                  "UUA": "L", "UUG": "L", "CUA": "L", "CUC": "L", "CUG": "L", "CUU": "L", #Leucine
                  "AAA": "K", "AAG": "K", #Lysine
                  "AUG": "M", #Methionine
                  "UUC": "F", "UUU": "F", #Phenylalanine
                  "CCA": "P", "CCC": "P", "CCG": "P", "CCU": "P", # Proline
                  "AGC": "S", "AGU": "S", "UCA": "S", "UCC": "S", "UCG": "S", "UCU": "S", #Serine
                  "ACA": "T", "ACC": "T", "ACG": "T", "ACU": "T", #Threonine
                  "UGG": "W", #Tryptophan
                  "UAC": "Y", "UAU": "Y", #Tyrosine
                  "GUA": "V", "GUC": "V", "GUG": "V", "GUU": "V", #Valine
                  "UAA": "*", "UAG": "*", "UGA": "*" #Termination codon
                  }

    if threecharsSeq in translator.keys():
        return translator[threecharsSeq]   
    else:
        return "?"                          


def sequence_gene(sequence):
   

    aaseq = ""                                                
    if is_nucleotide(sequence):                               
        comp_strand = complement_strand(sequence)           
        mrna = mRNA(comp_strand)                            
        amino_acid_list = chunk_amino_acid(mrna)            

        for amino_acid in amino_acid_list:                  
            aaseq = aaseq + amino_acid_chunks(amino_acid)  
    return aaseq                                           


def main():

    sequence = input("Please enter a valid gene sequence to convert to an amino acid: \n")
    print("The input sequence {0} produces the amino acid {1}".format(sequence, sequence_gene(sequence)))


if __name__ == "__main__":
    main()
