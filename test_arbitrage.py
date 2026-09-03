from src.arbitrage import find_opportunity

def test_finds_profitable_gap():
    opportunity = find_opportunity(0.54, 0.43, 0.02)
    assert opportunity is not None
    assert opportunity.pair_cost == 0.97
    assert opportunity.edge == 0.03

def test_ignores-small-gap():
    assert find_opportunity(0.495, 0.495, 0.02) is None

def test_ignores-pair-above-one():
    assert find_opportunity(0.52, 0.50, 0.02) is None
