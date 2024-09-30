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
    width = float(dimensions[1]) #turns width into a number
    height = float(dimensions[2]) #turns the height into a number
    start = int(dimensions[3]) #turns your numbers into start area code
    end = int(dimensions[4]) #turns number into end area code
    size =get_type(length,width,height)#makes size dependent on length, width,and height
     
    
    distance = abs(get_zone(start)- get_zone(end)) #takes ammount of area codes and sets start and end
    mail_type = get_type(length,width,height) #make mail type depend on dimensions
    cost = get_cost (mail_type,distance) #makes cost depend on type of package and zipcodes traveled
    print (cost)
def get_cost (size,zones): 
    '''
args: taking size of the user package price multiplied by ammount of zones traveled
returns: the price of the package  
raises: if the size of package or ammount of zones was negitve
    '''
    if size == "regular post card": 
        return .20 +.03*zones 
    elif size == "large post card": 
        return .37 +.03*zones 
    elif size == "envelope":  
        return .37 + .04*zones 
    elif size == "large envelope":
        return .60 + .05*zones
    elif size =="package":
        return 2.95 + .25*zones
    elif size == "large package":
        return 3.95 +.25*zones
def get_zone(zipcode):
    '''
args: defining zipcodes by setting a certain ammount of postal codes between zipcodes
returns: give back the zipecode that fits in between a certain ammount of area codes
raises: if the zipcode input did not exist
    '''
    if 1<=zipcode <=6999: #if the zipe codes are in between a certain ammount of area codes sort them into 6 different zones
        return 1
    elif 2<=zipcode <=7000:
        return 2 
    elif 3<=zipcode <=20000:
        return 3
    elif 4<=zipcode <=36000:
        return 4 
    elif 5<=zipcode <=63000:
        return 5
    elif 5<=zipcode <=85000:
        return 6

def get_type(length,width,height):
    '''
    args: takes lengh, width and height and returns what postage type you would need to ship.
    returns: what postage type would fit your dimensional requirements
    raises: if the input was negitive or was too large to mail
    '''
    if(3.5<= length<=4.25 and width >=0.007 and width <=0.016 and height >=3.5 and height <=6): # if the length width and height are all inbetween a certain range of numbers than it is attached to a certain post card
        return "Regular Post Card"
    elif (4.25<= length<=6 and width >=0.007 and width <=0.015 and height >=6 and height <=11.5):
        return "Large Post Card"
    elif (3.5<= length<=6.125 and width >=0.016 and width <=0.25 and height >=5 and height <=11.5):
        return "envelope" 
    elif (6.125<= length<=24 and width >=0.25 and width <=0.5 and height >=11 and height <=18):
        return "Large envelope"
    elif length+2 *height+2*width<=84:
        return "package"
    elif length+2 *height+2*width<=130:
        return "large package"
    else:
        "not mailable"
main()
 