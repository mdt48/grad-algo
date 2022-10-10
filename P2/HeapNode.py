class HeapNode:
    def __init__(self, symbol, frequency, left=None, right=None, huffman_code=''):
        self.symbol = symbol
        self.frequency = frequency
        self.huffman_code = huffman_code

        self.left = left
        self.right = right


    def __lt__(self, other):
        return self.frequency < other.frequency
