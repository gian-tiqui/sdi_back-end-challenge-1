
class Solution:
    cars = [
        {'size': 'S', 'capacity': 5, 'cost': 5000},
        {'size': 'M', 'capacity': 10, 'cost': 8000},
        {'size': 'L', 'capacity': 15, 'cost': 12000},
    ]

    def __init__(self, seat_amount: int):
        self.seat_amount = seat_amount

    def calculate_total(self) -> None:
        if self.seat_amount <= 5:
            print(f'S x {self.seat_amount // self.cars[0]['capacity']}')
            print(self.seat_amount * (self.cars[0]['cost'] // self.cars[0]['capacity']))
        elif 5 <= self.seat_amount <= 10:
            print(f'M x {self.seat_amount // self.cars[1]['capacity']} ')
            print(self.seat_amount * (self.cars[1]['cost'] // self.cars[1]['capacity']))
        else:
            print(f'L x {self.seat_amount // self.cars[2]['capacity']}')
            print(self.seat_amount * (self.cars[2]['cost'] // self.cars[2]['capacity']))


if __name__ == '__main__':

    input_seat_amount = int(input('Please input number (seat): '))

    solution = Solution(input_seat_amount)

    solution.calculate_total()
