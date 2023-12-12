from __future__ import annotations
import typing
from solders.pubkey import Pubkey
from solders.instruction import Instruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class BitwiseOperationArgs(typing.TypedDict):
    input: int


layout = borsh.CStruct("input" / borsh.U128)


def bitwise_operation(
    args: BitwiseOperationArgs,
    program_id: Pubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> Instruction:
    keys: list[AccountMeta] = []
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x01\xf1m\xb7D|\xd7\x8c"
    encoded_args = layout.build(
        {
            "input": args["input"],
        }
    )
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)
