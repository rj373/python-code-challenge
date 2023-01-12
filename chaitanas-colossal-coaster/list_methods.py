"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    ab=[person_name]
    if ticket_type==1:
        return express_queue+ab
    else:
        return normal_queue+ab
def find_my_friend(queue, friend_name):
    for i in range(len(queue)):
        if queue[i]==friend_name:
            return i
        else:
            pass
def add_me_with_my_friends(queue, index, person_name):
    queue.insert(index,person_name)
    return queue
def remove_the_mean_person(queue, person_name):
    queue.remove(person_name)
    return queue
def how_many_namefellows(queue, person_name):
    return queue.count(person_name)
def remove_the_last_person(queue):
    a=queue[-1]
    queue.remove(a)
    return str(a)
def sorted_names(queue):
    queue.sort()
    return queue
