"""
TITTLE: Homework 2 of Formal languages and compilers
PROGRAM: Implementation of CYK ALGORITHM  explained on Dexter C. Kozen
AUTHORS: David Alejandro Ramirez and Ana Sofia Alfonso Moncada
"""
# Function to implement the CYK algorithm
def CYK(G, str):
    # Getting the length of the input string
    size = len(str)
    # Matrix to store intermediate results
    M = []
    for i in range(size):
        M.append([])

    # Completing the matrix
    # First case, substring length = 1
    i = 0
    for a in str:
        nt = []
        for b in G:
            if a in G[b]:
                # Initialize cells with "-"
                for n in range(size):
                    M[i].append("-")
                # Add non-terminal symbol to the cell
                nt.append(b)
                M[i][i] = nt
        i += 1

    # For length greater than 1
    for l in range(2, size + 1):
        for i in range(size - l + 1):
            j = i + l - 1
            for k in range(i, j):
                agregar = []
                # Checking all grammar rules
                for b in G:
                    for a in G[b]:
                        if len(a) == 2:
                            nt = []
                            for c in a:
                                nt.append(c)
                            # If the substring can be formed using the grammar rules, add to list
                            if (nt[0] in M[k][i]) and (nt[1] in M[j][k + 1]):
                                agregar.append(b)
                                M[j][i] = agregar

    # Verify if the string is accepted or not
    if "S" in M[size - 1][0]:
        return "yes"
    else:
        return "No"


# Function to handle input and output
def Start():
    responses = {}

    G = {}

    # Input grammar rules
    l = input().split(" ")
    n_nt = l[0]  # Number of non-terminal symbols
    n_str = l[1]  # Number of strings to evaluate
    for h in range(int(n_nt)):
        r = input().split(" ")
        G[r[0]] = []
        for m in range(len(r) - 1):
            G[r[0]].append(r[m + 1])
    # Input strings
    for s in range(int(n_str)):
        string = input()
        response = CYK(G, string)
        responses[string] = response
    return responses


if __name__ == '__main__':
    # Input number of cases
    cases = int(input())
    collection = []
    # Loop through each case
    for i in range(cases):
        response = Start()
        collection.append(response)

    # Output results
    for a in collection:
        for x in a:
            print(f"{x} -> {a[x]}")