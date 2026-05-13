import random


def test_flaky_25_percent():
    assert random.random() >= 0.25, "intentional ~25% flake"
