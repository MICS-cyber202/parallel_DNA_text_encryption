

dna_dict = {'A':'00','T':'01','C':'10','G':'11'}

permutation_table = {
    'AAA': 1, 'AAT': 2, 'AAC': 3, 'AAG': 4, 'ATA': 5, 'ATT': 6, 'ATC': 7, 'ATG': 8, 'ACA': 9, 'ACT': 10,
    'ACC': 11, 'ACG': 12, 'AGA': 13, 'AGT': 14, 'AGC': 15, 'AGG': 16, 'AXX': 17, 'AAX': 18, 'ATX': 19, 'ACX': 20,
    'AGX': 21, 'TAA': 22, 'TAT': 23, 'TAC': 24, 'TAG': 25, 'TTA': 26, 'TTT': 27, 'TTC': 28, 'TTG': 29, 'TCA': 30,
    'TCT': 31, 'TCC': 32, 'TCG': 33, 'TGA': 34, 'TGT': 35, 'TGC': 36, 'TGG': 37, 'TXX': 38, 'TAX': 39, 'TTX': 40,
    'TCX': 41, 'TGX': 42, 'CAA': 43, 'CAT': 44, 'CAC': 45, 'CAG': 46, 'CTA': 47, 'CTT': 48, 'CTC': 49, 'CTG': 50,  
    'CCA': 51, 'CCT': 52, 'CCC': 53, 'CCG': 54, 'CGA': 55, 'CGT': 56, 'CGC': 57, 'CGG': 58, 'CXX': 59, 'CAX': 60, 
    'CTX': 61, 'CCX': 62, 'CGX': 63, 'GAA': 64, 'GAT': 65, 'GAC': 66, 'GAG': 67, 'GTA': 68, 'GTT': 69, 'GTC': 70, 
    'GTG': 71, 'GCA': 72, 'GCT': 73, 'GCC': 74, 'GCG': 75, 'GGA': 76, 'GGT': 77, 'GGC': 78, 'GGG': 79, 'GXX': 80, 
    'GAX': 81, 'GTX': 82, 'GCX': 83, 'GGX': 84
}


substitution_table = {
    '0': '0000', '2': '0001', '4': '0010', '6': '0011', '8': '0100',
    '9': '0101', '7': '0110', '5': '0111', '3': '1000', '1': '1001'
}

# refactor to use native encoding method to improve performance
def convert_to_binary_8dig(n):
    n = str(n)
    zeroes = 0
    for i in range(0,len(n)):
        if n[i]=='0':
            zeroes+=1
            continue
        break
    n = int(n)
    # print(f'Zeroes: {zeroes}')
    binary = bin(n).replace("0b", "")
    diff = 8 - len(binary)
    if diff>0:
        for i in range(0,diff):
            binary = '0'+binary
    # print(binary)
    return binary

# refactor to use compare operator to improve performance
def xor(A,B):
    if A=='0' and B=='0':
        return '0'
    if A=='0' and B=='1':
        return '1'
    if A=='1' and B=='0':
        return '1'
    if A=='1' and B=='1':
        return '0'

# refactor this using a hasmhmap to improve performance
def dna_complement(d):
    if d=='A':
        return 'T'
    if d=='T':
        return 'A'
    if d=='C':
        return 'G'
    if d=='G':
        return 'C'

def ones_complement(bit):
    return '0' if bit=='1' else '1'