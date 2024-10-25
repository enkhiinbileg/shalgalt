#1b
#2a
#3a
#4a
#5a
#6a
#7c
#7.1a
#8d
#9e
#10d
#11a
#12b
#13.Массив нь дараалсан хаягийн санах ойд хадгалагддаг бөгөөд хурдан санах, харин холбоослогдсон жагсаалт нь динамик бүтэцтэй тул санах ойд хэсэгчилсэн байршил үүсгэдэг.
#14.Стек нь сүүлийн орсон өгөгдлийг хамгийн эхэнд гаргах зарчмыг баримталдаг бол мод нь шаталсан өгөгдлийн бүтэц бөгөөд өргөтгөсөн харилцааг илэрхийлдэг.
#15c
#16a
#17A
#18c
#19a
#20b
#21b
#22a
#Greedy algorithm(b)
# Хаффман код 
#import heapq
#from collections import defaultdict

#class Node:
#    def __init__(self, freq, symbol, left=None, right=None):
#        self.freq = freq
#        self.symbol = symbol
#        self.left = left
#        self.right = right
#
#    def __lt__(self, other):
#        return self.freq < other.freq
#
#def huffman_code(symbols):
#    heap = [Node(freq, symbol) for symbol, freq in symbols.items()]
#    heapq.heapify(heap)
#
#    while len(heap) > 1:
#        node1 = heapq.heappop(heap)
#        node2 = heapq.heappop(heap)
#        merged = Node(node1.freq + node2.freq, None, node1, node2)
# #       heapq.heappush(heap, merged)
#
# #   huffman_tree = heapq.heappop(heap)
#    codes = {}
#
#    def generate_code(node, current_code=""):
#        if node is None:
#            return
#        if node.symbol is not None:
#            codes[node.symbol] = current_code
#        generate_code(node.left, current_code + "0")
#        generate_code(node.right, current_code + "1")
#
#    generate_code(huffman_tree)
# #   return codes
#
#symbols = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
#huffman_codes = huffman_code(symbols)
#print(huffman_codes)
#Python дээр Bubble Sort болон Insertion Sort алгоритмуудыг хэрэгжүүл.
#def bubble_sort(arr):
#    n = len(arr)
#    for i in range(n-1):
#        for j in range(0, n-i-1):
#            if arr[j] > arr[j+1]:
#                arr[j], arr[j+1] = arr[j+1], arr[j]
#    return arr
#def insertion_sort(arr):
#    for i in range(1, len(arr)):
#        key = arr[i]
#        j = i-1
#        while j >= 0 and key < arr[j]:
#            arr[j + 1] = arr[j]
#            j -= 1
#        arr[j + 1] = key
#    return arr
#Алгоритмын гүйцэтгэлийн шинжилгээ(b)
#Бинар мод үүсгэх ба хайлтын мод
#class Node:
#Функц ба буцаах утга
#Асуулт 1: Дараах функц ямар утга буцаах вэ?(b)
