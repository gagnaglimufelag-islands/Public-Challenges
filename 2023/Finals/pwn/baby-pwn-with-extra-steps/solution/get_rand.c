#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
  srand(time(NULL));
  printf("%d\n", rand() % (0x9999 + 1 - 0x1001) + 0x1001);
  return 0;
}

