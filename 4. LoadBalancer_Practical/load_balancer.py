import random


# Server Class
class Server:
    def __init__(self, name):
        self.name = name
        self.connections = 0
        
    def __str__(self):
        return self.name
        
    def connect(self):
        self.connections += 1

    def disconnect(self):
        if self.connections > 0:
            self.connections -= 1

# Load Balancer Class
class LoadBalancer:

    def __init__(self, servers):
        self.servers = [Server(name) for name in servers]
        self.server_index_rr = 0

    # Round Robin
    def round_robin(self):
        server = self.servers[self.server_index_rr]
        self.server_index_rr = (
            self.server_index_rr + 1
        ) % len(self.servers)
        return server

    # Random Selection
    def random_selection(self):
        return random.choice(self.servers)

    # Least Connection
    def least_connection(self):
        return min(
            self.servers,
            key=lambda server: server.connections)


# Simulate Requests
def simulate_client_requests(load_balancer, num_requests):

    for i in range(num_requests):

        print(f"\nRequest {i + 1}")

        # Round Robin
        server_rr = load_balancer.round_robin()
        server_rr.connect()
        print(f"Round Robin -> {server_rr}")

        # Random
        server_random = (load_balancer.random_selection())
        server_random.connect()
        print(f"Random -> {server_random}")

        # Least Connection
        server_lc = (load_balancer.least_connection())
        server_lc.connect()
        print(f"Least Connection -> {server_lc}")

        # Disconnect after processing
        server_rr.disconnect()
        server_random.disconnect()
        server_lc.disconnect()


# Main Program
if __name__ == "__main__":

    servers = [
        "Server A",
        "Server B",
        "Server C"
    ]

    load_balancer = LoadBalancer(servers)

    simulate_client_requests(
        load_balancer,
        10
    )