with open("source/AsyncSaveManager.h", "r", encoding="utf-8") as f:
    h_content = f.read()

# Replace declaration of startSaveSession and add notifyAllEnqueued
old_h_decl = """    // Estado del volcado seguro para la UI
    static void startSaveSession(int totalTasks);
    static int getTotalTasks();"""

new_h_decl = """    // Estado del volcado seguro para la UI
    static void startSaveSession(int totalTasks);
    static void notifyAllEnqueued(int totalActual = -1);
    static int getTotalTasks();"""

assert old_h_decl in h_content, "old_h_decl not found"
h_content = h_content.replace(old_h_decl, new_h_decl)

# Add s_allEnqueued private member
old_h_priv = """    static bool s_sessionActive;
    static bool s_sessionSuccess;"""

new_h_priv = """    static bool s_sessionActive;
    static bool s_sessionSuccess;
    static bool s_allEnqueued;"""

assert old_h_priv in h_content, "old_h_priv not found"
h_content = h_content.replace(old_h_priv, new_h_priv)

with open("source/AsyncSaveManager.h", "w", encoding="utf-8", newline="\n") as f:
    f.write(h_content)

print("source/AsyncSaveManager.h updated successfully")

