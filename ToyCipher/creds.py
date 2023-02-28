key = "10111001010010100101010101011001000"
key = key[: 20]

sub_keys = []
[sub_keys.append(key[i: i + 16]) for i in range(5)]