# This module contain different blockchain request type
# E.g connect.eth.get_balance(address) this get the ETH balnce of the address specified

from web3 import *
import time
import telegram,asyncio
import random

class requesting:
    
    addresses = ['0x532cbA28923AB09E527C4323C8E0A8eD73865376','0x77E3DaE164c3145452B81F5aFfb2e8c6f0a226C9','0x20f8Dd24C933ea9FBc247Db7Dc835654A0051Af6','0x8f0058C81a57673B3eb7DCBb489fAF687e489d4f','0x275aa46F74Cf1485282e0B4FFd63d7CC40bC8AE4','0x7afc85B0AFb51Eb639b1F8c08CA91a7d32013e96','0x37D11fAD5FC57562eb12b7c575958C9a2Bcf843C','0x56bb696e2F3c9864f7b3f3420E4d55a3183E75fA','0x033FFcf5d843a16da224F62B5CB1c4980310F796','0x1ECC0663aa9B7ffDbfA30c35dB336D75C959c2eC','0x9c69Cc30Ee62B0A629d524dE2188DB823323DC01','0x63EdCF4fBD5B821C14B3A5383f7E5469A69FE2b6','0xBA1B6D916b7Be7f1f6936A55f7ceDd09A2a2B64D','0x39B96101e8c273caE0e3153c262B76687131f3B3',]    
    hashes = ['0x46eb63632b52893d5893c34fb259137b42bdc868debad4a84d919289f395fcf7','0xed32da064a43eae8fed2d93ddc5e2c3b8bf596788222fc3959e8e9174160fb03','0x49058807b30771c9edfba5f118599ce6cc2ecbee51c7c82bc3c5f3cc9c2c34d2','0x981cddfcf6ee65a0021bf71c05db2f97ba083b7ca5de45ece158bfcdf6b41edd','0xfdbe111ae767d58f6700584c102ebc5fdf4120b5bbe014ae4e1e39d7bea3ab04','0x9504924533ccd3daf6ec5dbb409fd27ee155612dd23f11f963e912332eb02db9','0x1fa0adadc8d6e26c41bfceb0a1f59fe9ba29f82eb594ec4b959589046eb15e27','0xc35396aaf5eeec9e435833338e0374d171b9ef2e2042ebef3aba4e44a50106e0','0x7e29d7544e78be39366a1a0528fc8ed4ed0a50c5e88d19ccb80df3c7cfb66085','0x513964c9d319a835994922adbf374c278668a4f76b23d66747fecdd395433c8c','0x898e82333c3833a2ef8f1ed4dfa89b75d3d0b65a84808dd9e3a9767724ddd726','0x01cadbe2f40062ca6bc4deaddf1276411c9faaab44416786f85cc8cc05b61695','0xe1d9505b6a34187a63a5446fed35d30cdb7a736d1af8b4f339495089cf0418e7','0x78917a37a5b18929c2a7ff2ab0e5b76f5ac6c12dcfd26e07a2abf7c0c80d61aa','0x95190f7499440a9107187038099945fd2c2cfd9846ffb008cc4d28697cf9de10','0x7e29d7544e78be39366a1a0528fc8ed4ed0a50c5e88d19ccb80df3c7cfb66085','0x01cadbe2f40062ca6bc4deaddf1276411c9faaab44416786f85cc8cc05b61695','0x7e29d7544e78be39366a1a0528fc8ed4ed0a50c5e88d19ccb80df3c7cfb66085']

    def __init__(self,RPC:str) -> None:
        self.connect = Web3(Web3.HTTPProvider(RPC))

    def differntRequets(self,task):
        
        if task == 'task1' or task == 'task6':
            # Getting balnce of an address
            for i in range(3):
                address = random.choice(self.addresses)
                try:
                    balance = self.connect.eth.get_balance(address)
                    print("Balance of", address, "is:", self.connect.from_wei(balance, 'ether'), "ETH")
                except:
                    time.sleep(7)
                    balance = self.connect.eth.get_balance(address)
                    print("Balance of", address, "is:", self.connect.from_wei(balance, 'ether'), "ETH")
                time.sleep(3)


            # Request the latest block number
            for i in range(3):
                blockNumber = self.connect.eth.block_number
                time.sleep(1)
                print("Latest Block Number:", blockNumber)
                try:
                    blockData =  self.connect.eth.get_block(blockNumber,True)
                    print('Blockdata Successfully Retrieved')
                except:
                    time.sleep(7)
                    blockData =  self.connect.eth.get_block(blockNumber,True)
                    print('Blockdata Successfully Retrieved')
                time.sleep(3)


        if task == 'task2' or task == 'task5':
            # Get transaction count
            addresses = random.sample(self.addresses,3)
            for address in addresses:
                try:
                    transaction_count = self.connect.eth.get_transaction_count(address)
                    print("Transaction count of", address, "is:", transaction_count)
                except:
                    time.sleep(7)
                    transaction_count = self.connect.eth.get_transaction_count(address)
                    print("Transaction count of", address, "is:", transaction_count)
                time.sleep(3)

            # Get transaction by hash
            txHash = random.sample(self.hashes,3)
            for hash in txHash:
                try:
                    transaction = self.connect.eth.get_transaction(hash)
                    print("Transactions Requested")
                except:
                    time.sleep(7)
                    transaction = self.connect.eth.get_transaction(hash)
                    print("Transactions Requested")
                time.sleep(3) 

        if task == 'task3' or task == 'task4':

            # Geting transactioon Reciept
            txHash = random.sample(self.hashes,4)
            for hash in txHash:
                try:
                    receipt = self.connect.eth.get_transaction_receipt(hash)
                    print("Transaction Receipt Requested", )
                except:
                    time.sleep(7)
                    receipt = self.connect.eth.get_transaction_receipt(hash)
                    print("Transaction Receipt Requested", )
                time.sleep(3)


            # Esitmating gas price
            for address in random.sample(self.addresses,2):
                try:
                    block = self.connect.eth.get_block('latest')
                    baseFee = block['baseFeePerGas']*2
                    transaction = {
                        'type': '0x2',
                        'chainId': self.connect.eth.chain_id,
                        'from': random.choice(self.addresses),
                        'to': address,
                        'gas': 25000,
                        'value': self.connect.to_wei(0.002,'ether'),
                        'maxFeePerGas': baseFee ,
                        'maxPriorityFeePerGas': Web3.to_wei(2, 'gwei'),
                        'nonce':self.connect.eth.get_transaction_count(address)
                    }

                    estimate =  self.connect.eth.estimate_gas(transaction)
                    print(f'The Estimated Gas Is {estimate}')
                except:
                    time.sleep(10)
                    block = self.connect.eth.get_block('latest')
                    baseFee = block['baseFeePerGas']*2
                    transaction = {
                        'type': '0x2',
                        'chainId': self.connect.eth.chain_id,
                        'from': random.choice(self.addresses),
                        'to': address,
                        'gas': 25000,
                        'value': self.connect.to_wei(0.002,'ether'),
                        'maxFeePerGas': baseFee ,
                        'maxPriorityFeePerGas': Web3.to_wei(2, 'gwei'),
                        'nonce':self.connect.eth.get_transaction_count(address)
                    }

                    estimate =  self.connect.eth.estimate_gas(transaction)
                    print(f'The Estimated Gas Is {estimate}')
                time.sleep(5)
                
# Alert    
class RequestAlert:    
    def Alert(self):
        bot_token = '6743591728:AAGIuYYXKG8Wk8yeZ_pX2GY_fGNCissNP3Q'
        async def main():
            try:
                bot =  telegram.Bot(bot_token)
            except:
                bot = telegram.Bot(bot_token)
            async with bot:
                await bot.send_message(text=f'All (RPC) Request Completed For All Accounts',chat_id=5699580294)
        if __name__ != '__main__':
            asyncio.run(main())

