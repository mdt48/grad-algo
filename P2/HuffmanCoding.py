from heapq import heapify, heappush, heappop
from HeapNode import HeapNode

class HuffmanCodingHeap:
    def __init__(self, symbols, frequncies):
        self.heap = []
        heapify(self.heap)
        self.symbols = symbols
        self.frequencies = frequncies


    def encode(self):
        # push all nodes to heap
        for sym, freq in zip(self.symbols, self.frequencies):
            heappush(self.heap, HeapNode(sym, freq))

        while len(self.heap) > 1:
            l, r = heappop(self.heap), heappop(self.heap)

            l.huffman_code = '0'
            r.huffman_code = '1'

            new_node = HeapNode(l.symbol+ r.symbol, l.frequency + r.frequency, l, r)

            heappush(self.heap, new_node)

    def print_codes(self):
        self.__rec_print_codes(self.heap[0], '')
        
    
    def __rec_print_codes(self, node, val):
        curr_code = val + node.huffman_code

        if node.left is not None:
            left_val = self.__rec_print_codes(node.left, curr_code)
        
        if node.right is not None:
            right_val = self.__rec_print_codes(node.right, curr_code)

        if node.right is None and node.left is None:
            print('{} : {}'.format(node.symbol, curr_code))

