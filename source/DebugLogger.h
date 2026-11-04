#ifndef DEBUG_LOGGER_H
#define DEBUG_LOGGER_H

#include <nds.h>
#include <stdio.h>
#include <stdarg.h>

class DebugLogger {
public:
    static const int MAX_HISTORY = 8;
    static const int LINE_LEN = 128;

    static void init();
    static void log(const char* fmt, ...);
    static int getLineCount();
    static const char* getLine(int idx);
    static void drawBottomScreen();

private:
    static char s_history[MAX_HISTORY][LINE_LEN];
    static int s_head;
    static int s_count;
    static bool s_initialized;
    static FILE* s_logFile;
};

#endif // DEBUG_LOGGER_H
