import time
s=int(time.time())
a=((s//60)//60)
print(1970+(a//24)//365,"년",(a%24)+9,"시",(s//60)%60,"분",s%60,"초")
