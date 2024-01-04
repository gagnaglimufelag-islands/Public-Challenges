#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#define ROWS 10
#define COLS 10
#define MAX_LEN 101

int original[][10] = {
    {0x67, 0x67, 0x7b, 0x48, 0x33, 0x63, 0x6b, 0x31, 0x6e, 0x39},
    {0x44, 0x31, 0x34, 0x67, 0x30, 0x6e, 0x34, 0x6c, 0x5f, 0x5f},
    {0x5f, 0x39, 0x6c, 0x79, 0x5f, 0x46, 0x75, 0x6e, 0x41, 0x34},
    {0x79, 0x6e, 0x68, 0x5f, 0x4c, 0x30, 0x30, 0x5f, 0x64, 0x72},
    {0x6c, 0x31, 0x74, 0x75, 0x6e, 0x64, 0x70, 0x34, 0x76, 0x72},
    {0x6c, 0x7a, 0x31, 0x30, 0x7d, 0x73, 0x73, 0x6e, 0x33, 0x34},
    {0x34, 0x61, 0x57, 0x42, 0x64, 0x6e, 0x34, 0x64, 0x6e, 0x79},
    {0x63, 0x6d, 0x5f, 0x63, 0x69, 0x70, 0x45, 0x5f, 0x74, 0x35},
    {0x31, 0x34, 0x5f, 0x35, 0x31, 0x5f, 0x33, 0x72, 0x75, 0x5f},
    {0x64, 0x61, 0x52, 0x5f, 0x34, 0x5f, 0x33, 0x6b, 0x31, 0x4c}};

bool compare(int lhs[][COLS], int rhs[][COLS], int rows, int cols, char result[MAX_LEN - 1]) {
  int cnt = 0;
  int top = 0, bottom = rows - 1;
  int left = 0, right = cols - 1;
  int direction = 0;

  while (top <= bottom && left <= right) {
    if (direction == 0) {
      for (int i = left; i <= right; i++) {
        if (lhs[top][i] != rhs[top][i]) {
          return false;
        }
        result[cnt] = (char)(rhs[top][i]);
        cnt++;
      }
      top++;
    } else if (direction == 1) {
      for (int i = top; i <= bottom; i++) {
        if (lhs[i][right] != rhs[i][right]) {
          return false;
        }
        result[cnt] = (char)(rhs[i][right]);
        cnt++;
      }
      right--;
    } else if (direction == 2) {
      for (int i = right; i >= left; i--) {
        if (lhs[bottom][i] != rhs[bottom][i]) {
          return false;
        }
        result[cnt] = (char)(rhs[bottom][i]);
        cnt++;
      }
      bottom--;
    } else if (direction == 3) {
      for (int i = bottom; i >= top; i--) {
        if (lhs[i][left] != rhs[i][left]) {
          return false;
        }
        result[cnt] = (char)(rhs[i][left]);
        cnt++;
      }
      left++;
    }
    direction = (direction + 1) % 4;
  }
  return true;
}

void create(const char *str, int arr[ROWS][COLS]) {
  int i, j, index = 0;
  int len = strlen(str);

  for (i = 0; i < ROWS; i++) {
    for (j = 0; j < COLS; j++) {
      if (index < len)
        arr[i][j] = (int)str[index++];
      else
        arr[i][j] = ' ';
    }
  }
}

int main() {
  char input[MAX_LEN];
  int input_arr[ROWS][COLS];

  printf("Enter the key: ");
  fgets(input, sizeof(input), stdin);
  input[strcspn(input, "\n")] = '\0';

  if (strlen(input) != 100) {
    printf("Wrong!\n");
    return 1;
  }

  char result[MAX_LEN - 1] = {};
  create(input, input_arr);
  if (!compare(original, input_arr, ROWS, COLS, result)) {
    printf("Incorrect key!\n");
    return 1;
  }
  printf("Correct!\n");
  for (int c = 0; c < MAX_LEN - 1; c++) {
    printf("%c", result[c]);
  }
  printf("\n");
  return 0;
}
