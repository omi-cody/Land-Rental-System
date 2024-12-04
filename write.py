def update_land(land_dict):
    '''function to update land.txt when the land is rented or returned '''
    with open("land.txt","w") as file:
        for value in land_dict.values():
            file.write(str(value[0])+","+str(value[1])+","+str(value[2])+","+str(value[3])+","+str(value[4]))
            file.write("\n")
    
def write_rented_land(name,number,address,date_time,land_rented,grand_total,invoice_id):
    '''Function to generate a bill for rented land'''
    #Generate the bill name based on customer name ,number and time of rent
    file_name=f"rent_{invoice_id}.txt"
    #Open the file in write mode
    with open(file_name,"w") as file:
        #write Shop details and header
        file.write("----------------\n")
        file.write(f"INVOICE ID:{invoice_id}\n")
        file.write("---------------------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t  Techno Property Nepal            \n")
        file.write("\t\t\t\t\tAddress: Kathmandu,Nepal  \n")
        file.write("\t\t\t\t\t   Contact:98xxxxxxxx      \n")
        file.write("---------------------------------------------------------------------------------------------------------------\n")
        file.write("Customer Details:\n")
        file.write("-------------------------------------------\n")
        file.write(f"Customer Name: {name}\n")
        file.write(f"Phone Number: {number}\n")
        file.write(f"Address: {address}\n")
        file.write(f"Date and Time: {date_time}\n")
        file.write("-------------------------------------------\n")
        file.write("Rented Land Details:\n")
        file.write("----------------------------------------------------------------------------------------------------------------\n")
        file.write("Kitta No.\t Address\t\tDirection\tArea(aana)\t  Rent Price\tMonth\t  Total Price\n")
        file.write("----------------------------------------------------------------------------------------------------------------\n")
        for land in land_rented:
            for i in land:
                file.write(str(i)+"\t\t")
            file.write("\n")
        file.write("----------------------------------------------------------------------------------------------------------------\n")
        file.write(f"\t\t\t\t\t\t\t\t\t\t\t   Grand Total:{grand_total}\n")
        file.write("----------------------------------------------------------------------------------------------------------------\n")
        file.write("*Term and Condition:\n")
        file.write("--If land is failed to return in time then 10% per Month Fine will be applied.\n")
        file.write("\n\t\t\t                      Thank You! See You Soon.")


def write_returned_land(name,number,address,date_time,land_returned,month_rent,month_return,fine,total,grand_total,fine_total,return_invoice_id):
    '''Function to generate a bill for returning Land'''
    #Generete th bill name based on customer name,number,and time of rent
    file_name=f"return_{return_invoice_id}.txt"
    #Open the file in write mode
    with open(file_name,"w") as file:
        #write shop details and headers
        file.write("\n")
        file.write("----------------\n")
        file.write(f"INVOICE ID:{return_invoice_id}\n")
        file.write("--------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t\t\t  Techno Property Nepal            \n")
        file.write("\t\t\t\t\t\t\tAddress: Kathmandu,Nepal  \n")
        file.write("\t\t\t\t\t\t\t   Contact:98xxxxxxxx      \n")
        file.write("--------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("Customer Details:\n")
        file.write("-----------------------------------------------\n")
        file.write(f"Customer Name: {name}\n")
        file.write(f"Phone Number: {number}\n")
        file.write(f"Address: {address}\n")
        file.write(f"Date and Time: {date_time}\n")
        file.write("-----------------------------------------------\n")

        file.write("Rented Land Details:\n")
        file.write("---------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("Kitta No.\t Address\t\tDirection\tArea(aana)\t Rent Price\tMonth Rented\tMonth Returned\t Total Price\t Fine Amount\n")
        file.write("---------------------------------------------------------------------------------------------------------------------------------------------------\n")
        for land in land_returned:
            for i in land:
                file.write(str(i)+"\t\t")
            file.write("\n")
        file.write("---------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t   Total:{total}\n")
        file.write(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t   Total Fine Amount:{fine_total}\n")
        file.write(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t   Grand Total:{grand_total}\n")
        file.write("---------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\n\t\t\t                             Thank You! See You Soon.")
        
