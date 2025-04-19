
def max1(a, b):
    return a if a > b else b

# Function to display the logical timestamp
def display(e1, e2, p1, p2):
    print("\nThe time stamps of events in P1:")
    for i in range(e1):
        print(p1[i], end=" ")
    print("\nThe time stamps of events in P2:")
    for i in range(e2):
        print(p2[i], end=" ")

# Function to find the timestamp of events
def lamportLogicalClock(e1, e2, m):
    p1 = [0] * e1
    p2 = [0] * e2

    # Initialize timestamps
    for i in range(e1):
        p1[i] = i + 1
    for i in range(e2):
        p2[i] = i + 1

    # Print the dependency matrix
    print("Lamport Clock Assignments:")
    print("\t", end="")
    for i in range(e2):
        print(f"e2{i + 1}", end="\t")
    for i in range(e1):
        print(f"\ne1{i + 1}", end="\t")
        for j in range(e2):
            print(m[i][j], end="\t")

    # Apply Lamport clock rules
    for i in range(e1):
        for j in range(e2):
            if m[i][j] == 1:  # message sent from e1[i] to e2[j]
                p2[j] = max1(p2[j], p1[i] + 1)
                for k in range(j + 1, e2):
                    p2[k] = p2[k - 1] + 1
            elif m[i][j] == -1:  # message received by e1[i] from e2[j]
                p1[i] = max1(p1[i], p2[j] + 1)
                for k in range(i + 1, e1):
                    p1[k] = p1[k - 1] + 1

    display(e1, e2, p1, p2)

# Driver Code
if __name__ == "__main__":
    e1 = 5
    e2 = 3
    m = [[0] * e2 for _ in range(e1)]

    # Setting message dependencies
    m[1][2] = 1  # message sent from P1's event 2 to P2's event 3
    m[4][1] = -1 # message received by P1's event 5 from P2's event 2

    lamportLogicalClock(e1, e2, m)
