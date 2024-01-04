def spiral_order(matrix):
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1
    direction = 0  # 0: go right, 1: go down, 2: go left, 3: go up
    result = []

    while top <= bottom and left <= right:
        if direction == 0:  # Go right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
        elif direction == 1:  # Go down
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
        elif direction == 2:  # Go left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        elif direction == 3:  # Go up
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        direction = (direction + 1) % 4

    return result


array = [
    [0x67, 0x67, 0x7b, 0x48, 0x33, 0x63, 0x6b, 0x31, 0x6e, 0x39],
    [0x44, 0x31, 0x34, 0x67, 0x30, 0x6e, 0x34, 0x6c, 0x5f, 0x5f],
    [0x5f, 0x39, 0x6c, 0x79, 0x5f, 0x46, 0x75, 0x6e, 0x41, 0x34],
    [0x79, 0x6e, 0x68, 0x5f, 0x4c, 0x30, 0x30, 0x5f, 0x64, 0x72],
    [0x6c, 0x31, 0x74, 0x75, 0x6e, 0x64, 0x70, 0x34, 0x76, 0x72],
    [0x6c, 0x7a, 0x31, 0x30, 0x7d, 0x73, 0x73, 0x6e, 0x33, 0x34],
    [0x34, 0x61, 0x57, 0x42, 0x64, 0x6e, 0x34, 0x64, 0x6e, 0x79],
    [0x63, 0x6d, 0x5f, 0x63, 0x69, 0x70, 0x45, 0x5f, 0x74, 0x35],
    [0x31, 0x34, 0x5f, 0x35, 0x31, 0x5f, 0x33, 0x72, 0x75, 0x5f],
    [0x64, 0x61, 0x52, 0x5f, 0x34, 0x5f, 0x33, 0x6b, 0x31, 0x4c]]

def test():
    for y in range(0, 10):
        for x in range(0, 10):
            print(chr(array[y][x]), end="")
    print("")

    result = spiral_order(array)
    flag = "gg{H3ck1n9_4rr4y5_L1k3_4_Rad1c4lly_D14g0n4l_Adv3ntur3_15_4maz1n9ly_Fun_4nd_Epic_W1th_L00ps4ndB0unds}"
    assert "".join([chr(x) for x in result]) == flag

if __name__ == '__main__':
    test()
