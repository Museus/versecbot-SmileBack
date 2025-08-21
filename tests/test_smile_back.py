from versecbot_smile_back.jobs import contains_smile
import pytest

RECOGNIZED_SMILES = [":)", ":D", ":-)"]

TEST_MESSAGES = [
    {"message": "Hello :)", "expected": True},
    {"message": "Hello :(", "expected": False},
    {"message": "No smile here", "expected": False},
    {"message": ":) :) :)", "expected": True},
    {"message": "Hello :P", "expected": False},
    {"message": "Hello :D and :(", "expected": True},
]


@pytest.mark.parametrize("test_case", TEST_MESSAGES)
def test_contains_smile(test_case: dict[str, str | bool]) -> None:
    assert (
        contains_smile(test_case["message"], RECOGNIZED_SMILES) is test_case["expected"]
    )
