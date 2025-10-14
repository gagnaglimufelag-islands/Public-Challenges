CC=gcc
CFLAGS=-Wall -Wextra -Wno-unused-parameter
LDFLAGS=-static

TARGET=radio_net_module.cgi
SRC=radio_net_module.c

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC) $(LDFLAGS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
