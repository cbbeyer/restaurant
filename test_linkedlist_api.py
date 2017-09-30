from linkedlist_api import LinkedList

def LinkedList_Create():
    ll = LinkedList()
    # add assert equal

def LinkedList_GetOutOfBounds():
    try:
        ll.get(5)
    except Exception as e:
        print('Error: {}'.format(e))

    
