"""Validated baggage inputs. Invalid input returns None rather than raising."""
import math
import re


def parse_booking(code):
    """Accept 2-3 ASCII airline letters/digits, positive flight and seat A-F."""
    if not isinstance(code, str):
        return None
    match = re.fullmatch(r'([A-Za-z0-9]{2,3})-([0-9]{1,4})-([0-9]{1,3})([A-Fa-f])', code.strip())
    if match is None:
        return None
    airline, flight, row, seat = match.groups()
    if int(flight) == 0 or int(row) == 0:
        return None
    return airline.upper(), int(flight), seat.upper()


def total_weight(weights_csv):
    """Accept a nonempty CSV of finite nonnegative weights; reject bad totals."""
    if not isinstance(weights_csv, str) or not weights_csv.strip():
        return None
    total = 0.0
    for token in weights_csv.split(','):
        try:
            weight = float(token.strip())
        except (ValueError, OverflowError):
            return None
        if not math.isfinite(weight) or weight < 0:
            return None
        total += weight
        if not math.isfinite(total):
            return None
    return total


def tag_label(name):
    """Use the first initial and final surname, allowing Unicode letters."""
    if not isinstance(name, str):
        return None
    parts = name.split()
    if len(parts) < 2:
        return None
    for part in parts:
        if not part[0].isalpha() or not part[-1].isalpha():
            return None
        if not all(ch.isalpha() or ch in "-'’" for ch in part):
            return None
    return parts[0][0].upper() + '. ' + parts[-1].upper()


def main():
    steps = [
        ('parse_booking', 'Enter a booking code (e.g. AI-203-12A): ', parse_booking, 'Airline, Flight and Seat Letter:'),
        ('total_weight', 'Enter bag weights in kg as CSV (e.g. 12.5,7,23): ', total_weight, 'Total Weight:'),
        ('tag_label', 'Enter a passenger name (first and last): ', tag_label, 'Tag Label:'),
    ]
    for title, prompt, function, label in steps:
        print(f'==== Running {title} ====')
        try:
            value = input(prompt)
        except (EOFError, KeyboardInterrupt):
            print('\nInput cancelled.')
            return
        result = function(value)
        print('Invalid input. Please check the format.' if result is None else f'{label} {result}')
        print()


if __name__ == '__main__':
    main()
