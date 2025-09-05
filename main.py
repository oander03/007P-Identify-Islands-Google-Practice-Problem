# This is a google practice problem

# The function takes in a "map" which is made up of 1s and 0s. The 1s represent land and the 0s represent water. 
# The purpose of this function is to count how many islands there are in the map. Islands count as multiple 
# 1s connected above, left, right, or below each other. Two 1s connected diagonally count as 2 islands


# --------------------------------- INPUTS -----------------------------------


map = [
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
]

# Answer = 6 islands

# map = [
#     [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
#     [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
#     [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
#     [1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
#     [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
#     [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
# ]

# # Answer = 16 islands

# --------------------------------- MY CODE -----------------------------------

Xlen = len(map[0])
Ylen = len(map)

MAXISLANDS = 30

# Temporary array that keeps track of positions of the island
infection = [[999 for _ in range(2)] for _ in range(MAXISLANDS)]

# Function that makes it so that if the index is out of bounds it returns 0
def safe_get(arr, row, col):
    if 0 <= row < len(arr) and 0 <= col < len(arr[row]):
        return arr[row][col]
    return 0

islandNum = 1

# Function that counts the islands on the map
for j in range(Ylen):
    for i in range(Xlen):
        if map[j][i] == 1:
            islandNum += 1
            l = 0
            k = 0
            infection[k][0] = j
            infection[k][1] = i
            map[infection[k][0]][infection[k][1]] = islandNum
            # Causes a loop that infects the island with a new number by checking if there are any 1s above, left, right, and below.
            # If there is a 1 in those places it will log it in the infection array and go through each position one by one.
            while infection[k][0] != 999:
                if safe_get(map, infection[k][0]-1, infection[k][1]) == 1:
                    map[infection[k][0]-1][infection[k][1]] = islandNum
                    l += 1
                    infection[l][0] = infection[k][0]-1
                    infection[l][1] = infection[k][1]
                if safe_get(map, infection[k][0], infection[k][1]-1) == 1:
                    map[infection[k][0]][infection[k][1]-1] = islandNum
                    l += 1
                    infection[l][0] = infection[k][0]
                    infection[l][1] = infection[k][1]-1
                if safe_get(map, infection[k][0], infection[k][1]+1) == 1:
                    map[infection[k][0]][infection[k][1]+1] = islandNum
                    l += 1
                    infection[l][0] = infection[k][0]
                    infection[l][1] = infection[k][1]+1
                if safe_get(map, infection[k][0]+1, infection[k][1]) == 1:
                    map[infection[k][0]+1][infection[k][1]] = islandNum
                    l += 1
                    infection[l][0] = infection[k][0]+1
                    infection[l][1] = infection[k][1]
                # for n in range(Ylen):
                #     print(map[n])
                # print(infection)
                # print(k)
                # print(l)
                k += 1
            # Resets the temporary infection array
            infection = [[999 for _ in range(2)] for _ in range(MAXISLANDS)]

for n in range(Ylen):
    print(map[n])

print("\nThe amount of islands on the map are " + str(islandNum-1) + " islands")


























