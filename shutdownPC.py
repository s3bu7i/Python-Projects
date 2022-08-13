
  
from logging import shutdown
import os

shutdown=input("Shutdown you PC ?(Yes/No):")

if shutdown == 'no':
    exit()
else:
    os.system("shutdown/s/t1")
    
  
  
        
