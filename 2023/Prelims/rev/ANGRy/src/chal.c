#include <stdio.h>
#include <stdbool.h>

bool check_flag(char *buffer)
{
  if (buffer[4] == 0x5f) {
    if (buffer[3] == 0x52) {
      if (buffer[23] == 0x46) {
        if (buffer[6] == 0x35) {
          if (buffer[8] == 0x4c) {
            if (buffer[12] == 0x5f) {
              if (buffer[22] == 0x31) {
                if (buffer[0] == 0x41) {
                  if (buffer[17] == 0x5f) {
                    if (buffer[11] == 0x33) {
                      if (buffer[15] == 0x47) {
                        if (buffer[18] == 0x31) {
                          if (buffer[14] == 0x4e) {
                            if (buffer[24] == 0x33) {
                              if (buffer[10] == 0x56) {
                                if (buffer[1] == 0x4e) {
                                  if (buffer[9] == 0x30) {
                                    if (buffer[21] == 0x4c) {
                                      if (buffer[2] == 0x47) {
                                        if (buffer[7] == 0x5f) {
                                          if (buffer[13] == 0x41) {
                                            if (buffer[5] == 0x31) {
                                              if (buffer[16] == 0x52) {
                                                if (buffer[19] == 0x35) {
                                                  if (buffer[20] == 0x5f) {
                                                    return true;
                                                  }
                                                }
                                              }
                                            }
                                          }
                                        }
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
return false;
}


int main(int argc, char *argv[])
{
  while (true)
  {
    char input_buf[26];
    
    printf("Enter flag: ");
    fgets(input_buf, sizeof(input_buf), stdin);
    
    if (check_flag(input_buf) == true)
    {
      printf("\n[+] YOU GOT THE FLAG!\n\n");
      printf("gg{%s}\n\n", input_buf);
      break;
	  }
	  else
	  {
		  puts("\nNope...Try again!\n");
	  }
  }

  return 0;
}
