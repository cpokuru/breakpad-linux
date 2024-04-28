# ckpbreakpad
pre requisites
0.Install build essentials in your machine
1.clone the repo
https://github.com/google/breakpad
2.git clone https://chromium.googlesource.com/linux-syscall-support src/third_party/lss
3./configure
4.make 
5.make install 
6.all the required things will be in /usr/local
7.write you c/c++ code 
8.compile it
g++ -o test xxx.cpp -g -I/usr/local/include/breakpad -L/usr/local/lib -lbreakpad -lbreakpad_client
9.google-breakpad/src/tools/linux/dump_syms/dump_syms ./test > test.sym
10.head -n1 test.sym MODULE Linux x86_64 6EDC6ACDB282125843FD59DA9C81BD830 test
$ mkdir -p ./symbols/test/6EDC6ACDB282125843FD59DA9C81BD830
$ mv test.sym ./symbols/test/6EDC6ACDB282125843FD59DA9C81BD830
11.google-breakpad/src/processor/minidump_stackwalk minidump.dmp ./symbols

------------------

ubuntu@ubuntu-2204:~/ckp$ minidump_stackwalk /tmp/98dcf79a-ae80-4820-eedf95b2-309c0cff.dmp ./symbols/
2024-04-27 21:25:08: minidump.cc:5612: INFO: Minidump opened minidump /tmp/98dcf79a-ae80-4820-eedf95b2-309c0cff.dmp
2024-04-27 21:25:08: minidump.cc:5748: INFO: Minidump not byte-swapping minidump
2024-04-27 21:25:08: minidump.cc:6474: INFO: GetStream: type 15 not present
2024-04-27 21:25:08: minidump.cc:6474: INFO: GetStream: type 1197932545 not present
2024-04-27 21:25:08: minidump.cc:6474: INFO: GetStream: type 1197932546 not present
2024-04-27 21:25:08: minidump.cc:2704: INFO: MinidumpModule could not determine version for /home/ubuntu/ckp/crash
2024-04-27 21:25:08: minidump.cc:2704: INFO: MinidumpModule could not determine version for /usr/lib/x86_64-linux-gnu/libm.so.6
2024-04-27 21:25:08: minidump.cc:2704: INFO: MinidumpModule could not determine version for /usr/lib/x86_64-linux-gnu/libc.so.6
2024-04-27 21:25:08: minidump.cc:2704: INFO: MinidumpModule could not determine version for /usr/lib/x86_64-linux-gnu/libgcc_s.so.1
2024-04-27 21:25:08: minidump.cc:2704: INFO: MinidumpModule could not determine version for /usr/lib/x86_64-linux-gnu/libstdc++.so.6
2024-04-27 21:25:08: minidump.cc:2704: INFO: MinidumpModule could not determine version for /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
2024-04-27 21:25:08: minidump.cc:2704: INFO: MinidumpModule could not determine version for linux-gate.so
2024-04-27 21:25:08: minidump.cc:2704: INFO: MinidumpModule could not determine version for /home/ubuntu/ckp/crash
2024-04-27 21:25:08: minidump.cc:2704: INFO: MinidumpModule could not determine version for /usr/lib/x86_64-linux-gnu/libm.so.6
2024-04-27 21:25:08: minidump.cc:2704: INFO: MinidumpModule could not determine version for /usr/lib/x86_64-linux-gnu/libc.so.6
2024-04-27 21:25:08: minidump.cc:2704: INFO: MinidumpModule could not determine version for /usr/lib/x86_64-linux-gnu/libgcc_s.so.1
2024-04-27 21:25:08: minidump.cc:2704: INFO: MinidumpModule could not determine version for /usr/lib/x86_64-linux-gnu/libstdc++.so.6
2024-04-27 21:25:08: minidump.cc:2704: INFO: MinidumpModule could not determine version for /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
2024-04-27 21:25:08: minidump.cc:2704: INFO: MinidumpModule could not determine version for linux-gate.so
2024-04-27 21:25:08: minidump.cc:6474: INFO: GetStream: type 14 not present
2024-04-27 21:25:08: minidump_processor.cc:187: INFO: Found 2 memory regions.
2024-04-27 21:25:08: minidump_processor.cc:197: INFO: Minidump /tmp/98dcf79a-ae80-4820-eedf95b2-309c0cff.dmp has CPU info, OS info, no Breakpad info, exception, module list, thread list, no dump thread, requesting thread, and no process create time
2024-04-27 21:25:08: minidump.cc:6474: INFO: GetStream: type 24 not present
2024-04-27 21:25:08: minidump_processor.cc:266: INFO: Looking at thread /tmp/98dcf79a-ae80-4820-eedf95b2-309c0cff.dmp:0/1 id 0x239c
2024-04-27 21:25:08: minidump.cc:508: INFO: MinidumpContext: looks like AMD64 context
2024-04-27 21:25:08: minidump.cc:508: INFO: MinidumpContext: looks like AMD64 context
2024-04-27 21:25:08: source_line_resolver_base.cc:244: INFO: Loading symbols for module /home/ubuntu/ckp/crash from memory buffer, size: 172537
2024-04-27 21:25:08: simple_symbol_supplier.cc:199: INFO: No symbol file at ./symbols//libc.so.6/AA152096139D6C3CBCFB31EC300596D70/libc.so.6.sym
2024-04-27 21:25:08: stackwalker.cc:108: INFO: Couldn't load symbols for: /usr/lib/x86_64-linux-gnu/libc.so.6|AA152096139D6C3CBCFB31EC300596D70
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0xffffffffffffffff
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0xffffffff
2024-04-27 21:25:08: minidump.cc:1605: INFO: MinidumpMemoryRegion request out of range: 0x5590e6de0090+8/0x7fff51cde000+0x3000
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51cde647
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0xffffffffffffffff
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7bb249a4d579a550
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51cde647
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x5590e6df8a0f
2024-04-27 21:25:08: minidump.cc:1605: INFO: MinidumpMemoryRegion request out of range: 0x5590e6de0090+8/0x7fff51cde000+0x3000
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7f72a683c03f
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x844cea3f1ffba550
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x855705d10ff3a550
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0xffffffffffffffff
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0xffffffffffffffff
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0xffffffffffffffff
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0xffffffffffffffff
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0xffffffffffffffff
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0xab8ed8cea41a8ff
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0xffffffffffffffff
2024-04-27 21:25:08: minidump.cc:1605: INFO: MinidumpMemoryRegion request out of range: 0x5590e6de0090+8/0x7fff51cde000+0x3000
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51cde657
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x5590e6df8a0f
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7f72a683d2df
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0xffffffffffffffff
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0xffffffffffffffff
2024-04-27 21:25:08: minidump.cc:1605: INFO: MinidumpMemoryRegion request out of range: 0x5590e6de0090+8/0x7fff51cde000+0x3000
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51cde63f
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0xffffffffffffffff
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0xffffffffffffffff
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51cde637
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x1b
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x0
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce076c
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0xffffffffffffffff
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce0774
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce0784
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce0799
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce07a8
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce07bd
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce07cc
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce07de
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce07eb
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce0dda
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce0e0c
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce0e2e
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce0e45
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce0e59
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce0e79
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce0e85
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce0e8d
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce0e9f
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce0ebe
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce0edf
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce0f20
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce0f88
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce0fbe
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce0fd1
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51ce0fe5
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0xffffffffffffffff
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x20
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x7fff51d93fff
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x32
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x6ef
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0xf
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0xf8bfbfe
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x5
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0xfff
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x10
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x63
2024-04-27 21:25:08: basic_code_modules.cc:114: INFO: No module at 0x2
2024-04-27 21:25:08: minidump_processor.cc:391: INFO: Processed /tmp/98dcf79a-ae80-4820-eedf95b2-309c0cff.dmp
Operating system: Linux
                  0.0.0 Linux 5.15.0-102-generic #112-Ubuntu SMP Tue Mar 5 16:50:32 UTC 2024 x86_64
CPU: amd64
     family 6 model 158 stepping 10
     1 CPU
GPU: UNKNOWN
Crash reason:  SIGSEGV /SEGV_MAPERR
Crash address: 0x0
Process uptime: not available
Thread 0 (crashed)
 0  crash!crash_function1() [testapp.cpp : 16 + 0x4]
    rax = 0x0000000000000000   rdx = 0x0000000000000001
    rcx = 0x00007f72a6499887   rbx = 0x0000000000000000
    rsi = 0x0000000000000001   rdi = 0x00007f72a65a1a70
    rbp = 0x00007fff51cde380   rsp = 0x00007fff51cde380
     r8 = 0x0000000000000000    r9 = 0x00005590e8546fa0
    r10 = 0x0000000000000077   r11 = 0x0000000000000246
    r12 = 0x00007fff51cde648   r13 = 0x00005590e6de0088
    r14 = 0x00005590e6df8a10   r15 = 0x00007f72a683c040
    rip = 0x00005590e6de007f
    Found by: given as instruction pointer in context
 1  crash!main [testapp.cpp : 27 + 0x5]
    rbx = 0x0000000000000000   rbp = 0x00007fff51cde530
    rsp = 0x00007fff51cde390   r12 = 0x00007fff51cde648
    r13 = 0x00005590e6de0088   r14 = 0x00005590e6df8a10
    r15 = 0x00007f72a683c040   rip = 0x00005590e6de015c
    Found by: call frame info
 2  libc.so.6 + 0x29d90
    rbx = 0x0000000000000000   rbp = 0x0000000000000001
    rsp = 0x00007fff51cde540   r12 = 0x00007fff51cde648
    r13 = 0x00005590e6de0088   r14 = 0x00005590e6df8a10
    r15 = 0x00007f72a683c040   rip = 0x00007f72a63aed90
    Found by: call frame info
 3  crash!crash_function1() [testapp.cpp : 17 + 0x3]
    rsp = 0x00007fff51cde550   rip = 0x00005590e6de0088
    Found by: stack scanning
 4  0x100000000
    rbp = 0x00005590e6de0088   rsp = 0x00007fff51cde558
    rip = 0x0000000100000000
    Found by: call frame info
 5  crash!crash_function1() [testapp.cpp : 17 + 0x3]
    rsp = 0x00007fff51cde580   rip = 0x00005590e6de0088
    Found by: stack scanning
 6  0x5590e6df8a10
    rbp = 0x00005590e6de0088   rsp = 0x00007fff51cde588
    rip = 0x00005590e6df8a10
    Found by: call frame info
 7  libc.so.6 + 0x29e40
    rsp = 0x00007fff51cde5e0   rip = 0x00007f72a63aee40
    Found by: stack scanning
 8  crash!google_breakpad::ConvertUTF8toUTF32(unsigned char const**, unsigned char const*, unsigned long**, unsigned long*, google_breakpad::ConversionFlags) [clone .cold] + 0xd
    rsp = 0x00007fff51cde610   rip = 0x00005590e6ddff40
    Found by: stack scanning
 9  crash!_start + 0x25
    rsp = 0x00007fff51cde630   rip = 0x00005590e6ddff65
    Found by: stack scanning
10  0x7fff51cde638
    rsp = 0x00007fff51cde638   rip = 0x00007fff51cde638
    Found by: call frame info
Loaded modules:
0x5590e6ddc000 - 0x5590e6df1fff  crash  ???  (main)
0x7f72a629e000 - 0x7f72a6327fff  libm.so.6  ???
0x7f72a6385000 - 0x7f72a6541fff  libc.so.6  ???  (WARNING: No symbols, libc.so.6, AA152096139D6C3CBCFB31EC300596D70)
0x7f72a65ae000 - 0x7f72a65c7fff  libgcc_s.so.1  ???
0x7f72a65ce000 - 0x7f72a6778fff  libstdc++.so.6  ???
0x7f72a6802000 - 0x7f72a682dfff  ld-linux-x86-64.so.2  ???
0x7fff51d94000 - 0x7fff51d95fff  linux-gate.so  ???
2024-04-27 21:25:08: minidump.cc:5584: INFO: Minidump closing minidump
