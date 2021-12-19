#Breadth-first algorithm implementation
#Grokking Algorithms, Ch 6


#add double ended queue function
from collections import deque

#implementing the graph using dict
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

#create a function to check whether you found the person you are looking for,e.g. mango seller
def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    #create a new queue with double ends
    search_queue = deque()
    #add all neighbours for node "you" to the search queue
    search_queue += graph[name]
    #create a list of names that have already been checked
    searched = []

    #while the queue is not empty...
    while search_queue:
        #grab the first person off the queue
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

print(search("you"))