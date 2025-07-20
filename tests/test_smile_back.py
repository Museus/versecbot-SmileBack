from versecbot_smile_back.jobs import contains_smile
import pytest

RECOGNIZED_SMILES = [":)", ":D", ":-)"]

MESSAGE_CONTAINING_SMILE = "Hello :)"
MESSAGE_CONTAINING_FROWN = "Hello :("
MESSAGE_WITH_NO_EMOJI = "No smile here"
MESSAGE_WITH_MULTIPLE_SMILES = ":) :) :)"
MESSAGE_CONTAINING_UNRECOGNIZED_SMILE = "Hello :P"
MESSAGE_WITH_MIXED_SMILES = "Hello :D and :("


@pytest.mark.parametrize(
    "message_contents, expected_result",
    [
        (MESSAGE_CONTAINING_SMILE, True),
        (MESSAGE_CONTAINING_FROWN, False),
        (MESSAGE_WITH_NO_EMOJI, False),
        (MESSAGE_WITH_MULTIPLE_SMILES, True),
        (MESSAGE_CONTAINING_UNRECOGNIZED_SMILE, False),
        (MESSAGE_WITH_MIXED_SMILES, True),
    ],
)
def test_contains_smile(message_contents: str, expected_result: bool):
    assert contains_smile(message_contents, RECOGNIZED_SMILES) is expected_result
