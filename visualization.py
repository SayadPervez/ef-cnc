# FOR SHYAM
import sys

def RUN(param):
    print(param)

if(len(sys.argv)==2):
    RUN(sys.argv[1])
else:
    print('failed')