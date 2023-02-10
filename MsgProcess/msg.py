msg = ""
with open('MsgProcess/msg_uprocessed.txt', "r") as f:
    data = f.read()
    for c in data:
        if 'a' <= c <= 'z': msg += c
        elif 'A' <= c <= 'Z': msg += c.lower()
        elif c == ' ': msg += c

with open("MsgProcess/msg_no_symbol.txt", "w") as f:
    f.write(msg)

space_nxt = []
n = len(msg)
msg_processed = ""
step = 0
for i in range(n):
    if msg[i] == ' ':
        # space_nxt.append(step)
        step = -1
        continue
    elif step == -1:
        step = 0
    step += 1
    msg_processed += msg[i]

with open("MsgProcess/msg_processed.txt", "w") as f:
    f.write(msg_processed)

print(space_nxt)