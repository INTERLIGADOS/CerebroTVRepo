import socket

""" Returns the local IP of the interface that connects with address
"""
def getLocalIP(address):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        s.connect((address, 9))
        client = s.getsockname()[0]
    except socket.error as e:
        print "Error getting the local IP " + str(e)
        client = None
    finally:
        del s
    return client

def returnHTTPError(request, errorcode, errorresponse, debugprint=None):
    if debugprint:
        print debugprint
    request.setResponseCode(errorcode)
    return errorresponse

