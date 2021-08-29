# Desenvolvido e implementado em ambiente Linux
# Miguel Sanches Rocha
# 11811BCC001

from web3 import Web3

def balance(address, web3):
    result = web3.eth.getBalance(address)
    print("This account has:",web3.fromWei(result, "ether"))
    return


def main():
    # My mainnet infura address
    infura_url = "https://mainnet.infura.io/v3/23328a89a7ec409eadfb15c7a9b39935"
    web3 = Web3(Web3.HTTPProvider(infura_url))
    print("Is it connected to main net?: ",web3.isConnected())
    print("The latest block number is: ",web3.eth.blockNumber)
    address = input("Enter with an address: ")
    balance(address, web3)
    return

if __name__ == '__main__':
   main()