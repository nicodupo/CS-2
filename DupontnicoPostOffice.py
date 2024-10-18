'''
name: Nico Dupont
Description: algrithm for postage cost
bugs: returns wrong number when prompted
log: 1.0
features: defines postal zones and price of package type
sources: Mr.Campbell and mrs. Marciano 
'''
def main():  
    dimensions = input ("Enter data in order of length, width, height, starting zip code and ending zipcode: ") #prompts the user to give dimensions
    dimensions = dimensions.split(",") #
    length = float(dimensions[0]) #turns length into a number 
    height = float(dimensions[2]) #turns the height into a number
    width = float(dimensions[1]) #turns width into a number
    start = int(dimensions[3]) #turns your numbers into start area code
    end = int(dimensions[4]) #turns number into end area code
    mail_type =get_type(length,width,height)#makes size dependent on length, width,and height
     
    
    distance = abs(get_zone(start)- get_zone(end)) #takes ammount of area codes and sets start and end
    #mail_type = get_type(length,width,height) #make mail type depend on dimensions
    cost = get_cost (mail_type,distance) #makes cost depend on type of package and zipcodes traveled
    cost =str('%.2f'%cost)
    cost=cost.lstrip('0')
    print (cost)
def get_cost (size,zones): 
    '''
args: taking size of the user package price multiplied by ammount of zones traveled
returns: the price of the package  
raises: if the size of package or ammount of zones was negitve
    '''
    if size == "Regular Post Card": 
        return .20 +.03*zones 
    elif size == "Large Post Card": 
        return .37 +.03*zones 
    elif size == "Envelope":  
        return .37 + .04*zones 
    elif size == "Large Envelope":
        return .60 + .05*zones
    elif size =="Package":
        return 2.95 + .25*zones
    elif size == "Large Package":
        return 3.95 +.25*zones
def get_zone(zipcode):
    '''
args: defining zipcodes by setting a certain ammount of postal codes between zipcodes
returns: give back the zipecode that fits in between a certain ammount of area codes
raises: if the zipcode input did not exist
    '''
    if 1<=zipcode <=6999: #if the zipe codes are in between a certain ammount of area codes sort them into 6 different zones
        return 1
    elif 7000<=zipcode <=19999:
        return 2 
    elif 20000<=zipcode <=35999:
        return 3
    elif 36000<=zipcode <=62999:
        return 4 
    elif 63000<=zipcode <=84999:
        return 5
    elif 85000<=zipcode <=99999:
        return 6
def get_type(length,height,width):
    '''
    args: takes lengh, width and height and returns what postage type you would need to ship.
    returns: what postage type would fit your dimensional requirements
    raises: if the input was negitive or was too large to mail
    '''
    if(length >= 3.5 and length <=4.25 and height >=3.5 and height <=6 and width >=0.007 and width <=0.016): # if the length width and height are all inbetween a certain range of numbers than it is attached to a certain post card
        return "Regular Post Card"
    elif (length >= 4.25 <= length <=6 and height >=6 and height <=11.5 and width >=0.007 and width <=0.015):
        return "Large Post Card"
    elif (length >= 3.5 <= length<=6.125 and height >=5 and height <=11.5 and width >=0.016 and width <=0.25):
        return "Envelope" 
    elif (length >= 6.125<= length<=24 and height >=11 and height <=18 and width >=0.25 and width <=0.5):
        return "Large Envelope"
    elif length+2 *height+2*width<=84:
        return "Package"
    elif length+2 *height+2*width<=130:
        return "Large Package"
    else:
        "not mailable"
main()
