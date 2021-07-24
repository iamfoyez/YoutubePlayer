import os
import sys

os.system("javac *.java")
os.system("java " + sys.argv[1])
os.system("rm *.class")