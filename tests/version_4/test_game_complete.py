import pytest
from tests.flo import diff
from game import play


pytestmark = [pytest.mark.version_4]


def test_game_complete():
    """Plays 1 round game and confirms proper exit
    IMPORTANT: pass 1 for num_rounds
    """
    diffs = diff(
        lambda roller: play(roller=roller, num_rounds=1), path="/home/abdulkareem/pythonStarter/ten_thousand/tests/version_4/complete.sim.txt"
    )
    assert not diffs, diffs
