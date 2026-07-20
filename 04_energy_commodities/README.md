# Energy & Commodities Projects

This track connects quantitative finance with oil, gas, LNG, electricity, and commodity-linked macroeconomics. The projects should combine commercial logic, physical units, scenarios, and risk.

## 01 — Oil Revenue Scenario Engine

### Problem
Estimate government or project revenue from oil production under different price, production, cost, and fiscal assumptions.

### Core requirements
- model production volume, benchmark price, quality differential, operating cost, transport cost, royalties, taxes, and government participation;
- convert barrels per day into monthly and annual production;
- calculate gross revenue, net operating revenue, fiscal payments, and government take;
- create low, base, and high scenarios;
- perform sensitivity analysis on price and production;
- keep physical units explicit;
- present results in clear tables and charts.

### Research questions
- What is the difference between Brent price and realised price?
- How do royalties differ from profit-based taxes?
- Why can high production fail to produce high public revenue?

### Extensions
- decline curves;
- cost recovery contracts;
- exchange-rate risk;
- break-even price;
- discounted cash flow and project NPV.

### Deliverables
A documented scenario model, unit checks, tests, sensitivity charts, and a short commercial interpretation.

---

## 02 — LNG Cargo Economics Calculator

### Problem
Evaluate the economics of an LNG cargo from purchase to delivery.

### Core requirements
- model cargo volume, energy content, purchase price, shipping distance, charter rate, boil-off, regasification cost, and selling price;
- convert between relevant units such as MMBtu, tonnes, and currency values;
- calculate delivered cost, revenue, gross margin, and margin per MMBtu;
- compare routes or destinations;
- create scenarios for gas price, freight, and boil-off;
- document every unit conversion and assumption.

### Research questions
- How are LNG prices quoted?
- What is boil-off gas and why does voyage duration matter?
- Why can regional gas-price spreads disappear after logistics costs?

### Extensions
- destination flexibility;
- hedging with gas benchmarks;
- vessel speed optimisation;
- carbon cost;
- portfolio of multiple cargoes.

### Deliverables
A reusable calculator, unit-conversion module, tests, scenario tables, and a cargo decision memo.

---

## 03 — Commodity Price Risk and Hedging Lab

### Problem
Measure commodity price risk and test simple hedging strategies for a producer, importer, or airline.

### Core requirements
- import spot and futures price data or use a documented synthetic dataset;
- calculate returns, volatility, correlation, and basis;
- define an unhedged exposure;
- simulate profit and loss under price scenarios;
- calculate a minimum-variance hedge ratio;
- compare unhedged and hedged outcomes;
- discuss basis risk, liquidity, and contract mismatch;
- produce charts and a written recommendation.

### Research questions
- What is the difference between price risk and basis risk?
- Why is a hedge rarely perfect?
- How do contract size and maturity affect implementation?

### Extensions
- rolling hedge ratios;
- stress testing;
- options-based protection;
- jet-fuel versus crude-oil cross hedge;
- expected shortfall.

### Deliverables
A risk model, hedge comparison, tests, charts, and a concise recommendation explaining both benefits and limitations.

## Completion standard
An energy project is complete when physical units are consistent, commercial assumptions are traceable, scenarios are realistic, and the final result is interpreted as a decision rather than only a calculation.
