# aio_coind

This is an asynchronous library for working with cryptocurrency daemons.

Here is an example usage:
```python
import asyncio
from pprint import pprint

from aio_coind import CoindSession, CoindError


async def main():
    try:
        # Create an instance of CoindSession with authentication credentials
        async with CoindSession(
                "rpc_username",
                "rpc_password",
                "rpc_port",
                "rpc_host") as coind:
            # Call the getblockchaininfo method
            blockchain_info = await coind.blockchain.get_blockchain_info()
            pprint(blockchain_info)

            # Perform other operations with coind
    except CoindError as e:
        print('Coind Error:', e.code, e.msg)


# Run the asynchronous main() function
asyncio.run(main())

```

In this example, we import the necessary modules and classes for working with a cryptocurrency daemon. 
We create an instance of the CoindSession class, passing the required authentication data (RPC username, RPC password, RPC port, and RPC host). Within the main() function, we use the async with statement to establish a connection to the cryptocurrency daemon. We then call the get_blockchain_info() method to retrieve information about the blockchain and print the result using pprint. Additional operations with the coind instance can be performed as needed. If an error occurs during the execution, a CoindError will be raised and handled in the except block. The main() function is run using asyncio.run() to start the asynchronous event loop.

