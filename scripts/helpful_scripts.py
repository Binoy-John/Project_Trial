# from brownie import network, accounts, config, Contract, merkle_proof_verifier


# FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
# LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


# def get_account(index=None, id=None):
#     # these are the ways to add an account:
#     # accounts[0]
#     # accounts.add("env")
#     # accounts.load("id")
#     if index:
#         return accounts[index]
#     if id:
#         return accounts.load(id)

#     if (
#         network.show_active() in FORKED_LOCAL_ENVIRONMENTS
#         or network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
#     ):
#         print("The active network found is : ", network.show_active())
#         return accounts[0]
#     return accounts.add(config["wallets"]["from_key"])
