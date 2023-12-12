from __future__ import annotations
import typing
from solders.pubkey import Pubkey
from solders.instruction import Instruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class SumOfNaturalNumbersArgs(typing.TypedDict):
    end: int


layout = borsh.CStruct("end" / borsh.U128)


def sum_of_natural_numbers(
    args: SumOfNaturalNumbersArgs,
    program_id: Pubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> Instruction:
    keys: list[AccountMeta] = []
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xd8\x07F\x1f\xc2\xc7\xc2\x8b"
    encoded_args = layout.build(
        {
            "end": args["end"],
        }
    )
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)
