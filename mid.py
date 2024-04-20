class Star_Cinema:
    hall_list = [] 

    def entry_hall(self, newHall): 
        self.hall_list.append(newHall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = [] 
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        Star_Cinema().entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        self.__seats[id] = [['free' for _ in range(self.__cols)] for _ in range(self.__rows)]

    def book_seats(self, show_id, seat_list):
        if show_id in self.__seats:
            for row, col in seat_list:
                if 0 <= row < self.__rows and 0 <= col < self.__cols:
                    if self.__seats[show_id][row][col] == 'free':
                        self.__seats[show_id][row][col] = 'booked'
                    else:
                        print(f"Seat at row {row} and col {col} is already booked.")
                else:
                    print(f"Invalid seat coordinates: row {row}, col {col}.")
        else:
            print(f"No show found with ID: {show_id}")

    def view_show_list(self):

        for id, movie_name, time in self.__show_list:
            print(f"Movie Name: {movie_name}, Show ID: {id}, Time: {time}")

    def view_available_seats(self, show_id):

        if show_id in self.__seats:
            print(f"Available seats for show {show_id} (Matrix view):")

            for row in self.__seats[show_id]:
                print(' '.join(['1' if seat == 'booked' else '0' for seat in row]))
        
        else:
            print(f"No show found with ID: {show_id}")       


hall1 = Hall(rows=20, cols=20, hall_no=1)
hall1.entry_show(id='100', movie_name='Paglu', time='20/4/24  12:00AM')
hall1.entry_show(id='200', movie_name='Khokababu', time='20/4/24 4:00AM')
seats_paglu = [(1, 2), (1, 3), (1, 4)]
hall1.book_seats('100', seats_paglu)
seats_khokababu = [(1, 5), (1, 6), (1, 7)]
hall1.book_seats('200', seats_khokababu)

while True:
    print("1. View all shows today")
    print("2. View available seats")
    print("3. Book tickets")
    print("4. Exit")
    option = input("Enter Option: ")

    if option == "1":
        hall1.view_show_list()

    elif option == "2":
        show_id = input("Enter Show ID: ")
        hall1.view_available_seats(show_id)
        
    elif option == "3":
        show_id = input("Enter Show ID: ")
        seats = input("Enter seats to book (demo like: row,col  '1,2 2,3'): ")
        seat_list = [tuple(map(int, seat.split(','))) for seat in seats.split()]
        hall1.book_seats(show_id, seat_list)
        print("Your Seat Booked successfully",flush=True)

    elif option == "4":
        break
    else:
        print("Invalid option. Please try again.")
