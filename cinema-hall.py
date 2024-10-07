class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)

    @classmethod
    def get_hall_list(cls):
        return cls.__hall_list 


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []

        super().entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
            show = (show_id, movie_name, time)
            self.__show_list.append(show)
            self.__seats[show_id] = [[1 for i in range(self.__cols)] for i in range(self.__rows)]

    def book_seats(self, show_id, seat_positions):
        if show_id not in self.__seats:
            raise ValueError('Invalid show id.')
            
        for row,col in seat_positions:
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                raise ValueError(f'Seat ({row}, {col}) is invalid.')
            if self.__seats[show_id][row][col] == 0:
                raise ValueError(f'Seat ({row}, {col}) is booked.')
            self.__seats[show_id][row][col] = 0

    def view_show_list(self):
        show_info = f'{self.__hall_no} no hall shows are running:\n'
        for show in self.__show_list:
            show_info += f'ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}\n'
        return show_info
        
    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            raise ValueError('Invalid show ID.')
        seat_info = f'Available seats for show {show_id}: \n'
        for row in range(self.__rows):
            row_seats = ''
            for col in range(self.__cols):
                if self.__seats[show_id][row][col] == 1:
                    row_seats += 'A '
                else:
                     row_seats += 'B '
            seat_info += row_seats.strip() + '\n'     
        return seat_info
        
hall1 = Hall(10,10,1)
hall1.entry_show('1001','Tofaan','5.00 PM')
hall1.entry_show('1002','Poran','&.00 PM')
hall1.entry_show('1002','Godzila','!0.00 PM')

while True:
    print('\nWelcome to our Cinema. Please Choice: ')
    print("1. View All Shows")
    print("2. View Available Seats")
    print("3. Book Tickets")
    print("4. Logout")
    choice = input('Enter your choice: ')
    
    if choice == '1':
        halls = Star_Cinema.get_hall_list()
        for hall in halls:
            print(hall.view_show_list())
    
    elif choice == '2':
        hall_no = int(input("Enter hall number: "))
        show_id = input("Enter show ID: ")
        halls = Star_Cinema.get_hall_list()
        for hall in halls:
            if hall._Hall__hall_no == hall_no:
                try:
                    print(hall.view_available_seats(show_id))
                except ValueError as e:
                    print(e)

    elif choice == '3':
        hall_no = int(input("Enter hall number: "))
        show_id = input("Enter show ID: ")
        seats = input("Enter seat positions (row,col row,col ...): ")
        seat_positions = [
            tuple(map(int, seat.split(','))) for seat in seats.split()
        ]
        halls = Star_Cinema.get_hall_list()
        for hall in halls:
            if hall._Hall__hall_no == hall_no:
                try:
                    hall.book_seats(show_id,seat_positions)
                    print('Congrats! Tickets booked successfully.')
                except ValueError as e:
                    print(e)
    
    elif choice == '4':
        print('Logout the system. See you again!')
        break
    else:
        print('Wrong Choice, Try again please.')