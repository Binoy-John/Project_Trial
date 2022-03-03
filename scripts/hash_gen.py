from web3 import Web3
import math

voters = [
    "0xa4385CC927b157eD4c333626FDCCd1F8eDC00a03",
    "0x185Cc7E6cE0328EE2A7BdBCf7305741d09B546D5",
    "0x24C227E7b1A952A70101496a7C3F4628f9D134E6",
    "0x8A326a3F4E397a5f0f5E2A26D6F442f875B5D16E",
    "0x025C966aD1f6Ba23A9109611714E74D6A3bE8899",
    "0x10Bf077d4Ccb1177C1cf29f5f9E1ED205D390763",
    "0x58B5ddb932C871c74D9Fd4414D1c1B40d499B86B",
    "0x7343E1d41c888Fc56Eb13a5A14E0d41334dC963C",
    "0x837C3179A9F5f29cdb17069015541B287E75f638",
]


def get_index(voters_list, verify_voter):
    for i in range(len(voters_list)):
        if verify_voter == voters_list[i]:
            return i
    return -1


def calc_merkle_from_proof(proof, leaf, index):
    hash = leaf
    for i in range(0, len(proof)):
        proof_element = proof[i]
        print(f"proof element is {proof_element}")
        print(f"hash is {hash.hex()}")

        if index % 2 == 0:
            print(f"hashing {hash.hex()} and {proof_element}")
            hash = Web3.solidityKeccak(
                ["bytes32", "bytes32"], [hash.hex(), proof_element]
            )
            print(f"appended {hash.hex()}")

        else:
            print(f"hashing {proof_element} and {hash.hex()}")
            hash = Web3.solidityKeccak(
                ["bytes32", "bytes32"], [proof_element, hash.hex()]
            )
            print(f"appended {hash.hex()}")

        index = math.floor(index / 2)

    return hash


def get_merkle_root(merkle_list):
    return merkle_list[-1]


def get_merkle_list(voters):
    print("==============initiating creation of tree===============")
    offset = 0
    voters_length = len(voters)
    print("length of voter is", voters_length)
    print("offset is ", offset)
    merkle_list = []

    for i in range(voters_length):
        merkle_list.append(Web3.toHex(voters[i]))

    print("=============Added the initial list of addresses============")

    while voters_length > 0:

        print("===============Creating a new level==================")

        for i in range(0, voters_length - 1, 2):
            last = voters_length + offset

            print(
                f"===============hashing {merkle_list[offset + i]} at index {offset+i} and {merkle_list[offset + i + 1]} at index {offset+i+1} together============"
            )
            merkle_list.append(
                Web3.toHex(
                    Web3.solidityKeccak(
                        ["bytes32", "bytes32"],
                        [
                            merkle_list[offset + i],
                            merkle_list[offset + i + 1],
                        ],
                    )
                )
            )

            print("+++++++++++++++Added element in the current level++++++++++++++++++")
        if voters_length % 2 != 0 and voters_length != 1:
            print(
                f"===============hashing {merkle_list[last - 1]} at index {last-1} and {merkle_list[last - 1]} at index {last-1} together============"
            )
            merkle_list.append(
                Web3.toHex(
                    Web3.solidityKeccak(
                        ["bytes32", "bytes32"],
                        [
                            (merkle_list[last - 1]),
                            (merkle_list[last - 1]),
                        ],
                    )
                )
            )

            print(
                "+++++++++++++++Added element in the current level using duplicate++++++++++++"
            )
        offset += voters_length
        print("offset updated to ", offset)
        if voters_length % 2 != 0 and voters_length != 1:
            voters_length = math.ceil((voters_length) / 2)
        else:
            voters_length = int(voters_length / 2)

        print("voters length updated to ", voters_length)

    return merkle_list


def generate_proof_list_index(l):
    first_no = 0
    f = 0
    second_no = 1
    offset = 2
    columns = math.ceil(math.log(l, 2))
    PL = []
    for i in range(l):
        PL.insert(0, [])
    # print("==================Created empty list==================")

    for i in range(0, columns):
        # print(PL)
        # print("================Creating new Column==============")
        first_claw = 0
        last_claw = (offset) - 1
        rows = 0
        flag = 0
        while True:
            mid = math.ceil((last_claw + first_claw) / 2)
            while first_claw < mid:
                PL[first_claw].append(second_no)
                first_claw += 1
                rows += 1

            while mid <= last_claw and mid < l:
                PL[mid].append(first_no)
                mid += 1
                rows += 1

            first_no += 2
            second_no += 2
            first_claw = last_claw + 1
            last_claw += offset
            if last_claw >= l:
                break

        while rows < l:
            PL[rows].append(first_no)
            flag = 1
            rows += 1
        if flag == 1:
            first_no += 1
            second_no += 1
        offset *= 2

    return PL


# to verify: 0x58B5ddb932C871c74D9Fd4414D1c1B40d499B86B


def main():
    verify_voter_id = "0x58B5ddb932C871c74D9Fd4414D1c1B40d499B86B"
    voter_index = -1
    voters_hashed = []
    for i in range(len(voters)):
        voters_hashed.append(Web3.solidityKeccak(["address"], [str(voters[i])]))

    merkle_list = get_merkle_list(voters_hashed)
    merkle_root = get_merkle_root(merkle_list)

    for i in range(len(merkle_list)):
        print(merkle_list[i])

    proof_list_index = generate_proof_list_index(len(voters))
    # print(proof_list_index)
    id_index = get_index(voters, verify_voter_id)
    print("voter found at index ", id_index)
    proof_list_index = proof_list_index[id_index]
    print("The indexes of the proof is ", proof_list_index)
    proof_list = []
    for i in proof_list_index:
        proof_list.append(merkle_list[i])
    # print(proof_list)

    print("voter hash from the hashed array is ", Web3.toHex(voters_hashed[id_index]))
    print(
        "voter hash from calculated is ",
        Web3.toHex(Web3.solidityKeccak(["address"], [verify_voter_id])),
    )
    hash = calc_merkle_from_proof(
        proof_list,
        Web3.solidityKeccak(["bytes32"], [verify_voter_id]),
        id_index,
    )
    print("The merkle root is", (merkle_root))
    print("Hash from the proof function is", (hash).hex())
    # print("-------------------------test------------------------------")
    # print(proof_list)
    # print(id_index)
    # print(Web3.solidityKeccak(["bytes32"], [verify_voter_id]).hex())
