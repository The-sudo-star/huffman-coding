"""
Huffman Coding - Extra Credit Project
"""
import heapq, pickle, os, sys

class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char, self.freq, self.left, self.right = char, freq, left, right
    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanCoding:
    def __init__(self):
        self.root = None
        self.codes = {}
    
    def build_tree(self, text):
        # Count frequencies
        freq = {}
        for char in text:
            freq[char] = freq.get(char, 0) + 1
        
        # Build tree
        heap = [Node(char=c, freq=f) for c, f in freq.items()]
        heapq.heapify(heap)
        
        if len(heap) == 1:
            return Node(freq=heap[0].freq, left=heap[0])
        
        while len(heap) > 1:
            left, right = heapq.heappop(heap), heapq.heappop(heap)
            heapq.heappush(heap, Node(freq=left.freq + right.freq, left=left, right=right))
        
        return heapq.heappop(heap)
    
    def get_codes(self, node, code=""):
        if not node:
            return {}
        if node.char:
            return {node.char: code or "0"}
        return {**self.get_codes(node.left, code + "0"), **self.get_codes(node.right, code + "1")}
    
    def encode(self, text):
        self.root = self.build_tree(text)
        self.codes = self.get_codes(self.root)
        return "".join(self.codes[c] for c in text)
    
    def decode(self, encoded):
        result, node = [], self.root
        for bit in encoded:
            node = node.left if bit == '0' else node.right
            if node.char:
                result.append(node.char)
                node = self.root
        return "".join(result)
    
    def save(self, filename, encoded):
        with open(filename, 'wb') as f:
            pickle.dump({'tree': self.root, 'data': encoded}, f)
    
    def load(self, filename):
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            self.root = data['tree']
            return data['data']

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python huffman.py [encode/decode] input output")
        sys.exit()
    
    cmd, input_file, output_file = sys.argv[1], sys.argv[2], sys.argv[3]
    huff = HuffmanCoding()
    
    if cmd == "encode":
        text = open(input_file, 'r').read()
        encoded = huff.encode(text)
        huff.save(output_file, encoded)
        
        orig_size = os.path.getsize(input_file)
        comp_size = os.path.getsize(output_file)
        
        if comp_size < orig_size:
            saved = orig_size - comp_size
            percent = (saved / orig_size) * 100
            print(f"\nDone! {orig_size} bytes -> {comp_size} bytes")
            print(f"Compressed: {percent:.1f}% smaller\n")
        else:
            added = comp_size - orig_size
            percent = (added / orig_size) * 100
            print(f"\nDone! {orig_size} bytes -> {comp_size} bytes")
            print(f"Got bigger: +{percent:.1f}% (tree overhead)\n")
        
    elif cmd == "decode":
        encoded = huff.load(input_file)
        decoded = huff.decode(encoded)
        open(output_file, 'w').write(decoded)
        print(f"\nDecoded to {output_file}\n")
