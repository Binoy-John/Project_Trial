# from tkinter import N
# from web3 import Web3
# from brownie import accounts
# from hexbytes import HexBytes

# voters = [
#     "0xa4385CC927b157eD4c333626FDCCd1F8eDC00a03",
#     "0x185Cc7E6cE0328EE2A7BdBCf7305741d09B546D5",
#     "0x24C227E7b1A952A70101496a7C3F4628f9D134E6",
#     "0x8A326a3F4E397a5f0f5E2A26D6F442f875B5D16E",
#     "0x025C966aD1f6Ba23A9109611714E74D6A3bE8899",
#     "0x10Bf077d4Ccb1177C1cf29f5f9E1ED205D390763",
#     "0x58B5ddb932C871c74D9Fd4414D1c1B40d499B86B",
#     "0x7343E1d41c888Fc56Eb13a5A14E0d41334dC963C",
#     "0x92A89b745A933F1fB4e45d4a4E234B342b61cebD",
# ]
# merkel_list = []


# def main():

#     voters_hashed = []
#     for i in range(len(voters)):
#         voters_hashed.append([Web3.solidityKeccak(["address"], [str(voters[i])])])

#     voters_hashed_hashed = []

#     for i in range(len(voters_hashed)):
#         print(i)
#         hb = voters_hashed[i][0]
#         print(hb)
#         print(type(hb))
#         hb = hb.hex()
#         voters_hashed_hashed.append(Web3.solidityKeccak(["bytes32"], [hb]))
