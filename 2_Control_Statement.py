for i in range(10):
    print(i)
    if i==4:
        break

for i in range(10):
    if i==4:
        continue
    print(i)

for i in range(10):
    if i==4:
        pass

import os
print('You are in : ', os.getcwd())#show where you located