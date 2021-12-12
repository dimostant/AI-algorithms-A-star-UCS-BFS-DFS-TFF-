import heapq
import sys

max_possible_value = sys.maxsize

class PriorityQueue(object):
    """
    A queue structure where each element is served in order of priority.
    Elements in the queue are popped based on the priority with higher priority
    elements being served before lower priority elements.  If two elements have
    the same priority, they will be served in the order they were added to the
    queue.
    Traditionally priority queues are implemented with heaps, but there are any
    number of implementation options.
    (Hint: take a look at the module heapq)
    Attributes:
        queue (list): Nodes added to the priority queue.
    """

    def __init__(self):
        """Initialize a new Priority Queue."""

        self.queue = []

    def pop(self):
        """
        Pop top priority node from queue.
        Returns:
            The node with the highest priority.
        """
        return heapq.heappop(self.queue)

    def remove(self, node_id):
        """
        Remove a node from the queue.
        This is a hint, you might require this in ucs,
        however, if you choose not to use it, you are free to
        define your own method and not use it.
        Args:
            node_id (int): Index of node in queue.
        """
        self.queue.pop(node_id)
        heapq.heapify(self.queue)

    def __iter__(self):
        """Queue iterator."""

        return iter(sorted(self.queue))

    def __str__(self):
        """Priority Queue to string."""

        return 'PQ:%s' % self.queue

    def append(self, node):
        """
        Append a node to the queue.
        Args:
            node: Comparable Object to be added to the priority queue.
        """
        heapq.heappush(self.queue, node)

    def __contains__(self, key):
        """
        Containment Check operator for 'in'
        Args:
            key: The key to check for in the queue.
        Returns:
            True if key is found in queue, False otherwise.
        """

        return key in [n for _, n in self.queue]

    def __eq__(self, other):
        """
        Compare this Priority Queue with another Priority Queue.
        Args:
            other (PriorityQueue): Priority Queue to compare against.
        Returns:
            True if the two priority queues are equivalent.
        """

        return self.queue == other.queue

    def size(self):
        """
        Get the current size of the queue.
        Returns:
            Integer of number of items in queue.
        """

        return len(self.queue)

    def clear(self):
        """Reset queue to empty (no nodes)."""

        self.queue = []

    def top(self):
        """
        Get the top item in the queue.
        Returns:
            The first item stored in teh queue.
        """

        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return 0, None

def pop_frontier(frontier):
    if len(frontier) == 0:
        return None
    # copied_list = frontier.copy()
    min = max_possible_value
    max_values = []
    for key, path in frontier:
        if key == min:
            max_values.append(path)
        elif key < min:
            min = key
            max_values.clear()
            max_values.append(path)

    max_values = sorted(max_values, key=lambda x: x[-1])
    # max_values.sort()
    desired_value = max_values[0]
    frontier.remove((min, max_values[0]))
    return min, desired_value


def get_frontier_params_new(node, frontier):
    for i in range(len(frontier)):
        curr_tuple = frontier[i]
        cost, path = curr_tuple
        if path[-1] == node:
            return True, i, cost, path

    return False, None, None, None


#custom implementations, test to see if they are accurate ~ for Dimos
# def pop_frontier(frontier):
#     return frontier[0][0], frontier[0][1]

# def get_frontier_params_new(neighbour, frontier):
#     print("\n \n \n" , neighbour, frontier)
#     is_there = False
#     for _ in frontier :
#         if neighbour == _ : 
#             is_there = True

#     if is_there == False :
#         indexx = None 
#         neighbour_old_cost = 0

#     #Calculate cost if neighbour exists 
    
#   return  is_there, indexx, neighbour_old_cost
