import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        self.connections[connection_id] = connection_load
        # Add the connection to the dictionary with the calculated load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for load in self.connections.values():
            total += load
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())

#Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        server = self.ensure_availability(server)
        server.add_connection(connection_id)
        self.connections[connection_id] = server
        
        # Add the connection to the dictionary with the selected server
        # Add the connection to the server

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        self.connections[connection_id].close_connection(connection_id)
        del self.connections[connection_id]
        
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        avg_load = 0
        server_num = len(self.servers)
        for ser in self.servers:
            avg_load += ser.load()
        avg_load = avg_load/server_num
        return avg_load

    def ensure_availability(self,server):
        """If the average load is higher than 50, spin up a new server"""
        for ser in self.servers:
            if ser.load() < 50:
                if server.load() < 50:
                    return server
                else:
                    return ser
        self.servers.append(Server())
        return self.servers[-1]

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
#End Portion 2#

# server = Server()
# server.add_connection("192.168.1.1")
# print(server.connections)

l = LoadBalancing()
# l.add_connection("fdca:83d2::f20d")
# print(l.avg_load())
# l.servers.append(Server())
# print(l.avg_load())

# l.close_connection("fdca:83d2::f20d")
# print(l.avg_load())

for connection in range(20):
    l.add_connection(connection)
print(l)
print(l.avg_load())