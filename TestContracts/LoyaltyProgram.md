# Demo and test of a base smart contract for a Loyalty Program using Remix IDE. 

You'll need to have either test Metis (on Sepolia), or real Metis tokens (on Andromeda) in order to deploy.


[Here's a short tutorial on how to get Metis test tokens](https://twitter.com/Quantic___/status/1788536128464650581)

### Step 1: Preparing the Environment in Remix

1. **Open Remix**: Go to [Remix Ethereum IDE](https://remix.ethereum.org) in your browser. Remix is a powerful, browser-based development environment.
2. **Create a New File**: In the 'File Explorers' tab, create a new file by clicking on the "Create New File" icon. Name it, for example, `LoyaltyProgram.sol`.
3. **Paste the Contract Code**: Copy the LoyaltyProgram contract code provided previously into this new file.

### Step 2: Creating the Smart Contract

Here’s the `LoyaltyProgram.sol` contract :

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract LoyaltyProgram {
    mapping(address => uint256) public balances;
    address public owner;

    event PointsIssued(address indexed to, uint256 amount);
    event PointsTransferred(address indexed from, address indexed to, uint256 amount);
    event PointsRedeemed(address indexed by, uint256 amount);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can issue points");
        _;
    }

    function issuePoints(address to, uint256 amount) public onlyOwner {
        require(to != address(0), "Cannot issue points to the zero address");
        balances[to] += amount;
        emit PointsIssued(to, amount);
    }

    function transferPoints(address to, uint256 amount) public {
        require(to != address(0), "Cannot transfer points to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance to transfer points");
        balances[msg.sender] -= amount;
        balances[to] += amount;
        emit PointsTransferred(msg.sender, to, amount);
    }

    function redeemPoints(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient points to redeem");
        balances[msg.sender] -= amount;
        emit PointsRedeemed(msg.sender, amount);
    }
}
```

### Step 3: Compiling the Contract

1. **Go to the Solidity Compiler**: Click on the 'Solidity Compiler' tab in Remix.
2. **Select Compiler Version**: Make sure the compiler version matches the version declared in your contract (`^0.8.0`). If not, adjust it accordingly.
3. **Compile**: Click the "Compile" button. 

_____________
** Note: Make sure to use the Berlin EVM version to avoid any potential issues with deployment. **
_____________

### Step 4: Deploying the Contract

1. **Switch to the Deploy Tab**: Click on the 'Deploy & run transactions' tab.
2. **Environment Selection**: From the "Environment" dropdown, choose "Injected Web3" which allows you to use MetaMask or other Web3 providers.
3. **Connect Your Wallet**: Ensure your MetaMask or another wallet is connected to the network you intend to deploy on (like Metis L2 testnet).
4. **Deploy**: Click on "Deploy" to send the contract to the blockchain. Confirm the transaction in your wallet.

### Step 5: Interacting with the Contract

Once deployed:
- You can interact with the contract functions directly from the "Deployed Contracts" section in Remix.
- Use the functions like `issuePoints`, `transferPoints`, and `redeemPoints` by providing necessary arguments and clicking the respective buttons.

### Step 6: Testing Script

Here is a simple script to test your contract functionalities using JavaScript in Remix:

```javascript
(async () => {
    try {
        const accounts = await web3.eth.getAccounts();
        const loyalty = new web3.eth.Contract(abi, contractAddress); // Replace 'abi' and 'contractAddress' with actual values

        // Issue points to account[1]
        await loyalty.methods.issuePoints(accounts[1], 1000).send({from: accounts[0]});
        console.log(`Points issued to account[1]: 1000`);

        // Transfer points from account[1] to account[2]
        await loyalty.methods.transferPoints(accounts[2], 500).send({from: accounts[1]});
        console.log(`500 points transferred from account[1] to account[2]`);

        // Redeem points for account[2]
        await loyalty.methods.redeemPoints(200).send({from: accounts[2]});
        console.log(`200 points redeemed by account[2]`);
    } catch (error) {
        console.error("Error in executing transactions", error);
    }
})();
```

- Check and interact with all the deployed functions to make sure they work as expected.
