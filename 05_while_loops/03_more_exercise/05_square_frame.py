def printSymbol(s):
    print(f"{s} {(n - 2) * '- '}{s}")

n = int(input())

printSymbol('+')  # <--

for i in range(n - 2):
    printSymbol('|')

printSymbol('+')