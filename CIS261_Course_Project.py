# Dwayne Winn CSI261 Class project week 3

import decimal
from pickletools import TAKEN_FROM_ARGUMENT1
from site import ENABLE_USER_SITE

def main():

  #zero counters
  t_gross = float(0.00)
  t_tax = float(0.00)
  t_net = float(0.00)
  e_total = float(0.00)

  #get first employee name 
  e_name =  employee()

  #start loop
  while e_name != 'end':

     #user input hours worked function
     h_worked = hours()

     #call pay rate function
     p_rate = pay_rate()

     #call tax rate function
     t_rate = tax_rate()

     #call gross pay funtion 
     g_pay = grosspay(h_worked,p_rate)

     #call
     i_tax = taxes(g_pay,t_rate)

     #call caculate net pay functions
     e_pay= net_pay(g_pay,i_tax)

      #call function to display employee
     d_pay(e_name,h_worked,i_tax,g_pay,i_tax,e_pay)

     #running totals
     t_gross += g_pay
     t_tax += i_tax
     t_net += e_pay
     e_total += 1
     e_name = employee()


#display running totals
  print('Number of employess:', e_total)
  print('Total gross pay: $',t_gross)
  print('Total income tax: $',t_tax)
  print('Total Income taxes: $',t_net)
  
    

#employee name functions
def employee():
    e_name = input('Employee name or end to quit: ')
    return e_name

#hours worked functions 
def hours():
   h_worked = float(input('Hours worked: '))
   return h_worked

#pay rate function
def pay_rate():
    p_rate = float(input('Pay rate: '))
    return p_rate

#tax rate functions
def tax_rate():
    t_rate= float(input('Income tax rate: '))
    t_rate = t_rate/100
    return t_rate
    
#display caculated data
def d_pay(e_name,h_worked,p_rate,g_pay,i_tax,e_pay):
    print('Employee Name     Hours  Rate Gross Tax Net')
    print(e_name, f"{h_worked: ,.2f}",,f{p_rate:,.2f}", f"{g_pay:,.2f}", f"{i_tax:,.2f}", f"{e_pay:,.2f}")
    return

#caculate gross pay functions
def grosspay(h_worked,p_rate):
    g_pay = (h_worked * p_rate)
    return float(g_pay)

# caculate income tax functions
def taxes(g_pay,t_rate):
    i_tax = (g_pay * t_rate)
    return float(i_tax)

#caculate net_pay
def  net_pay(g_pay,i_tax):
   e_pay = g_pay - i_tax
   return float(e_pay)

if __name__ == '__main__':
    main()
