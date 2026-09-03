from src.arbitrage import find_opportunity

class MarketWatcher:
    def __init__(self, min_edge=0.02):
        self.min_edge=min_edge
    def check(self, yes_ask, no_ask):
        return find_opportunity(yes_ask, no_ask, self.min_edge)
