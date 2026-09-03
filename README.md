# Polymarket Grok Arbitrage

> Grok-agent-powered arbitrage system for BTC Up/Down markets on Polymarket.

A market-neutral arbitrage system designed to detect pricing inefficiencies in binary BTC markets on Polymarket.

The core idea is simple: when the executable cost of buying both sides of a binary market is below $1.00, the difference represents a potential gross arbitrage edge.
![BORED ARBITRAGE TERMINAL](assets/banner.jpg)

## Strategy

For a binary market:

```text
YES + NO = $1.00 at settlement
```

Example:

```text
YES = $0.54
NO  = $0.43

Combined cost = $0.97
Gross edge    = $0.03
```

The system continuously monitors executable ask prices and evaluates whether the detected edge exceeds the configured minimum threshold.

The strategy is market-neutral when both legs are successfully acquired.

## Architecture

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

## Components

### Watcher Agent

Monitors BTC Up/Down markets and evaluates executable Yes/No ask prices.

### Arbitrage Engine

Calculates the potential gross edge:

```text
edge = 1.00 - (YES_ASK + NO_ASK)
```

An opportunity is considered valid when the edge exceeds the configured minimum threshold.

### Executor Agent

Coordinates execution of both sides of the market.

The core execution invariant is:

```text
BOTH LEGS OR NEITHER
```

Production wallet credentials and private execution infrastructure are intentionally excluded from this repository.

### Position Merger

Handles the matched Yes + No position and provides the interface for recycling the resulting position back into collateral.

## Risk Controls

The example configuration includes:

* Minimum edge threshold
* Maximum position size
* Maximum daily loss
* Kill switch
* Dry-run execution
* Both-leg execution requirement
* Fill verification

The repository does not contain private keys, production credentials, or other sensitive wallet infrastructure.

## Agents

The system is structured around specialized agents rather than a single monolithic process:

```text
Watcher
   ↓
Detection
   ↓
Risk
   ↓
Execution
   ↓
Merge
```

This separation makes the strategy easier to test, monitor, and extend.

## Project Structure

```text
polymarket-grok-arbitrage/
│
├── src/
│   ├── arbitrage.py
│   ├── watcher.py
│   ├── executor.py
│   └── merge.py
│
├── config/
│   └── example.yaml
│
├── tests/
│   └── test_arbitrage.py
│
├── docs/
│   └── architecture.md
│
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

## Example Configuration

```yaml
strategy:
  market: BTC_UP_DOWN
  min_edge: 0.02

risk:
  max_position_size: 20
  max_daily_loss: 50
  kill_switch: true

execution:
  dry_run: true
  require_both_legs: true

agents:
  watcher: true
  executor: true
```

## Example

Given:

```text
YES ask = $0.54
NO ask  = $0.43
```

The engine calculates:

```text
pair cost = $0.97
edge      = $0.03
```

With a minimum edge of `0.02`, this opportunity passes the detection threshold.

## Public Release

This repository contains the public architecture, strategy logic, configuration examples, and tests.

Production execution infrastructure, private credentials, and wallet-signing components are intentionally excluded.

## Status

The project is under active development.

The public repository is intended to demonstrate the architecture and core logic behind the arbitrage system.

## Disclaimer

This project is provided for educational and research purposes.

Prediction-market trading involves financial risk. Past performance does not guarantee future results.
