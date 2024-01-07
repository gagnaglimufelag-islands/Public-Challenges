void chall() {
    int input[20] = {37, 37, 57, 59, 46, 32, 47, 113, 49, 49, 118, 38, 113, 49, 48, 113, 52, 113, 48, 63};
    int key = 0x42;

    for (int i = 0; i < 8; i++) {
        input[i] = input[i] ^ key;
    }
}

int main() {
    chall();
}
