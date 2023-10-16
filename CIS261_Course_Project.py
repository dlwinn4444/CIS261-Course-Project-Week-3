# Dwayne Winn CSI261 Class project week 3

from pickletools import TAKEN_FROM_ARGUMENT1
from site import ENABLE_USER_SITE


def main():
   #get employee name
   employee()
   #start loop
   if e_name != 'end':
     #call for hours
     hours()
     #callfor pay rate 
     pay_rate()
     #call for tax rate
     tax_rate()
     #call caculate input return results
     caculate_pay(h_worked,p_rate,t_rate)
     #display employee's caculate payroll
     e_totals(e_name,g_pay,i_tax,n_pay)
     #runnuing totals
     e_count += 1
     t_hours= t_hours + hours
     t_tax = t_tax + i_tax
     t_net = t_net = n_pay
     
     main()
      
   elif e_name == 'end':
       r_totals(t_hours,t_tax,t_net)

def employee():
    e_name = input('Employee name or end to quit: ')
    return main(e_name)

def hours():
    h_worked = input('Hours worked: ')
    return(h_worked)

def pay_rate():
    p_rate = input('Pay rate: ')
    return main(p_rate)

def tax_rate():
    t_rate = input('Income tax rate:(decimal only) ')
    return main(t_rate)



def caculate_pay():
    g_pay = h_worked * p_rate
    i_tax = g_pay * t_rate
    n_pay = g_pay - i_tax
    return main(g_pay,i_tax,n_pay)

def e_totals():
    print('Employee name: ',e_name)
    print('Gross pay: $',g_pay)
    print('Income tax $',i_tax)
    print('Net pay: $',n_pay)
    return main()

def r_totals():
    print('Total employees: ',e_count)
    print('Total gross pay: $',t_gross)
    print('Total income tax: $',t_tax)
    print('Total net pay: $',t_net)
    
__name__=__main__
