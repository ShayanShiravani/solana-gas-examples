from solana.transaction import Transaction
from solana.rpc.api import Client
from solana.exceptions import SolanaExceptionBase
from solana.rpc.core import RPCException
from anchor_client.instructions import *
from utils import Utils

RPC_URL = "http://localhost:8899"

rpc_client = Client(RPC_URL)

signer = Utils.get_local_wallet()

init = initialize({
    "payer": signer.pubkey()
})
bitwiseOperation = bitwise_operation(
    {"input": 11111111111111},
    {"payer": signer.pubkey()}
)
sumOfNaturalNumbers = sum_of_natural_numbers(
    {"end": 8},
    {"payer": signer.pubkey()}
)
isPrime = is_prime(
    {"number": 24},
    {"payer": signer.pubkey()}
)
nthPrime = nth_prime(
    {"n": 10},
    {"payer": signer.pubkey()}
)
fib = fibonacci(
    {"n": 19},
    {"payer": signer.pubkey()}
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
