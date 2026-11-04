with open("source/main.cpp", "rb") as f:
    content = f.read().decode("utf-8")

# 1. Add AsyncSaveManager::processQueue(); after chunkManager->update
old_update = "{ PROF(Prof::UPDATE); chunkManager->update(player->x, player->z, ldx, ldz); }"
new_update = "{ PROF(Prof::UPDATE); chunkManager->update(player->x, player->z, ldx, ldz); }\r\n        AsyncSaveManager::processQueue();"

if old_update in content:
    content = content.replace(old_update, new_update, 1)
    print("Added AsyncSaveManager::processQueue() to main loop")
else:
    print("Warning: old_update not found")

# 2. Add AsyncSaveManager::flushAll() before delete chunkManager
old_del = "delete chunkManager;"
new_del = "AsyncSaveManager::flushAll();\r\n        delete chunkManager;"

# Replace first 2 occurrences of delete chunkManager
content = content.replace(old_del, new_del)
print("Added AsyncSaveManager::flushAll() before delete chunkManager")

with open("source/main.cpp", "wb") as f:
    f.write(content.encode("utf-8"))

