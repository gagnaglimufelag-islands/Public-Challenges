#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_LEN 11
#define NUM_WOR 10

typedef struct node {
  struct node *left;
  struct node *right;
  int data;
} node;

node *new_node(int data) {
  node *tmp = (node *)malloc(sizeof(node));

  tmp->data = data;
  tmp->left = NULL;
  tmp->right = NULL;

  return tmp;
}

node *insert(node *root, int data) {
  if (root == NULL) {
    root = new_node(data);
  } else if (data > root->data) {
    root->right = insert(root->right, data);
  } else if (data < root->data) {
    root->left = insert(root->left, data);
  }
  return root;
}

node *getMax(node *root) {
  if (root->right != NULL) {
    return getMax(root->right);
  }
  return root;
}

node *delete(node *root, int data) {
  if (root == NULL) {
    return root;
  } else if (data > root->data) {
    root->right = delete (root->right, data);
  } else if (data < root->data) {
    root->left = delete (root->left, data);
  } else if (data == root->data) {
    if ((root->left == NULL) && (root->right == NULL)) {
      free(root);
      return NULL;
    } else if (root->left == NULL) {
      node *tmp = root;
      root = root->right;
      free(tmp);
      return root;
    } else if (root->right == NULL) {
      node *tmp = root;
      root = root->left;
      free(tmp);
      return root;
    } else {
      node *tmp = getMax(root->left);
      root->data = tmp->data;
      root->left = delete (root->left, tmp->data);
    }
  }
  return root;
}

void purge(node *root) {
  if (root != NULL) {
    if (root->left != NULL) {
      purge(root->left);
    }
    if (root->right != NULL) {
      purge(root->right);
    }
    free(root);
    root = NULL;
  }
}

void output(node *root, char *value, int *i) {
  if (root != NULL) {
    output(root->left, value, i);
    value[*i] = (char)root->data;
    (*i)++;
    output(root->right, value, i);
  }
}

bool strcnp(const char *lhs, const char *rhs, int len) {
  for (int i = 0; i < len; i++) {
    if (lhs[i] != rhs[i]) {
      return false;
    }
  }
  return true;
}

int main() {
  char words[NUM_WOR][MAX_LEN];
  for (int word_num = 0; word_num < NUM_WOR; word_num++) {
    printf("Enter hashtag: ");

    fgets(words[word_num], sizeof(words[word_num]), stdin);
    words[word_num][strcspn(words[word_num], "\n")] = '\0';
    int word_len = strlen(words[word_num]);

    if (word_len < 5) {
      printf("Nope!\n");
      return 1;
    }

    for (int w = 0; w < word_num; w++) {
      if (strcmp(words[word_num], words[w]) == 0) {
        printf("Nope!\n");
        return 1;
      }
    }

    node *root = NULL;
    int data = 0;
    for (int c = 0; c < word_len; c++) {
      root = insert(root, (int)(words[word_num][c]));
    }

    char *value = (char*)malloc((word_len + 1) * sizeof(char));
    value[word_len] = '\0';
    int index = 0;
    output(root, value, &index);

    if (!strcnp(words[word_num], value, word_len)) {
      printf("Nope!\n");
      free(value);
      purge(root);
      return 1;
    }
    free(value);
    purge(root);
  }

  printf("\nCorrect!\nRun the following:\n\n");
  printf("echo '");
  for (int i = 0; i < NUM_WOR; i++) {
    printf("%s", words[i]);
    if (i != NUM_WOR - 1) {
      printf("_");
    }
  }
  printf("' | nc IP PORT\n\n");
  printf("You can get the IP and the PORT values in the challenge description\n");
  return 0;
}
