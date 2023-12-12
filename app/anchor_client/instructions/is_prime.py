from __future__ import annotations
import typing
from solders.pubkey import Pubkey
from solders.instruction import Instruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class IsPrimeArgs(typing.TypedDict):
    number: int


layout = borsh.CStruct("number" / borsh.U128)


def is_prime(
    args: IsPrimeArgs,
    program_id: Pubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> Instruction:
    keys: list[AccountMeta] = []
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"p\xaf\x16\xcb\xf1iu\x1c"
    encoded_args = layout.build(
        {
            "number": args["number"],
        }
    )
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)
