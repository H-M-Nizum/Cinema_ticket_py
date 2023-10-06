class Star_cinema():
    hall_list = []
    
    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.__rows = rows
        self.__cols = cols
        self.hall_no = hall_no
        
    def entry_show(self, id, _movie_name, time):
        self.show_list.append([id, _movie_name, time])
        self.seats[id] = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]

        
    def book_seats(self, id, num):
        tem = 0
        for x in self.show_list:
            if x[0] == id:
                tem = 1
        if tem == 1:
            for i in range(num):
                ro = int(input('Enter row: '))
                co = int(input('Enter col: '))
                if ro>=0 and ro<self.__rows and co>=0 and co<self.__cols:
                    if self.seats[id][ro][co] == 0:
                        print(f"Seat ({ro}, {co}) booked conform \n")
                        self.seats[id][ro][co] = 1
                    else:
                        # if this seat are already booked
                        print('This seat are already booked \n')
                else:
                    # if choose invalid seat number
                    print('Its invalid seat number !\n')
        else:
            # If choose wrong id 
            print('This show are not avabile \n')
            
    def view_show_list(self):
        print('Current show list \n')
        for i in self.show_list:
            print(f"Show ID: {i[0]}, Movie: {i[1]}, Time: {i[2]}")
    
    def view_available_seats(self, id):
        if id in self.seats:
            for i in self.seats[id]:
                print(i)
            print('\n')
        else:
            print('This movie now not available')


cinema = Star_cinema()
          
star = Hall(20, 20, 11)
moon = Hall(30, 30, 12)

cinema.entry_hall(star)
cinema.entry_hall(moon)

star.entry_show(11, 'alibaba', '7Am 1/10/23')
star.entry_show(12, 'dolababa', '10Am 2/10/23')
star.entry_show(13, 'kalababa', '2pm 3/10/23')

moon.entry_show(21, 'lalcan', '2pm 1/10/23')
moon.entry_show(22, 'sadacan', '6pm 2/10/23')
moon.entry_show(23, 'kalacam', '10pm 3/10/23')

flag = True

while flag:
    print('Chose any Option : \n')
    print('1: View all show today')
    print('2: View available seats')
    print('3: Book ticket')
    print('4: Exit')
    op = int(input('Enter your option : '))
    if op == 1:
        for i in cinema.hall_list:
            i.view_show_list()
        
    elif op == 2:
        id = int(input('enter movies id: '))
        star.view_available_seats(id)
        
    elif op == 3:
        id = int(input('enter mivies id: '))
        ticket_num = int(input('enter numbers ticket: '))
        star.book_seats(id, ticket_num)
        
    else:
        flag = False