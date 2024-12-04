from read import read_a_file,read_invoice
from datetime import datetime
from write import update_land
 
def rent_land():
    '''A function for renting the land which return name as string,number as int,address as string,datetime ,land_rented as list and total price as int  for renting.'''
    #Read the land details from a file using read_a_file() function from read.py
    land_dict=read_a_file()
    
    while True:
        try:
            for value in land_dict.values():
                if value[-1]==" Not Available":
                    raise ValueError("\n\t\t----None of the lands are available for rent----")
                    break
                else:
                    #Display a welcome message to the customer
                    print("------------------------------------------------------------------------------------------------------------------")
                    print("\t\t\t\t\tWelcome To Techno Property Nepal ")
                    print("\t\t\t\t\t    Thank you for Choosing Us ")
                    print("------------------------------------------------------------------------------------------------------------------")
                    #prompt the customer for their name ,number and address
                    print("\nPlease Provide your Name,Number and Address for the Billing.")
                    name=input("\nEnter Your Full Name: ")
                   #validating the length of number
                    while True:
                        try:
                            number=int(input("\nEnter Your Mobile Number: "))
                            number=str(number)
                            if len(number)<10 or len(number)>10:
                                raise ValueError("\n---Please Enter The valid Number---")
                            break
                        except ValueError as e:
                            print("\n",e)
                    address=input("\nEnter Your Address: ")
                    print("------------------------------------------------------------------------------------------------------------------")
                    #initialize an empty list to store rented land details
                    land_rented=[]
    
                    #Initialize a variable to control the renting land
                    choice="Yes"

                    #Start a loop to allow the customer to rent multiple land
                    while choice.lower()=="yes":
                        print("\n")
                        print("-----------------------------------------------------------------------------------------------------------------")
                        print("\t\t\t\t\tHere are the list of available Land")

                    #Display a table with land details
                        print("-----------------------------------------------------------------------------------------------------------------")
                        print("Kitta No.\t Address\t\tDirection\tArea(aana)\t  Rent Price\t  Avaibility")
                        print("-----------------------------------------------------------------------------------------------------------------")

                        #Iteration through the land dictionary and print the land details
                        for kitta_no,land_details in land_dict.items():
                            print(kitta_no,end="\t\t")
                            for details in land_details:
                                print(details,end="\t\t")
                            print("\n")
                        print("-----------------------------------------------------------------------------------------------------------------")
        
                        #store the kitta number in list
                        k=list(land_dict.keys())
        
                        '''get and validate the kitta nunber given by customer and also check
                           if that land are available to rent or not'''
                        while True:
                            try:
                                valid_kitta=int(input("\nPlease provide the Kitta number of Land you want to rent: "))
                                iter_valid_kitta=str(valid_kitta)
                                if valid_kitta in k:
                                    ava=land_dict[valid_kitta][-1]
                                    aval=ava.lower()
                                    if aval==" not available":
                                        raise ValueError("---The land is Unavailable.Please Enter the kitta number of available land.---")
                                    else:
                                        land_dict[valid_kitta][-1]=" Not Available" #update the avaibility of land
                                        break
                                else:
                                    raise ValueError("---Invalid Kitta Number.Please Provide Valid Kitta Number Again.---")        
                            except ValueError as e:
                                print(e)
        
                        #update the the file land.txt
                        update_land(land_dict)

                        #get valid aana froom the customer
                        aana=valid_aana(land_dict,valid_kitta,1)
        
                        #get the valid month form the customer
                        while True:
                            try:
                                month=int(input("\nEnter the desired period of month you want to rent land: "))
                                if month<=0:
                                    raise ValueError("---Invalid Month---")
                                break
                            except ValueError as e:
                                print(e)
        
    
                        #store the rented land in list
                        land_r=[valid_kitta,land_dict[valid_kitta][0],land_dict[valid_kitta][1],land_dict[valid_kitta][2],land_dict[valid_kitta][3],month,int(land_dict[valid_kitta][3])*month]
                        land_rented.append(land_r)

                        #get date and time
                        date_time=datetime.now()
                        invoice_id=str(datetime.now().minute)+str(datetime.now().second)+str(datetime.now().microsecond)

                        #calculate the total price for rented land
                        grand_total=sum(item[6] for item in land_rented)

                        #ask the customer if they want to rent another land
                        l=[]
                        s={}
                        while True:
                            try:
                                choice=input("\nWould You Like To Rent More Land?(yes/no): ")
                                if choice.lower() in ["yes","no"]:
                                    if choice.lower()=="yes":
                                        for value in land_dict.values():
                                             l.append(value[-1])
                                             s=set(l)
                                        if " Not Available" in s and len(s)==1:
                                             raise ValueError("----None of the lands are available so can't be rented----")
                                        break
                    
                                else:
                                    raise ValueError("---Invalid input.Please Enter 'yes' or 'no'.---")
                                print("\n")
                                break #break out the loop if input is valid
                            except ValueError as e:
                                print(e)
                    
                    #Display the rented summary to the customer
                    print("\n")
                    print("---------------------------------------------------------------------------------------------------------------")
                    print("\t\t\t\t\t  Techno Property Nepal            ")
                    print("\t\t\t\t\tAddress: Kathmandu,Nepal  ")
                    print("\t\t\t\t\t   Contact:98xxxxxxxx      ")
                    print("---------------------------------------------------------------------------------------------------------------")
                    print("Customer Details:")
                    print("-----------------------------------------")
                    print(f"Invoice ID: {invoice_id}")
                    print(f"Customer Name: {name}")
                    print(f"Phone Number: {number}")
                    print(f"Address: {address}")
                    print(f"Date and Time: {date_time}")
                    print("-----------------------------------------")
                    print("\nRented Land Details:")
                    print("----------------------------------------------------------------------------------------------------------------")
                    print("Kitta No.\t Address\t\tDirection\tArea(aana)\t  Rent Price\tMonth\t  Total Price")
                    print("----------------------------------------------------------------------------------------------------------------")
                    for land in land_rented:
                        for i in land:
                            print(i,end="\t\t")
                        print("\n")
                    print("----------------------------------------------------------------------------------------------------------------")
                    print(f"\t\t\t\t\t\t\t\t\t\t\t   Grand Total:{grand_total}")
                    print("----------------------------------------------------------------------------------------------------------------")

                    return name,number,address,date_time,land_rented,grand_total,invoice_id
        except ValueError as e:
            print(e)
            break
            
def valid_aana(land_dict,valid_kitta,operation):
    '''For validation of area of land with parameters as land_dict as dictionaries,valid_kitta as int ,operation as int and return aana as int'''
    total_aana=int(land_dict[valid_kitta][2])
    if operation==1:
        while True:
            try:
                aana=int(input("\nPlease Provide the area of land you want to rent: "))
                if aana<0:
                    raise ValueError("---Invalid area of land.Please enter positive area---")
                elif aana < total_aana:
                    raise ValueError("---You Must Rent Whole Area of land.---")
                elif aana>total_aana:
                    raise ValueError("---Invalid Area of Land.Please enter Valid area.---")
                else:
                    return aana
            except ValueError as e:
                print(e)
    elif operation==2:
        while True:
            try:
                aana=int(input("\nPlease Provide the area of land you want to return: "))
                if aana<0:
                    raise ValueError("---Invalid area of land.Please enter positive area---")
                elif aana < total_aana:
                    raise ValueError("---You Must Return Whole Area of land.---")
                elif aana>total_aana:
                    raise ValueError("---Invalid Area of Land.Please enter Valid area.---")
                else:
                    return aana
            except ValueError as e:
                print(e)

def return_land():
     '''A function for returning the land which return name as string,number as int,address as string,date_time,land_returned as list,month_rent as int,month_return as int,fine as int
,total as int,grand_total as int,fine_total as int,return_invoice_id as int '''
     #Display a welcome message to the customer
     print("------------------------------------------------------------------------------------------------------------------")
     print("\t\t\t\t\tWelcome To Techno Property Nepal ")
     print("\t\t\t\t\t    Thank you for Choosing Us ")
     print("------------------------------------------------------------------------------------------------------------------")
     #prompt the customer for their name ,number and address
     print("\nPlease Provide your Name,Number and Address for the Billing.")
     name=input("\nEnter Your Full Name: ")
     #validating the length of number
     while True:
         try:
             number=int(input("\nEnter Your Mobile Number: "))
             number=str(number)
             if len(number)<10 or len(number)>10:
                 raise ValueError("\n---Please Enter The valid Number---")
             break
         except ValueError as e:
             print(e)
     address=input("\nEnter Your Address: ")
     #extract the details of rented invoice 
     bill,land_dict,return_invoice_id=read_invoice()

     print("------------------------------------------------------------------------------------------------------------------\n")
     print("Here is your bill of given invoice id.")
     
     #initialize an empty list to store rented land details
     land_returned=[]
     
     #Initialize a variable to control the renting land
     choice="Yes"
     
     #Start a loop to allow the customer to rent multiple land
     while choice.lower()=="yes":
         #land detail from land.txt
         land_detail=read_a_file()

         #print the invoice of rented land bill of given invoice id
         for bill_line in bill:
             bill_history=bill_line.replace("\n","")
             print(bill_history)

         #store the rented kitta number of invoice in list
         k=list(land_dict.keys())

         #get and valid the kitta number from the invoice and check if the land is returned
         while True:
            try:
                valid_kitta=int(input("\nPlease provide the Kitta number of Land you want to return: "))
                upvalid_kitta=int(valid_kitta)
                valid_kitta=str(valid_kitta)
                if valid_kitta in k:
                    if land_detail[upvalid_kitta][-1]==" Not Available":
                        land_detail[upvalid_kitta][-1]=" Available"
                        break
                    else:
                        raise ValueError("---The Land has already been returned.---")    
                    return valid_kitta
                else:
                    raise ValueError("---Invalid Kitta Number.Please Provide Valid Kitta Number Again.---")
            except ValueError as e:
                print(e)     
         #update the avaibility in land.txt
         update_land(land_detail)

         #get valid aana froom the customer
         aana=valid_aana(land_dict,valid_kitta,2)
        
         # the month rented extracted from invoice
         month_rent=int(land_dict[valid_kitta][4])

         #validate the month returning
         while True:
            try:
                month_return=int(input("\nEnter the period of month Returning After:"))
                if month_return<=0:
                    raise ValueError("---Invalid Month--")
                break
            except ValueError as e:
                print(e)

         #calculate total amount and fine for renting
         fine=0
         if month_rent==month_return:
             total=int(land_dict[valid_kitta][3])*month_rent
         elif month_rent>=month_return:
             total=int(land_dict[valid_kitta][3])*month_return
         elif month_rent<=month_return:
             total=int(land_dict[valid_kitta][3])*month_return
             duration=month_return-month_rent
             fine=int(land_dict[valid_kitta][3])*duration*0.1
        
         #store the rented land in list
         land_r=[valid_kitta,land_dict[valid_kitta][0],land_dict[valid_kitta][1],land_dict[valid_kitta][2],land_dict[valid_kitta][3],month_rent,month_return,total,fine]
         land_returned.append(land_r)
         
         #calculate the total price for rented land
         total=sum(item[7] for item in land_returned)

         #calculating the total fine applied
         fine_total=sum(item[8] for item in land_returned)
         
         #calculating the grand total if multiple land is returned
         grand_total=fine_total+total
         
         #get date and time
         date_time=datetime.now()
         return_invoice_id=str(datetime.now().minute)+str(datetime.now().second)+str(datetime.now().microsecond)

         #ask the customer if they want to return another land
         l=[]
         s={}
         while True:
             try:
                 choice=input("\nWould You Like To Return More Land?(yes/no): ")
                 if choice.lower() in ["yes","no"]:
                     if choice.lower()=="yes":
                         for key in k:
                             l.append(land_detail[int(key)][-1])
                             s=set(l)
                         if " Available" in s and len(s)==1:
                             raise ValueError("----Thank You!,You have returned all the lands.---")
                         break
                 else:
                     raise ValueError("---Invalid input.Please Enter 'yes' or 'no'.---")
                 print("\n")
                 break #break out the loop if input is valid
             except ValueError as e:
                 print(e)

     #Display the returned summary to the customer
     print("\n")
     print("---------------------------------------------------------------------------------------------------------------------------------------------------")
     print("\t\t\t\t\t\t\t  Techno Property Nepal            ")
     print("\t\t\t\t\t\t\tAddress: Kathmandu,Nepal  ")
     print("\t\t\t\t\t\t\t   Contact:98xxxxxxxx      ")
     print("---------------------------------------------------------------------------------------------------------------------------------------------------")
     print("Customer Details:")
     print("-----------------------------------------")
     print(f"Invoice ID: {return_invoice_id}")
     print(f"Customer Name: {name}")
     print(f"Phone Number: {number}")
     print(f"Address: {address}")
     print(f"Date and Time: {date_time}")
     print("-----------------------------------------")
     print("\nRented Land Details:")
     print("---------------------------------------------------------------------------------------------------------------------------------------------------")
     print("Kitta No.\t Address\t\tDirection\tArea(aana)\t Rent Price\tMonth Rented\tMonth Returned\t Total Price\tFine Amount")
     print("---------------------------------------------------------------------------------------------------------------------------------------------------")
     for land in land_returned:
         for i in land:
             print(i,end="\t\t")
         print("\n")
     print("---------------------------------------------------------------------------------------------------------------------------------------------------")
     print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t   Total:{total}")
     print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t   Total Fine Amount:{fine_total}")
     print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t   Grand Total:{grand_total}")
     print("---------------------------------------------------------------------------------------------------------------------------------------------------")
     return name,number,address,date_time,land_returned,month_rent,month_return,fine,total,grand_total,fine_total,return_invoice_id
      
#return_land() #for deubugging
#rent_land() #for debugging
            
            
