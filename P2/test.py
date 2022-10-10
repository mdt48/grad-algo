from HuffmanCoding import HuffmanCoding


def main():
    chars = ['a', 'b', 'c', 'd', 'e', 'f']
 
    freq = [ 5, 9, 12, 13, 16, 45]


    huff = HuffmanCoding(chars, freq)
    huff.encode()
    huff.print_codes()


if __name__ == '__main__':
    main()