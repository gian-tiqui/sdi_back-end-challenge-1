
class Solution:
    cars = [
        {'size': 'S', 'capacity': 5, 'cost': 5000},
        {'size': 'M', 'capacity': 10, 'cost': 8000},
        {'size': 'L', 'capacity': 15, 'cost': 12000},
    ]

    def __init__(self, seat_amount: int):
        self.seat_amount = seat_amount

    def calculate_total(self) -> None:
        if self.seat_amount == 0:
            return

        remaining_seat = self.seat_amount
        car_amount = {'S': 0, 'M': 0, 'L': 0}
        total = 0

        while remaining_seat > 0:
            if remaining_seat > 10:
                remaining_seat -= 15
                car_amount['L'] = car_amount['L'] + 1
                total += 12000
            elif 10 >= remaining_seat > 5:
                remaining_seat -= 10
                car_amount['M'] = car_amount['M'] + 1
                total += 8000
            elif 5 >= remaining_seat > 0:
                remaining_seat -= 5
                car_amount['S'] = car_amount['S'] + 1
                total += 5000

        for key in car_amount.keys():
            if car_amount[key] != 0:
                print(f'{key} x {car_amount[key]}')

        print(f'TOTAL = PHP {total}')


if __name__ == '__main__':

    input_seat = int(input('Please input number (seat): '))

    solution = Solution(input_seat)

    solution.calculate_total()
