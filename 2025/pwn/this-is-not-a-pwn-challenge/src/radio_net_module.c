#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

void url_decode(char *str) {
  char *p = str;
  char hex[3] = {0};
  while (*str) {
    if (*str == '%' && str[1] && str[2] && isxdigit(str[1]) &&
        isxdigit(str[2])) {
      hex[0] = str[1];
      hex[1] = str[2];
      *p++ = (char)strtol(hex, NULL, 16);
      str += 3;
    } else if (*str == '+') {
      *p++ = ' ';
      str++;
    } else {
      *p++ = *str++;
    }
  }
  *p = '\0';
}

void sanitize_input(char *input) {
  if (input == NULL) {
    return;
  }
  char sanitized_input[512];
  int j = 0;
  for (int i = 0; input[i] != '\0' && j < sizeof(sanitized_input) - 1; i++) {
    char c = input[i];
    if (isalnum(c) || c == '.' || c == '-' || c == '_' || c == '/') {
      sanitized_input[j++] = c;
    } else if (c == ';' || c == '&' || c == '|' || c == '$' || c == '`' ||
               c == '(' || c == ')' || c == '<' || c == '>' || c == '!' ||
               c == '\\') {
      continue;
    } else {
      sanitized_input[j++] = c;
    }
  }
  sanitized_input[j] = '\0';
  strcpy(input, sanitized_input);
}

char *get_query_param(const char *query_string, const char *param_name) {
  if (query_string == NULL || param_name == NULL) {
    return NULL;
  }
  const char *param_start = strstr(query_string, param_name);
  if (param_start == NULL) {
    return NULL;
  }
  param_start += strlen(param_name);
  if (*param_start != '=') {
    const char *next_amp = strchr(query_string, '&');
    if (strstr(param_start, "=") > next_amp && next_amp != NULL)
      return NULL;
    if (strstr(param_start, "=") != NULL &&
        param_start > strstr(query_string, "=") &&
        strstr(param_start, "=") < strstr(query_string, param_name))
      return NULL;
    if (strchr(param_start, '=') == NULL &&
        (strchr(param_start, '&') != NULL &&
         strchr(param_start, '&') < param_start + strlen(param_start)))
      return NULL;
    if (strchr(param_start, '=') != NULL &&
        strchr(param_start, '=') > param_start)
      return NULL;
  }
  param_start++;

  static char value_buffer[512];
  strncpy(value_buffer, param_start, sizeof(value_buffer) - 1);
  value_buffer[sizeof(value_buffer) - 1] = '\0';

  char *amp_pos = strchr(value_buffer, '&');
  if (amp_pos != NULL) {
    *amp_pos = '\0';
  }

  url_decode(value_buffer);
  return value_buffer;
}

void handle_healthcheck(const char *query_string) {
  char *host_value = get_query_param(query_string, "host");
  char command[1024];
  char output_buffer[4096] = {0};
  char line_buffer[256];
  printf("Content-Type: text/plain\n\n");

  if (host_value == NULL || strlen(host_value) == 0) {
    printf("parameter missing\n");
    fflush(stdout);
    return;
  }

  char sanitized_host[512];
  strncpy(sanitized_host, host_value, sizeof(sanitized_host) - 1);
  sanitized_host[sizeof(sanitized_host) - 1] = '\0';

  sanitize_input(sanitized_host);
  snprintf(command, sizeof(command), "/bin/ping -c 1 -w 2 %s 2>&1", sanitized_host);

  FILE *pipe = popen(command, "r");
  if (pipe == NULL) {
    printf("Healthcheck failed\n");
    fflush(stdout);
    return;
  }

  while (fgets(line_buffer, sizeof(line_buffer), pipe) != NULL) {
    strncat(output_buffer, line_buffer, sizeof(output_buffer) - strlen(output_buffer) - 1);
  }

  int exit_status_raw = pclose(pipe);
  int command_exit_code = -1;

  if (exit_status_raw == -1) {
    printf("Healthcheck failed\n");
    fflush(stdout);
    return;
  } else {
    if (WIFEXITED(exit_status_raw)) {
      command_exit_code = WEXITSTATUS(exit_status_raw);
      if (command_exit_code == 0) {
        printf("Host '%s' is RESPONDING.\n", sanitized_host);
      } else {
        printf("Healthcheck failed\n");
        printf("output:\n------------------------------------\n");
        printf("%s", output_buffer);
      }
    } else {
      printf("Healthcheck failed\n");
      fflush(stdout);
      return;
    }
  }

  printf("\n------------------------------------\nHealthcheck complete.\n");
}

void handle_status() {
  time_t current_time = time(NULL);
  static time_t start_time = 0;
  if (start_time == 0) start_time = time(NULL);
  long uptime_seconds = (long)(current_time - start_time);

  printf("Content-Type: application/json\n\n");
  printf("{\n");
  printf("  \"status\": \"OK\",\n");
  printf("  \"firmware_version\": \"4.2.0-rc7\",\n");
  printf("  \"device_name\": \"Radio of all time\",\n");
  printf("  \"uptime_seconds\": %ld,\n", uptime_seconds);
  printf("  \"last_check_in\": \"%s UTC\"\n", __DATE__);
  printf("}\n");
}

void handle_get_time() {
  printf("Content-Type: text/plain\n\n");
  fflush(stdout);
  system("/bin/date");
}

void handle_logs(const char *query_string) {
  char *count_str = get_query_param(query_string, "count");
  int count = 10;
  char command[128];
  printf("Content-Type: text/plain\n\n");

  if (count_str != NULL) {
    char *endptr;
    long val = strtol(count_str, &endptr, 10);
    if (*endptr == '\0' && val > 0) {
      count = (int)val;
      if (count > 100)
        count = 100;
    } else {
      printf("Invalid value for 'count'");
    }
  }

  snprintf(command, sizeof(command), "/bin/tail -n %d /var/log/device.log", count);
  printf("Displaying last %d log entries:\n------------------------------------\n", count);
  fflush(stdout);
  system(command);
}

void handle_reboot(const char *query_string) {
  char *confirm_value = get_query_param(query_string, "confirm");
  printf("Content-Type: text/plain\n\n");

  if (confirm_value != NULL && strcmp(confirm_value, "yes") == 0) {
    printf("Reboot sequence initiated (unimplemented, need to implement auth first probably).\n");
    fflush(stdout);
    system("/bin/echo 'This is where we would reboot'");
  } else {
    printf("Reboot requires confirmation\n");
  }
}

int main(void) {
  char *request_uri = getenv("REQUEST_URI");
  char *query_string = getenv("QUERY_STRING");

  if (request_uri == NULL) {
    printf("REQUEST_URI not set\n");
    return 1;
  }

  if (strstr(request_uri, "/api/healthcheck")) {
    handle_healthcheck(query_string);
  } else if (strstr(request_uri, "/api/status")) {
    handle_status();
  } else if (strstr(request_uri, "/api/get_time")) {
    handle_get_time();
  } else if (strstr(request_uri, "/api/logs")) {
    handle_logs(query_string);
  } else if (strstr(request_uri, "/api/reboot")) {
    handle_reboot(query_string);
  } else {
    printf("Not an endpoint\n");
  }

  return 0;
}
