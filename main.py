from operation import rent_land,return_land
from write import write_rented_land,write_returned_land
def menu_choice():
    '''displays the company details of company and execute the process according to user choice'''
    print("\n")
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\t  Techno Property Nepal            ")
    print("\t\t\t\t\t\t\tAddress: Kathmandu,Nepal  ")
    print("\t\t\t\t\t\t\t   Contact:98xxxxxxxx      ")
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    while True:
        print("-----------------------------------------------------------------")
        print("\t\t\t What would you like to do?        ")
        print("-----------------------------------------------------------------")
        print("---->1. To rent the land.")
        print("---->2. To return the land.")
        print("---->3. To Exit the process.")
        print("-----------------------------------------------------------------")
        try:
            #prompts the customer ro enter their choice
            choice = int(input("\nPlease Enter your choice(1,2, or 3): "))
            if choice in [1,2,3]:
                #return the choice if it is valid(1,2,or 3)
                    if choice==1:
                        try:
                            #call the rent_land to record the renting land details
                            name,number,address,date_time,land_rented,grand_total,invoice_id=rent_land()
                            #Call the wite_rented_land to print the invoice of renting land
                            write_rented_land(name,number,address,date_time,land_rented,grand_total,invoice_id)
                            print("\n---------------------------------The land is Rented successfully----------------------------------------------")
                        except:
                            print("\n\t\t\t----Sorry.Please Try Again Later.----")
                            continue
                    elif choice==2:
                            #Call the return_land to record the returning land details
                            name,number,address,date_time,land_returned,month_rent,month_return,fine,total,grand_total,fine_total,return_invoice_id=return_land()
                            #Call the write_returned_land  to print the invoice of returning land
                            write_returned_land(name,number,address,date_time,land_returned,month_rent,month_return,fine,total,grand_total,fine_total,return_invoice_id)
                            print("\n---------------------------------------------The land is Returned successfully----------------------------------------------------------")
                    elif choice==3:
                        print("\n-----Thank you for Visiting Techno Property Nepal! Have a great day!-----")
                        break
            else:
                print("\n---Invalid Choice.Please Try again---")
        except ValueError:
            print("\n---Invalid Input.Please enter a number.---")
    
#function is called to print the menu
menu_choice()

    
