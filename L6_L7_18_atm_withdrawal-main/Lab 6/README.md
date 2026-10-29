# L6_L7_18_atm_withdrawal — ATM Withdrawal

Lab 6: Code and Branch Coverage

## About
A small Python module that processes ATM withdrawals with daily limits and fees, checks PIN attempts and works out the note breakup.

## Files
| File | Description |
|------|-------------|
| `atm_withdrawal.py` | The module under test |
| `test_atm_withdrawal.py` | Starter test file |
| `CodeCoverageTest_CS455_atm_withdrawal.py` | Tests for code (line) coverage |
| `BranchCoverageTest_CS455_atm_withdrawal.py` | Tests for branch coverage |
| `code_coverage.png` | Terminal screenshot of line coverage |
| `branch_coverage.png` | Terminal screenshot of branch coverage |

## Setup
```bash
pip install coverage pytest
```

## How to run
Run these from inside the `Lab 6` folder.

Code coverage:
```bash
coverage run -m pytest CodeCoverageTest_CS455_atm_withdrawal.py
coverage report -m
```

Branch coverage:
```bash
coverage run --branch -m pytest BranchCoverageTest_CS455_atm_withdrawal.py
coverage report -m
```

## Results
| Type | Test file | Coverage |
|------|-----------|----------|
| Starter tests | `test_atm_withdrawal.py` | 38% |
| Line coverage | `CodeCoverageTest_CS455_atm_withdrawal.py` | 100% |
| Branch coverage | `BranchCoverageTest_CS455_atm_withdrawal.py` | 100% |

## What the tests cover
- `withdraw()`: unknown account, invalid amounts (zero, negative, not a multiple of 100), daily limits for savings and current accounts (at and above the limit), own-bank and other-bank fees (₹20, and ₹30 above 10000), and sufficient or insufficient balance.
- `pin_check()`: correct PIN, wrong PIN with retry, and card blocked after the third wrong attempt or when attempts reach 3.
- `note_breakup()`: invalid amounts and breakups using 500, 200 and 100 notes.
