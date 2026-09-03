from dataclasses import dataclass


@dataclass(frozen=True)
class ArbitrageOpportunity:
    yes_ask: float
    no_ask: float
    pair_cost: float
    edge: float


def find_opportunity(
    yes_ask: float,
    no_ask: float,
    min_edge: float = 0.02,
) -> ArbitrageOpportunity | None:
    """
    Detect an executable binary-market arbitrage opportunity.

    For a complete Yes + No pair:
        guaranteed value = $1.00

    Therefore:
        edge = 1.00 - (yes_ask + no_ask)

    Only ask prices are used because they represent
    the executable purchase price.
    """

    pair_cost = yes_ask + no_ask
    edge = 1.0 - pair_cost

    if edge < min_edge:
        return None

    return ArbitrageOpportunity(
        yes_ask=yes_ask,
        no_ask=no_ask,
        pair_cost=pair_cost,
        edge=edge,
    )
