# Importing 
import hub
import utime, os, ujson
import secrets as p
from Backpack_Code import Backpack

# Fill in with the name of your AirTable (tip: the ESP doesn't like spaces)
# Also fill in the name of the field column you want the values to be updated in!!!
####################################
table = 'Table1'
field = 'Name'
####################################

# The code below runs on the ESP!
commands = '''
\x05
import ESPClient, ujson
ESPClient.wifi('SSID','PASS')
PORT = 443
base='api.airtable.com'
Key = 'Bearer KEY'
request='%s /v0/%s/%s HTTP/1.1\\r\\n'
request += 'Host: %s\\r\\n' % base
request += 'Content-Type: application/json\\r\\n'
request += 'Accept: application/json\\r\\n'
request += 'Authorization: %s\\r\\n' %Key
    
def readIt(table): 
    req = request % ('GET','docID',table)
    req += '\\r\\n'
    code, reason, reply = ESPClient.REST(base, PORT, req, False)
    try:
        if code == 200:
            Json = reply.split("\\r\\n")[-3]
            response = ujson.loads(Json)['rows'][0]
            return code, response[property]
        else:
            return code, reason
    except:
        return (-1, reply)

def writeIt(table, field, value):
    payload = {"records": [{"fields": {  field: value}} ]}
    payload = ujson.dumps(payload)
    req = request % ('POST','docID',table)   
    req += 'Content-Length: %d\\r\\n\\r\\n' % len(payload)
    req += '%s\\r\\n\\r\\n' % payload

    code, reason, reply = ESPClient.REST(base, PORT, req, True)
    try:
        if code == 200:
            return code, reply
        else:
            return code, reason
    except:
        return (-1, reply)
\x04
'''

# Replacing all the passwords from the secrets.py doc 
commands = commands.replace('SSID',p.SSID)
commands = commands.replace('PASS',p.KEY)
commands = commands.replace('KEY',p.tsATappkey)
commands = commands.replace('docID',p.ATdocID)

dongle = Backpack(hub.port.C, verbose = True) 
# if verbose is true you can switch to the backpack mode 

# functions calling dongle.ask() (esp)
def configure():
    if not dongle.setup(): return False
    for cmd in commands.split('\n'):
        if not dongle.EOL(dongle.ask(cmd)) : return False
    return True

def grab():
    dongle.ask()
    reply = dongle.ask('readIt("%s")' % (table))
    try:
        print(reply)
        return reply.split('\r\n')[-2]
    except: 
        return None
        
def set(value):
    dongle.ask()
    reply = dongle.ask('writeIt("%s","%s","%s")' % (table, field, value))
    dongle.ask()
    try:
        return reply.split('\r\n')[1]
    except: 
        return None
         
configure()


############### YOU CAN CHANGE (SOME) CODE BELOW HERE !!!!! #######################


# Fill in this part with how you initialize your SPIKE! 
############################
legR = hub.port.A.motor                                                                                    
legL = hub.port.E.motor                                                                                    
legR.mode(2)                                                                                               
legL.mode(2)

begR = legR.get()[0]
begL = legL.get()[0]

sitR = begR-60
sitL = begL-60
############################

# Fill in your functions for sit and stand or any other two types of SPIKE movement!

#######################################
def sit():
    print('sitting')
    legR.run_to_position(sitR, 30)
    legL.run_to_position(sitL,30)

def stand():
    print('standing')
    legR.run_to_position(begR,50)
    legL.run_to_position(begL,50)
#######################################

# Main while loop 
while True:
    # Grab airtable data and parse 
    ret=grab()
    retS=eval(ret)
    retJ=ujson.loads(retS[1])
    name=retJ['records'][0]['fields']['Name']  #<------- REPLACE ['Name'] with your field name 
    print(name).  # prints out what you get back from AirTable
    

    # Customize to have the SPIKE respond to the values you are pulling from AirTable 
    if name == 'sit':
        sit()
        utime.sleep(0.5)
    else:
        stand()
        utime.sleep(0.5)
