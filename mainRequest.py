from web3 import *
import time
import random
from requestClass import requesting,RequestAlert

# Paste your different Rpc here
RPC_1 = 'https://eth1.lava.build/lava-referer-cc9e5c72-63b2-4cb2-a184-2da02275e79f/' #  vxlt
RPC_2 = 'https://eth1.lava.build/lava-referer-bb51f107-9227-4755-afbc-5eac2d67b731/' # X37

RPC_3 = 'https://eth1.lava.build/lava-referer-cc9e5c72-63b2-4cb2-a184-2da02275e79f/'
# RPC_3 = 'https://eth1.lava.build/lava-referer-80954d5b-d806-40d6-a5f3-d7f6c52995ae/'

RPC_4 = 'https://eth1.lava.build/lava-referer-cc9e5c72-63b2-4cb2-a184-2da02275e79f/'
# RPC_4 = 'https://eth1.lava.build/lava-referer-e5e7adad-d677-4580-806d-bd2d2e3dd67e/'

RPC_5 = 'https://eth1.lava.build/lava-referer-cc9e5c72-63b2-4cb2-a184-2da02275e79f/'
# RPC_5 = 'https://eth1.lava.build/lava-referer-85290b4d-eb65-40d4-816b-a998caa660f4/'

RPC_6 = 'https://eth1.lava.build/lava-referer-bcaf1744-0d7b-46b8-a081-fa27b794238a/'


requestTasks = [ 'task1','task2' 'task3','task4','task5','task6']
ENDPOINT = [ RPC_1,RPC_2,RPC_3,RPC_4,RPC_5,RPC_6 ]

def main():
    for index, RPC_KEY in enumerate(ENDPOINT):
        print(f'Requesting to the {index} RPC')
        processor = requesting(RPC_KEY)
        task = random.choice(requestTasks)
        try:
            processor.differntRequets(task)
        except Exception as e:
            print(f'The Error Is From {e}')
            pass


processor = RequestAlert()
request = True
try:
    main()
    print('Done requesting')
    processor.Alert()
except Exception as e:
    print(f'Thi issue is from {e}')
    processor.failed()

