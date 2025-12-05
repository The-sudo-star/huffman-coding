Huffman Coding Implementation

[Prince Adjei]
California State University San Marcos
CS 201 - Data Structures
Fall 2025

I. INTRODUCTION

Huffman coding is a lossless compression algorithm that assigns variable-length codes to characters based on frequency [1]. Frequent characters get short codes, rare characters get long codes. This implementation demonstrates the algorithm on small test files.

II. IMPLEMENTATION

A. Data Structures
- Node class: binary tree nodes with character, frequency, and children
- Min-heap: priority queue for tree construction (Python heapq)
- Dictionary: character-to-code mappings

B. Algorithm
1) Count character frequencies in O(n) time
2) Build binary tree using greedy approach - always merge two lowest frequencies (O(k log k))
3) Generate codes via tree traversal - left=0, right=1 (O(k))
4) Encode: replace characters with codes (O(n))
5) Decode: traverse tree using bits (O(m))

Overall time complexity: O(n + k log k) where n = text length, k = unique characters

C. Visual Example

Tree for text "BEEP" (Frequencies: B:1, P:1, E:2):

        [4]
       /   \
     [E:2] [2]
           / \
        [B:1][P:1]

Resulting Codes: E=0, B=10, P=11

III. RESULTS

Tested on three files with actual compression results:

Small file (512 bytes):
- Compressed to: 3,694 bytes
- Size increase: +621.5% (file got bigger)
- Reason: Tree storage overhead exceeds text size

Medium file (2,181 bytes):
- Compressed to: 12,656 bytes
- Size increase: +480.3% (file got bigger)
- Reason: Tree overhead still dominates

Large file (3,148 bytes):
- Compressed to: 15,682 bytes
- Size increase: +398.2% (file got bigger)
- Reason: Diverse character set creates large tree

Analysis: All test files increased in size because:
1. The Huffman tree structure must be stored with compressed data
2. Python's pickle serialization adds metadata overhead
3. Small files with diverse character sets create large trees
4. For positive compression, need much larger files (>10KB) or repetitive text

All files successfully decoded back to originals with 100% accuracy, confirming lossless compression works correctly.

IV. CONCLUSION

Successfully implemented Huffman coding in ~100 lines of Python. The algorithm works correctly - encoding and decoding are error-free. However, results demonstrate that Huffman coding is inefficient for small files due to tree storage overhead. The implementation would work better on larger files (kilobytes or more) where tree overhead becomes negligible relative to file size.

Learned: binary trees, priority queues, greedy algorithms, and the practical limitations of compression algorithms on small datasets.

REFERENCES

[1] D. A. Huffman, "A Method for the Construction of Minimum-Redundancy Codes," Proceedings of the IRE, vol. 40, no. 9, pp. 1098-1101, 1952.


