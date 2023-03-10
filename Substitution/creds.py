# enc_key = [
#     ['a', 'z'], ['b', 'p'], ['c', 'm'], ['d', 'a'], ['e', 'x'], 
#     ['f', 'd'], ['g', 'k'], ['h', 'q'], ['i', 'u'], ['j', 'w'], 
#     ['k', 'o'], ['l', 'j'], ['m', 'n'], ['n', 'g'], ['o', 'c'], 
#     ['p', 'y'], ['q', 'i'], ['r', 'f'], ['s', 't'], ['t', 'h'], 
#     ['u', 'v'], ['v', 'l'], ['w', 'r'], ['x', 'e'], ['y', 'b'], 
#     ['z', 's']
# ]

enc_key = [
    ['A', 'Z'], ['B', 'P'], ['C', 'M'], ['D', 'A'], ['E', 'X'], 
    ['F', 'R'], ['G', 'K'], ['H', 'F'], ['I', 'U'], ['J', 'E'], 
    ['K', 'O'], ['L', 'J'], ['M', 'N'], ['N', 'G'], ['O', 'C'], 
    ['P', 'B'], ['Q', 'I'], ['R', 'Q'], ['S', 'T'], ['T', 'H'], 
    ['U', 'V'], ['V', 'L'], ['W', 'D'], ['X', 'S'], ['Y', 'Y'], 
    ['Z', 'W']
]

# enc_key = [
#     ['A', 'Z'], ['B', 'P'], ['C', 'M'], ['D', 'A'], ['E', 'X'], 
#     ['F', 'N'], ['G', 'L'], ['H', 'F'], ['I', 'G'], ['J', 'I'], 
#     ['K', 'O'], ['L', 'J'], ['M', 'R'], ['N', 'C'], ['O', 'U'], 
#     ['P', 'K'], ['Q', 'E'], ['R', 'Q'], ['S', 'T'], ['T', 'H'], 
#     ['U', 'V'], ['V', 'B'], ['W', 'D'], ['X', 'S'], ['Y', 'Y'], 
#     ['Z', 'W']
# ]

dec_key = sorted(enc_key, key=lambda x: x[1])