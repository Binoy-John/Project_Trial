// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract merkle_proof_verifier {
    function getHash(
        bytes32[] memory proof_list,
        bytes32 leaf,
        uint256 index
    ) public pure returns (bytes32) {
        bytes32 hash = leaf;
        for (uint256 i = 0; i < proof_list.length; i++) {
            bytes32 proof_element = proof_list[i];
            if (index % 2 == 0) {
                hash = keccak256(abi.encodePacked(hash, proof_element));
            } else {
                hash = keccak256(abi.encodePacked(proof_element, hash));
            }
            index = index / 2;
        }

        return hash;
    }

    // function test_length(bytes32[] memory proof_list)public pure returns (uint256){
    //     return proof_list.length;
    // }
}
