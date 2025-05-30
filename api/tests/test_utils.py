from typing import Any
import pytest


def approx(o1: Any, o2: Any) -> None:
    assert type(o1) is type(o2)

    o1_keys = [v for v in dir(o1) if not v.startswith("__")]
    o2_keys = [v for v in dir(o2) if not v.startswith("__")]

    assert sorted(o1_keys) == sorted(o2_keys)

    for k in o1_keys:
        v1 = getattr(o1, k)
        v2 = getattr(o2, k)
        if isinstance(v1, int) or isinstance(v1, float):
            assert v1 == pytest.approx(v2)
            continue

        if isinstance(v1, bool) or isinstance(v1, str):
            assert v1 == v2
            continue

        approx(v1, v2)
