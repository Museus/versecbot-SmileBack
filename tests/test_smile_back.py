from versecbot_smile_back.util import contains_smile
import pytest

MESSAGE_CONTAINING_SMILE = "Hello :)"
MESSAGE_CONTAINING_FROWN = "Hello :("
MESSAGE_WITH_NO_EMOJI = "No smile here"
MESSAGE_WITH_MULTIPLE_SMILES = ":) :) :)"


@pytest.mark.parametrize(
    "message_contents, expected_result",
    [
        (MESSAGE_CONTAINING_SMILE, True),
        (MESSAGE_CONTAINING_FROWN, False),
        (MESSAGE_WITH_NO_EMOJI, False),
        (MESSAGE_WITH_MULTIPLE_SMILES, True),
    ],
)
def test_contains_smile(message_contents: str, expected_result: bool):
    assert contains_smile(message_contents) is expected_result
