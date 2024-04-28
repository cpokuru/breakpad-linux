#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 256

void extractCrashDetails(FILE *file) {
    printf("ENter --\n");
    char line[MAX_LINE_LENGTH];
    int inCrashDetails = 0;

    // Read each line from the file
    while (fgets(line, MAX_LINE_LENGTH, file)) {
        // Check if the line contains "crashed"
        if (strstr(line, "crashed") != NULL) {
            // Start printing crash details from this line
            inCrashDetails = 1;
        }
        // Print crash details if inside crash section
        if (inCrashDetails) {

                printf("%s", line);
            // Check if the line contains a CPP file
            char *filePtr = strstr(line, ".cpp");
            if (filePtr != NULL) {
                // Print the line only if it contains the CPP file and line number
                //printf("%s", line);
                // Exit the loop once crash details are printed
                break;
            }
        }
    }
    printf("EXit --\n");
}

int main() {
    FILE *file = fopen("output.txt", "r");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    extractCrashDetails(file);

    fclose(file);
    return 0;
}

