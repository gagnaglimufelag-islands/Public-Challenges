#include <openssl/aes.h>
#include <openssl/bio.h>
#include <openssl/buffer.h>
#include <openssl/evp.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/evp.h>

const char iv[] = "sixteenbyteivheh";
const char secretKey[] = "supersecretkeythatshouldnotleak!";
const char encryptedMsg[] =
    "oLsxPguNeX6oVxBiUwAZSJau6P2ruxYo/WaoDhIN1LGa9hurV1yuu7DwJfLmV9rcX/"
    "he1HuKZ6yI2t4e5CP3zw==";

typedef struct {
  const char *iv;
  const char *secret;
  const char *ciphertext;
} decryptor;

void base64decode(const char *encoded, unsigned char **decoded,
                  size_t *decodedLen) {
  BIO *bio, *b64;
  int len;

  *decodedLen = 0;

  b64 = BIO_new(BIO_f_base64());
  bio = BIO_new_mem_buf((void *)encoded, -1);
  bio = BIO_push(b64, bio);

  *decoded = (unsigned char *)malloc(strlen(encoded));
  len = BIO_read(bio, *decoded, strlen(encoded));

  *decodedLen = len;

  BIO_free_all(bio);
}

char *decryptAESCBC256(const char *encodedCiphertext, const unsigned char *key,
                       const unsigned char *iv) {
  unsigned char ciphertext[1024];
  int ciphertextLen;
  AES_KEY aesKey;
  EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
  char *plaintext;

  base64decode(encodedCiphertext, &ciphertext, &ciphertextLen);

  plaintext = (char *)malloc(ciphertextLen + AES_BLOCK_SIZE);
  memset(plaintext, 0, ciphertextLen + AES_BLOCK_SIZE);

  AES_set_decrypt_key(key, 256, &aesKey);

  EVP_CIPHER_CTX_init(ctx);
  EVP_DecryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv);
  EVP_DecryptUpdate(ctx, (unsigned char *)plaintext, &ciphertextLen,
                    ciphertext, ciphertextLen);
  EVP_DecryptFinal_ex(ctx, (unsigned char *)plaintext + ciphertextLen,
                      &ciphertextLen);
  EVP_CIPHER_CTX_free(ctx);

  return plaintext;
}

int main() {
  printf("It really is just strings\n");
  return 0;
}
