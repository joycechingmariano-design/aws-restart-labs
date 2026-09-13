# Python3.11
# Coding: utf-8

# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = (
    "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrr"
    "eaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
)

# Store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Combine B chain and A chain to form insulin:
insulin = bInsulin + aInsulin

# pKR values:
pKR = {
    'y': 10.07,
    'c': 8.18,
    'k': 10.53,
    'r': 12.48,
    'h': 6.00,
    'd': 3.65,
    'e': 4.25
}

# Count how many of each amino acid appears in insulin:
seqCount = {
    x: float(insulin.count(x))
    for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']
}

# Start pH at 0:
pH = 0

# Calculate the net charge from pH 0 to pH 14:
while pH <= 14:

    positiveCharge = sum({
        x: (
            (seqCount[x] * (10 ** pKR[x]))
            / ((10 ** pH) + (10 ** pKR[x]))
        )
        for x in ['k', 'h', 'r']
    }.values())

    negativeCharge = sum({
        x: (
            (seqCount[x] * (10 ** pH))
            / ((10 ** pH) + (10 ** pKR[x]))
        )
        for x in ['y', 'c', 'd', 'e']
    }.values())

    netCharge = positiveCharge - negativeCharge

    print('{0:.2f}'.format(pH), netCharge)

    pH += 1