import pytest
from tests.flo import diff
from game import play

pytestmark = [pytest.mark.version_2]


def test_quitter():
    diffs = diff(play, path="./quitter.sim.txt")
    assert not diffs, diffs


def test_one_and_done():
    diffs = diff(play, path="./one_and_done.sim.txt")
    assert not diffs, diffs


def test_single_bank():
    diffs = diff(
        play, path="./bank_one_roll_then_quit.sim.txt"
    )
    assert not diffs, diffs


def test_bank_first_for_two_rounds():
    diffs = diff(
        play, path="./bank_first_for_two_rounds.sim.txt"
    )
    assert not diffs, diffs
