import shutil
shutil.copy("day63.py","day64.py")#copies a file to a destination

shutil.copy2("day63.py","day64.py")#copies a file along with metadata (timestamps, permissions,)

shutil.copytree(".data","mydata")#recursively copies an entire directory tree.

shutil.move(".data/bler2", "bler1")#moves a file or directory.
shutil.rmtree("mydata")#recursively deletes a directory tree. Use with caution!+
