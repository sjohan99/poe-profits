import msgspec
import logging
from typing import Sequence, Type, TypeVar
from typing import Callable

JsonDataStruct = TypeVar("JsonDataStruct", bound=msgspec.Struct | Sequence[msgspec.Struct])


def parse_into_type(json_bytes: bytes, type_: Type[JsonDataStruct]) -> JsonDataStruct | None:
    try:
        parsed = msgspec.json.decode(json_bytes, type=type_)
        return parsed
    except msgspec.DecodeError as e:
        logging.error(f"Msgspec failed to decode bytes into type: {type_}. Error message: {e}")
        return None


def create_parser(type_: Type[JsonDataStruct]) -> Callable[[bytes], JsonDataStruct | None]:
    def parse_fn(json_bytes: bytes) -> JsonDataStruct | None:
        return parse_into_type(json_bytes, type_)

    return parse_fn
