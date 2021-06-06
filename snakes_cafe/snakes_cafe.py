print("""$ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")

manue=['Wings','Cookies','Spring Rolls','Salmon','Steak','Meat Tornado','A Literal Garden'
,'Ice Cream','Cake','Pie','Coffee','Tea','Unicorn Tears']

order_list=[0,0,0,0,0,0,0,0,0,0,0,0,0]


def make_an_order(manue):
    order= input('>').title()
    flag=True
    while (flag):
        if(order in manue):
           order_list[int(manue.index(order))]=int(order_list[manue.index(order)])+1 
           print_order(manue,order_list)
           order= input('>').title()
        elif order=='Quit':
            break
        else:
            print('Please insert from main mune')
            order= input('>').title()
            
def print_order(manue,order_list):
    counter=0
    for ele in order_list:
        if(ele != 0):
            print(f'** {ele} orders of {manue[counter]} have been added to your meal **')
        counter+=1
make_an_order(manue)


print('Summary Of Order:')
print_order(manue,order_list)
        





