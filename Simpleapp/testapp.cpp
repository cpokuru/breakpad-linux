#include <stdio.h>
#include <stdlib.h>
#include <breakpad/client/linux/handler/exception_handler.h>

// Global handler for exceptions
static bool DumpCallback(const google_breakpad::MinidumpDescriptor& descriptor,
                         void* context,
                         bool succeeded) {
  printf("Dump path: %s\n", descriptor.path());
  return succeeded;
}

void crash_function1() {
    // Accessing a NULL pointer to deliberately cause a crash
    int *ptr = NULL;
    *ptr = 10; // This will cause a segmentation fault
}

int main() {
    // Initialize Breakpad
    google_breakpad::MinidumpDescriptor descriptor("/tmp"); // Path to save minidump
    google_breakpad::ExceptionHandler eh(descriptor, NULL, DumpCallback, NULL, true, -1);

    printf("Starting crash program...\n");

    // Cause a crash
    crash_function1();

    printf("Program continues after crash (this shouldn't execute).\n");

    return 0;
}

