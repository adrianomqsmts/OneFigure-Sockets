import socket
import json


def client(host='localhost', port=8082, data=None):

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server
    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)
    sock.connect(server_address)
    # Send data
    try:
        # Send data

        #data = {
        #  "id": "1",
        #}

        # convert into JSON:
        y = json.dumps(data)

        # the result is a JSON string:
        print(y)
        message = y
        amount = len(message)
        print("Sending %s" % message)
        sock.sendall(message.encode('utf-8'))
        # Look for the response
        # amount_received = 0
        # amount_expected = len(message)
        # while amount_received < amount_expected:
        data = sock.recv(3000)
            # amount_received += len(data)
        print("Received: %s" % data)
    except socket.error as e:
        print("Socket error: %s" % str(e))
    except Exception as e:
        print("Other exception: %s" % str(e))
    finally:
        print("Closing connection to the server")
        sock.close()
        data = json.loads(data)
        if(data['authenticated']):
            return data
        else:
            return 0
