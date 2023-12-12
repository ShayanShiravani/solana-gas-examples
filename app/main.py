from solana.transaction import Transaction
from solana.rpc.api import Client
from solana.exceptions import SolanaExceptionBase
from solana.rpc.core import RPCException
from anchor_client.instructions import *
from utils import Utils
from dotenv import load_dotenv

load_dotenv()

RPC_URL = "http://localhost:8899"

rpc_client = Client(RPC_URL)

signer = Utils.get_local_wallet()

init = initialize({
    "payer": signer.pubkey()
})
bitwiseOperation = bitwise_operation(
    {"input": 11111111111111}
)
sumOfNaturalNumbers = sum_of_natural_numbers(
    {"end": 8}
)
isPrime = is_prime(
    {"number": 24}
)
nthPrime = nth_prime(
    {"n": 10}
)
fib = fibonacci(
    {"n": 19}
)

txn = Transaction().add(init)
txn.add(bitwiseOperation)
txn.add(sumOfNaturalNumbers)
txn.add(isPrime)
txn.add(nthPrime)
txn.add(fib)

try:
    rpc_client.send_transaction(txn, signer)
except SolanaExceptionBase as exc:
    print(exc.error_msg)
except RPCException as exc:
    print(exc)
