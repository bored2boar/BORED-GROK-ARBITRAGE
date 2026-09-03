# Architecture

The system is split into independent components.

```text
Polymarket Market Data
        |
        v
   Watcher Agent
        |
        v
  Arbitrage Engine
        |
        v
    Risk Checks
        |
        v
   Executor Agent
        |
        v
   Position Merge
        |
        v
  Capital Recycled
```

## Watcher

Monitors BTC Up/Down markets and evaluates executable ask prices.

## Arbitrage Engine

Calculates:

`edge = 1.00 - (YES_ASK + NO_ASK.`)

## Executor

Coordinates both sides of the trade.

||BOTH LEGS OR NEITHER||

Production credentials and private infrastructure are excluded.
