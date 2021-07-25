S = "spammy"

# Slice sections from S
S = S[:3] + "xx" + S[5:]
print(S)

S = "spammy"

# Replace all mm with xx in S
S = S.replace("mm", "xx")
print(S)

print("aa$bb$cc$dd".replace("$", "SPAM"))