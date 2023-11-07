from __future__ import annotations
import typing
from solders.pubkey import Pubkey
from solders.instruction import Instruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class NthPrimeArgs(typing.TypedDict):
    n: int


layout = borsh.CStruct("n" / borsh.U128)


class NthPrimeAccounts(typing.TypedDict):
    payer: Pubkey


def nth_prime(
    args: NthPrimeArgs,
    accounts: NthPrimeAccounts,
    program_id: Pubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> Instruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=True)
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x02D\x85k\xc0@\xa1\xfc"
    encoded_args = layout.build(
        {
            "n": args["n"],
        }
    )
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)