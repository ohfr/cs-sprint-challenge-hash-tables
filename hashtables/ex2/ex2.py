#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    lookup = {}

    route = [None] * length

    for ticket in tickets:
        lookup[ticket.source] = ticket.destination
    
    route[0] = lookup["NONE"]

    for i in range(1, length):
        route[i] = lookup[route[i-1]]

    return route


# reconstruct_trip([
#     Ticket("NONE", "LAX"), Ticket("LAX", "SFO"), Ticket("SFO", "BHM"), Ticket("BHM", "FLG"), Ticket("FLG", "XNA"), Ticket("XNA", "CID"), Ticket("CID", "SLC"), Ticket("SLC", "PIT"), Ticket("PIT", "ORD"), Ticket("ORD", "NONE")], 10)