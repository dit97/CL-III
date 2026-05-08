#XML-RPC → XML(Stubbung/ Marshaling) + HTTP(commmuncation) protocol
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Class for factorial calculation
class FactorialServer:

    def calculate_factorial(self, number):

        if number < 0:
            return "Factorial not possible for negative numbers"

        result = 1

        for i in range(1, number + 1):
            result = result * i

        return result


# Restrict access path -- RequestHandler class is inheriting from SimpleXMLRPCRequestHandler
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server - with Automatically handles opening and closing resource
with SimpleXMLRPCServer(
    ("localhost", 8000),
    requestHandler=RequestHandler # Tells server to use custom request hanler
) as server:

    # gives information about server methods to client
    server.register_introspection_functions()

    # registers the server object so that client can remotely access its methods.
    server.register_instance(FactorialServer())

    print("Server is running on port 8000...")

    # Run server continuously
    try:
        server.serve_forever()

    except KeyboardInterrupt:
        print("Server stopped.")