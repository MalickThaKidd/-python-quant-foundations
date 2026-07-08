# Python Core Methods Cheat Sheet

This file is your quick reference for the Python methods you need to master before going deeper into NumPy, financial returns, risk metrics, and Monte Carlo.

The goal is not to memorize everything at once. The goal is to know what exists, recognize it when you see it, and practice it in small scripts.

---

## 1. Built-in functions you must know

These are not specific to lists, strings, or dictionaries. They work across many Python objects.

| Function | What it does | Example |
|---|---|---|
| `print()` | Displays output | `print("hello")` |
| `input()` | Gets user input as a string | `name = input("Name: ")` |
| `len()` | Returns length | `len([1, 2, 3])` |
| `type()` | Shows the type of an object | `type(3.14)` |
| `int()` | Converts to integer | `int("10")` |
| `float()` | Converts to float | `float("3.5")` |
| `str()` | Converts to string | `str(100)` |
| `bool()` | Converts to boolean | `bool(1)` |
| `range()` | Creates a sequence for loops | `range(1, 6)` |
| `sum()` | Adds values | `sum([1, 2, 3])` |
| `min()` | Smallest value | `min([4, 2, 9])` |
| `max()` | Largest value | `max([4, 2, 9])` |
| `round()` | Rounds a number | `round(3.14159, 2)` |
| `sorted()` | Returns a sorted copy | `sorted([3, 1, 2])` |
| `enumerate()` | Gives index and value | `for i, value in enumerate(values):` |
| `zip()` | Loops over two sequences together | `for x, y in zip(xs, ys):` |

### Finance examples

```python
returns = [0.01, -0.02, 0.015]

print(len(returns))
print(sum(returns))
print(min(returns))
print(max(returns))
print(round(sum(returns), 4))
```

```python
tickers = ["AAPL", "MSFT", "TSLA"]
prices = [190, 420, 250]

for ticker, price in zip(tickers, prices):
    print(ticker, price)
```

---

## 2. Strings

A string is text.

```python
ticker = " aapl "
```

Strings are immutable, meaning string methods return a new string. They do not change the original one directly.

### Essential string methods

| Method | What it does | Example |
|---|---|---|
| `.strip()` | Removes spaces at the beginning and end | `" aapl ".strip()` |
| `.lower()` | Converts to lowercase | `"AAPL".lower()` |
| `.upper()` | Converts to uppercase | `"aapl".upper()` |
| `.title()` | Capitalizes each word | `"hello world".title()` |
| `.replace(old, new)` | Replaces text | `"a-b".replace("-", " ")` |
| `.split()` | Splits into a list | `"BUY AAPL 10".split()` |
| `.split(sep)` | Splits by separator | `"100,101,102".split(",")` |
| `.join(list)` | Joins strings | `", ".join(["AAPL", "MSFT"])` |
| `.startswith()` | Checks beginning | `"hello".startswith("h")` |
| `.endswith()` | Checks ending | `"file.py".endswith(".py")` |
| `.find()` | Finds position, returns -1 if absent | `"AAPL.csv".find(".")` |
| `.count()` | Counts occurrences | `"banana".count("a")` |
| `.isdigit()` | Checks if all characters are digits | `"123".isdigit()` |
| `.isalpha()` | Checks if all characters are letters | `"abc".isalpha()` |

### Examples

```python
ticker = " aapl "
clean_ticker = ticker.strip().upper()
print(clean_ticker)  # AAPL
```

```python
trade = "BUY AAPL 10 150"
side, ticker, quantity, price = trade.split()

quantity = int(quantity)
price = float(price)

print(side)
print(ticker)
print(quantity * price)
```

### Common mistakes

```python
"7:30".strip(":")
```

This does not split the time into hours and minutes. It only removes `:` from the edges if it exists there.

Correct:

```python
hours, minutes = "7:30".split(":")
```

---

## 3. Lists

A list stores multiple values in order.

```python
returns = [0.01, -0.02, 0.015]
```

Lists are mutable, meaning you can modify them.

### Essential list methods

| Method | What it does | Example |
|---|---|---|
| `.append(x)` | Adds one item at the end | `returns.append(0.02)` |
| `.extend(list)` | Adds many items | `returns.extend([0.01, 0.03])` |
| `.insert(i, x)` | Inserts at index | `returns.insert(0, 0.0)` |
| `.remove(x)` | Removes first matching value | `returns.remove(0.01)` |
| `.pop()` | Removes and returns last item | `returns.pop()` |
| `.pop(i)` | Removes and returns item at index | `returns.pop(0)` |
| `.index(x)` | Finds index of value | `returns.index(-0.02)` |
| `.count(x)` | Counts occurrences | `returns.count(0.01)` |
| `.sort()` | Sorts the list in place | `returns.sort()` |
| `.reverse()` | Reverses the list in place | `returns.reverse()` |
| `.copy()` | Makes a shallow copy | `copy_returns = returns.copy()` |

### Important list operations

```python
returns = [0.01, -0.02, 0.015]

print(returns[0])     # first item
print(returns[-1])    # last item
print(returns[1:])    # from index 1 to end
print(len(returns))
```

### Looping through a list

```python
returns = [0.01, -0.02, 0.015]

total = 0

for r in returns:
    total += r

print(total)
```

### Looping with index

```python
prices = [100, 102, 101, 105]

for i in range(1, len(prices)):
    today = prices[i]
    yesterday = prices[i - 1]
    print(today - yesterday)
```

### List comprehension

```python
returns = [0.01, -0.02, 0.015, -0.01]
positive_returns = [r for r in returns if r > 0]
print(positive_returns)
```

### Common mistakes

`.sort()` changes the list directly and returns `None`.

```python
returns = [0.03, -0.01, 0.02]
sorted_returns = returns.sort()  # bad idea
print(sorted_returns)            # None
```

Better:

```python
returns = [0.03, -0.01, 0.02]
sorted_returns = sorted(returns)
print(sorted_returns)
```

---

## 4. Tuples

A tuple is like a list, but immutable.

```python
trade = ("AAPL", 10, 150)
```

You cannot append, remove, or change values inside a tuple.

### Essential tuple operations

| Operation | What it does | Example |
|---|---|---|
| indexing | Access value | `trade[0]` |
| unpacking | Assign values to variables | `ticker, qty, price = trade` |
| `len()` | Length | `len(trade)` |
| `.count(x)` | Count value | `trade.count("AAPL")` |
| `.index(x)` | Find index | `trade.index(10)` |

### Example

```python
trade = ("AAPL", 10, 150)
ticker, quantity, price = trade

print(ticker)
print(quantity * price)
```

### When to use tuples

Use tuples when the structure should not change.

Examples:

```python
point = (3, 5)
trade = ("BUY", "AAPL", 10, 150)
price_range = (100, 120)
```

---

## 5. Dictionaries

A dictionary stores key-value pairs.

```python
prices = {
    "AAPL": 190,
    "MSFT": 420,
    "TSLA": 250,
}
```

Dictionaries are extremely important in Python because they let you connect labels to values.

For finance, keys are often tickers, dates, risk categories, countries, or strategy names.

### Essential dictionary methods

| Method / Operation | What it does | Example |
|---|---|---|
| `dict[key]` | Gets value for key | `prices["AAPL"]` |
| `dict[key] = value` | Adds or updates value | `prices["NVDA"] = 900` |
| `key in dict` | Checks if key exists | `"AAPL" in prices` |
| `.get(key)` | Gets value safely | `prices.get("AAPL")` |
| `.get(key, default)` | Gets value or default | `prices.get("NVDA", 0)` |
| `.keys()` | Gets all keys | `prices.keys()` |
| `.values()` | Gets all values | `prices.values()` |
| `.items()` | Gets key-value pairs | `prices.items()` |
| `.update(other_dict)` | Adds/updates many values | `prices.update({"NVDA": 900})` |
| `.pop(key)` | Removes key and returns value | `prices.pop("TSLA")` |
| `.clear()` | Removes everything | `prices.clear()` |
| `.copy()` | Copies dictionary | `new_prices = prices.copy()` |

### Accessing values

```python
prices = {"AAPL": 190, "MSFT": 420}

print(prices["AAPL"])
print(prices.get("NVDA", 0))
```

Use `.get()` when the key may not exist.

### Looping through a dictionary

```python
prices = {"AAPL": 190, "MSFT": 420, "TSLA": 250}

for ticker, price in prices.items():
    print(ticker, price)
```

### Finance example: portfolio value

```python
portfolio = {
    "AAPL": 10,
    "MSFT": 5,
    "TSLA": 2,
}

prices = {
    "AAPL": 190,
    "MSFT": 420,
    "TSLA": 250,
}

total_value = 0

for ticker, quantity in portfolio.items():
    price = prices[ticker]
    value = quantity * price
    total_value += value

print(total_value)
```

### Nested dictionaries

```python
portfolio = {
    "AAPL": {"quantity": 10, "price": 190},
    "MSFT": {"quantity": 5, "price": 420},
}

for ticker, data in portfolio.items():
    value = data["quantity"] * data["price"]
    print(ticker, value)
```

---

## 6. Sets

A set stores unique values.

```python
tickers = {"AAPL", "MSFT", "AAPL"}
print(tickers)  # {'AAPL', 'MSFT'}
```

Sets are useful when you want to remove duplicates or compare groups.

### Essential set methods

| Method / Operation | What it does | Example |
|---|---|---|
| `.add(x)` | Adds value | `tickers.add("TSLA")` |
| `.remove(x)` | Removes value, errors if absent | `tickers.remove("AAPL")` |
| `.discard(x)` | Removes value safely | `tickers.discard("NVDA")` |
| `x in set` | Checks membership | `"AAPL" in tickers` |
| `.union(other)` | Combines sets | `a.union(b)` |
| `.intersection(other)` | Common values | `a.intersection(b)` |
| `.difference(other)` | Values in one not other | `a.difference(b)` |

### Example

```python
portfolio_a = {"AAPL", "MSFT", "TSLA"}
portfolio_b = {"AAPL", "NVDA", "MSFT"}

print(portfolio_a.intersection(portfolio_b))
print(portfolio_a.difference(portfolio_b))
```

---

## 7. Useful patterns to master

### Pattern 1 — Counter with dictionary

```python
tickers = ["AAPL", "MSFT", "AAPL", "TSLA", "AAPL"]
counts = {}

for ticker in tickers:
    if ticker not in counts:
        counts[ticker] = 0
    counts[ticker] += 1

print(counts)
```

Cleaner version with `.get()`:

```python
tickers = ["AAPL", "MSFT", "AAPL", "TSLA", "AAPL"]
counts = {}

for ticker in tickers:
    counts[ticker] = counts.get(ticker, 0) + 1

print(counts)
```

### Pattern 2 — Build a list with a loop

```python
returns = [0.01, -0.02, 0.015, -0.01]
positive_returns = []

for r in returns:
    if r > 0:
        positive_returns.append(r)

print(positive_returns)
```

### Pattern 3 — Parse user input

```python
trade = input("Trade: ")  # BUY AAPL 10 150
side, ticker, quantity, price = trade.split()

quantity = int(quantity)
price = float(price)

print(quantity * price)
```

### Pattern 4 — Convert strings to floats

```python
text = "100,101,99,105"
parts = text.split(",")
prices = []

for part in parts:
    prices.append(float(part))

print(prices)
```

---

## 8. What to master first

Priority order:

1. `str.strip()`, `str.lower()`, `str.upper()`, `str.split()`
2. List indexing, `.append()`, `len()`, `for` loops
3. Dictionary access, `.get()`, `.items()`
4. `range()`, `enumerate()`, `zip()`
5. `sorted()`, `min()`, `max()`, `sum()`
6. Tuples and unpacking
7. Sets for uniqueness

For your quant path, the most important trio is:

```python
lists + dictionaries + loops
```

If you master those, NumPy and pandas will make much more sense later.
