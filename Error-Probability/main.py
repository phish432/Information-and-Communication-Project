from utils import *

# Number of decoding iterations
N = 2000

# Given n, k, p values

narr = [15, 20]
parr = [0.015, 0.1, 0.45]
k = 10

# Custom n, k, p values

# narr = [i for i in range(12, 25)]
# parr = [0.015, 0.1, 0.45]
# k = 10

for p in parr:
    PE_array = []

    for n in narr:
        EArray = []

        for i in range(5):
            code = GenerateCode(n, k)
            E = 0

            for j in range(N):
                # Pick a random vector from the binary vector space
                c = SelectCodeword(code)

                # Pass the codeword through BSC(p) to get output y
                y = BSC(p, c)

                # Decode y using MDD to get the estimates of c
                # Select any one of them if there are multiple
                estimate = SelectCodeword(MDD(code, y))

                # Calculate value of indicator I and return it
                I = ErrorIndicator(estimate, c)

                # Add to total error count
                E += I

            EArray.append(E / N)

        minE = min(EArray)
        PE_array.append(minE)

        print("n = {}, k = {}, p = {}".format(n, k, p))
        print("Avg. Probability of Error in Decoding")
        for i in range(len(EArray)):
            print("Run {} = {}".format(i + 1, EArray[i]))
        print("Minimum Avg. Probability of Error = {}\n".format(minE))

    plt.plot(narr, PE_array, marker="o")

plt.title(
    r"Minimum Avg. Probability of Error vs. $n$"
    + "\n"
    + r"$P_E(n,k,p) = \frac{E}{N}$,"
    + f"k = {k}"
)
plt.xlabel(r"$n$")
plt.ylabel(r"$P_E(n,k,p)$")
plt.legend(["p = {}".format(i) for i in parr])
plt.savefig("result_given.png")
