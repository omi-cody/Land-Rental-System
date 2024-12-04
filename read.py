def read_a_file():
    '''This function helps to read the Land file'''
    land_dict={}#Initialize an empty dictionary to store land information
    try:
        #Open the file "land.txt" in read mode
        with open("land.txt","r") as file:
            #Iterate over each line in the file
            for kitta_no,line in enumerate(file,101):
                #Remove leading/trailing whitespaces from the line
                line=line.strip()
                #Split the line using comma as the seperator 
                land_details=line.split(",")
                 #Add land details to the dictionary using kiita number as  key
                land_dict[kitta_no]=land_details
    except:
        print("File Not Found")
    #Return the dictionary containing land information
    return land_dict
#print(read_a_file())#for debugging
def read_invoice():
    '''this function read the rented land detail of given invoice id'''
    while True:
    #open the bill of given invoice id
        try:
            invoice_id=int(input("\nEnter the Invoice ID of Bill:"))
            file=f"rent_{invoice_id}.txt"
            with open(file,"r") as rent_bill:
                rent_invoice={}#initialize a empty dictionary to store rented land detail
                line=rent_bill.readlines()
                #iterate over land details lines only
                for i in line[18:len(line)-7]:
                    d=i.replace("\n","")
                    d=d.replace("\t\t",",")
                    d=d.split(",")
                    key=d[0]
                    value=[]
                    for j in range(1,len(d)):
                        value.append(d[j])
                #add the rented land details in dictionary using kitts number as key
                    rent_invoice[key]=value
                return line,rent_invoice,invoice_id
        except:
            print("Invalid Invoice Id.Please Enter Valid Invoice Id.")
    
    
