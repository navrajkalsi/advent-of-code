#include <stdlib.h>
#include <stdio.h>

#define INPUT "input.txt"

int rows = 0,
    cols = 0,
    source = 0,
    answer = 0;
char *lines = NULL;

void follow_beam(int row, int col) {
  if (row == rows) {
      ++answer;
      return;
  }

  if (row < 0 || row >= rows || col < 0 || col >= cols) 
    return;

  if (lines[(row * (cols + 1)) + col] == '^') {
    follow_beam(row + 1, col + 1);
    follow_beam(row + 1, col - 1);
  }
  else 
    follow_beam(row + 1, col);
}

int main(void) {
  FILE *input = fopen(INPUT, "r");
  if (!input)
    return -1;

  fseek(input, 0, SEEK_END);

  long input_size = ftell(input);
  rewind(input);

  lines = malloc(input_size * sizeof(char));

  size_t input_read = fread(lines, sizeof(char), input_size, input);
  printf("Read %ld bytes from %s:\n", input_read, INPUT);
  printf("\n%.*s\n", (int)input_size, lines);

  // setting global vars
  while (cols < input_size && lines[cols] != '\n') {
    if (lines[cols] == 'S')
      source = cols;
    cols++;
  }
  rows = input_size / (cols + 1);

  printf("Rows: %d, Columns: %d\nSource at: %d\n", rows, cols, source);

  follow_beam(0, source);

  fclose(input);
  
  printf("\nAnswer: %d\n", answer);
}
