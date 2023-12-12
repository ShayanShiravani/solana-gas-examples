import typing
from anchorpy.error import ProgramError


class NotPositiveInt(ProgramError):
    def __init__(self) -> None:
        super().__init__(6000, "Input must be a positive integer")

    code = 6000
    name = "NotPositiveInt"
    msg = "Input must be a positive integer"


CustomError = typing.Union[NotPositiveInt]
CUSTOM_ERROR_MAP: dict[int, CustomError] = {
    6000: NotPositiveInt(),
}


def from_code(code: int) -> typing.Optional[CustomError]:
    maybe_err = CUSTOM_ERROR_MAP.get(code)
    if maybe_err is None:
        return None
    return maybe_err
