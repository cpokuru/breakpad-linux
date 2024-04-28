#include <iostream>
#include <thread>
#include <chrono>
#include <breakpad/client/linux/handler/exception_handler.h>

bool Thread1Crashed = false;
bool Thread2Crashed = false;

void Thread1() {
    // Simulate some work
    std::this_thread::sleep_for(std::chrono::seconds(2));
}

void Thread2() {
    // Simulate some work
    std::this_thread::sleep_for(std::chrono::seconds(1));

    // Crash in thread 2
    int* ptr = nullptr;
    *ptr = 42;  // Access violation
}

// Breakpad callback function to handle crashes
bool CrashCallback(const google_breakpad::MinidumpDescriptor& descriptor,
                   void* context,
                   bool succeeded) {
    std::cerr << "Crash dump written to: " << descriptor.path() << std::endl;
    return succeeded;
}

int main() {
    google_breakpad::MinidumpDescriptor descriptor("./");
    google_breakpad::ExceptionHandler eh(descriptor,
                                         /*filter*/ nullptr,
                                         CrashCallback,
                                         /*context*/ nullptr,
                                         true, -1);

    std::thread t1(Thread1);
    std::thread t2(Thread2);

    t1.join();
    t2.join();

    return 0;
}

