# Dwayne Winn CSI261 Class project week 3



def main():
  t_gross = float()
  t_net = float()
  t_tax = float()
  t_hours = float()
  e_total = int()
  #zero counter
  i_tax = 0
  p_rate = 0
  n_pay = 0
  g_pay = 0
  #get first employee name 
  e_name =  employee()

  #start loop
  while e_name != 'end':
     #user input hours worked function
     h_worked = hours()

     #call pay rate input function
     p_rate = pay_rate()

     # call tax rate input function
     t_rate = tax_rate()

     #call gross pay funtion 
     g_pay = grosspay(h_worked,p_rate)

     #get income tax cacualtion function
     i_tax = taxes(g_pay,t_rate)

     #call caculate net pay functions
     e_pay= net_pay(g_pay,i_tax)

     #call function to display employee
     d_pay(e_name,h_worked,p_rate,g_pay,i_tax,e_pay)
      
     t_gross += g_pay
     t_hours += h_worked
     t_tax += i_tax
     t_net += e_pay
     e_total += 1
     #get next employee name
     print('')
     e_name = employee() 
     
     
  #Call display totals
  totals(e_total,t_hours,t_gross,t_tax,t_net)


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
    
    print('Emplyee ',e_name)
    print('Hours: ',f"{h_worked: ,.2f}")
    print('Pay Rate: $',f"{p_rate:,.2f}",)
    print('Gross pay: $',f"{g_pay:,.2f}")
    print('Income tax: $', f"{i_tax:,.2f}")
    print('Net pay: $', f"{e_pay:,.2f}")
    return

#caculate gross pay functions
def grosspay(h_worked,p_rate):
    g_pay = h_worked * p_rate
    return float(g_pay)

# caculate income tax functions
def taxes(g_pay,t_rate):
    i_tax = g_pay * t_rate
    return float(i_tax)

#caculate net_pay
def  net_pay(g_pay,i_tax):
   e_pay = g_pay - i_tax
   return float(e_pay)

#display running totals
def totals(e_total,t_hours,t_gross,t_tax,t_net):
   print('Number of employess:',e_total)
   print('Total hours: ',f"{t_hours:,.2f}")
   print('Total gross pay: $',f"{t_gross:,.2f}")
   print('Total income tax: $',f"{t_tax:,.2f}")
   print('Total net taxes: $',f"{t_net:,.2f}")
  

if __name__ == '__main__':
   main()
