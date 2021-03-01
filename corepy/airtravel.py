"""Model for aircraft flights."""


class Flight:
    """A flight with a particular passenger aircraft"""
    # pass Bare minimum for a named class
    def __init__(self, number, aircraft):
        """Not quite a constructor"""
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")

        self._number = number
        # _number doesn't clash with underscore
        # symbolizes a private variable
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number

    def allocate_seat(self, seat, passenger):
        """Allocate a seate to a passenger.

        Args:
            seat: A seat designator such as '12C' or '21F'.
            passenger: The passenger name.

        Raises:
            ValueError: If the seat is unavailable
        """
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")

        self._seating[row][letter] = passenger

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row {row_text}")

        if row not in rows:
            raise ValueError(f"Invalid row number {row}")

        return row, letter

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger to a different seat.

        Args:
            from_seat: The existing seat designator for the passenger to be moved.
            to_seat: The new seat designator.
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate in seat {from_seat}")

        # Couldn't we just call allocate seat here instead?
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} already occupied")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seates()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seates(self):
        """An iterable series of passenger seat locations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield passenger, f"{row}{letter}"


# class Aircraft:
#     """Deprecated in favor of individual full configurations"""
#     def __init__(self, registration, model, num_rows, num_seats_per_row):
#         self._registration = registration
#         self._model = model
#         self._num_rows = num_rows
#         self._num_seats_per_row = num_seats_per_row
#
#     def registration(self):
#         return self._registration
#
#     def model(self):
#         return self._model
#
#     def seating_plan(self):
#         return (range(1, self._num_rows + 1),
#                 "ABCDEFGHJK"[:self._num_seats_per_row])

class Aircraft:

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777(Aircraft):

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        # Ignoring 1st class seating
        return range(1, 56), "ABCDEGHJK"


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f"| Name: {passenger}"      \
             f" Flight: {flight_number}" \
             f" Seat: {seat}"            \
             f" Aircraft: {aircraft}"    \
             " |"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()


def make_flights():
    # f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
    f = Flight("BA758", AirbusA319("G-EUPT"))
    f.allocate_seat("12A", "Max Rockatansky")
    f.allocate_seat("15E", "Imperator Furiosa")
    f.allocate_seat("15F", "Nux")
    f.allocate_seat("1C", "The Dag")
    f.allocate_seat("1D", "Toast")

    g = Flight("AF72", Boeing777("F-GSPS"))
    g.allocate_seat("55K", "Immortan Joe")
    g.allocate_seat("33G", "Rictus Erectus")
    g.allocate_seat("4B", "The Doof Warrior")
    g.allocate_seat("4A", "Slit")

    return f, g
