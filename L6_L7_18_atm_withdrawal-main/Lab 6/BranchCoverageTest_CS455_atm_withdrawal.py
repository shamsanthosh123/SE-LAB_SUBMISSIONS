import pytest
from atm_withdrawal import withdraw, pin_check, note_breakup

# ======================= withdraw() =======================

# --- account_type check: True / False branches ---
def test_simple_withdrawal():
    assert withdraw(5000, 1000, "savings", True) == 4000

def test_unknown_account():
    with pytest.raises(ValueError, match="unknown account"):
        withdraw(5000, 1000, "fixed", True)

# --- amount validity: each part of the 'or' condition ---
def test_invalid_amount_zero():
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(5000, 0, "savings", True)

def test_invalid_amount_negative():
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(5000, -100, "savings", True)

def test_invalid_amount_not_multiple_of_100():
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(5000, 150, "savings", True)

# --- daily limit: both account types, boundary and just over ---
def test_savings_limit_exceeded():
    assert withdraw(90000, 25100, "savings", True) == "limit exceeded"

def test_savings_exactly_at_limit_allowed():
    assert withdraw(30000, 25000, "savings", True) == 5000

def test_current_limit_exceeded():
    assert withdraw(90000, 50100, "current", True) == "limit exceeded"

def test_current_exactly_at_limit_allowed():
    assert withdraw(60000, 50000, "current", True) == 10000

# --- fee logic: own bank / other bank / amount <=10000 / >10000 ---
def test_own_bank_no_fee():
    assert withdraw(5000, 1000, "savings", True) == 4000

def test_other_bank_fee_20():
    assert withdraw(5000, 1000, "savings", False) == 3980

def test_other_bank_exactly_10000_fee_20():
    assert withdraw(20000, 10000, "savings", False) == 9980

def test_other_bank_above_10000_fee_30():
    assert withdraw(20000, 10100, "savings", False) == 9870

def test_other_bank_high_amount_fee_30():
    assert withdraw(20000, 15000, "savings", False) == 4970

# --- balance check ---
def test_insufficient_funds():
    assert withdraw(500, 1000, "savings", True) == "insufficient funds"

def test_insufficient_funds_due_to_fee():
    # 1000 + 20 fee > 1000 balance
    assert withdraw(1000, 1000, "savings", False) == "insufficient funds"

def test_balance_exactly_equals_amount_plus_fee():
    assert withdraw(1020, 1000, "savings", False) == 0

# ======================= pin_check() =======================

def test_correct_pin():
    assert pin_check(1234, 1234, 0) == "ok"

def test_correct_pin_on_last_allowed_attempt():
    assert pin_check(1234, 1234, 2) == "ok"

def test_blocked_with_three_attempts():
    assert pin_check(1234, 1234, 3) == "card blocked"

def test_blocked_with_more_than_three_attempts():
    assert pin_check(1111, 1234, 5) == "card blocked"

def test_wrong_pin_first_attempt_retry():
    assert pin_check(1111, 1234, 0) == "retry"

def test_wrong_pin_second_attempt_retry():
    assert pin_check(1111, 1234, 1) == "retry"

def test_wrong_pin_third_attempt_blocks():
    assert pin_check(1111, 1234, 2) == "card blocked"

# ======================= note_breakup() =======================

def test_note_breakup_invalid_amount():
    with pytest.raises(ValueError, match="invalid amount"):
        note_breakup(250)

def test_note_breakup_zero():
    assert note_breakup(0) == (0, 0, 0)

def test_note_breakup_only_100s():
    assert note_breakup(100) == (0, 0, 1)

def test_note_breakup_exactly_one_200():
    assert note_breakup(200) == (0, 1, 0)

def test_note_breakup_200_and_100():
    assert note_breakup(300) == (0, 1, 1)

def test_note_breakup_500_and_100_no_200():
    assert note_breakup(600) == (1, 0, 1)

def test_note_breakup_500_and_200():
    assert note_breakup(700) == (1, 1, 0)

def test_note_breakup_two_200s():
    assert note_breakup(900) == (1, 2, 0)

def test_note_breakup_only_500s():
    assert note_breakup(1000) == (2, 0, 0)

def test_note_breakup_all_denominations():
    assert note_breakup(1800) == (3, 1, 1)