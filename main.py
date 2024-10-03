from collections import deque
import time
import random


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


def lottery(people: Queue)->deque:
    if people.size() > 0:

        # Convert 'people' deque to list to randomize the names
        people_list = list(people.queue)
        # Shuffle the people_list
        random.shuffle(people_list)
        # Convert the list to deque
        randomized_deque_people = deque(people_list)
        # Run a while loop to remove people from the left or front (FIFO) until it reaches four
        while len(randomized_deque_people) > 4:
            randomized_deque_people.popleft()
            if len(randomized_deque_people) == 4:
                return randomized_deque_people
        return randomized_deque_people


if __name__ == "__main__":
    print("WELCOME TO THE SPACESHIP TO TRAVEL TO MARS")
    time.sleep(2)
    print("LET'S GET THE BOARDING STARTED. CATEGORIES ARE: CHILDREN, TEEN, ADULT")

# Create an instance of Queue()
    space_traveler = Queue()
    categories = ["Children", "Teen", "Adult", "Old"]
    # Track total number of people boarding the spaceship
    total_people = 0
    # Take user based on their age
    for category in categories:
        # Space travelers are in the deque
        space_traveler.enqueue("John")
        space_traveler.enqueue("Nana")
        space_traveler.enqueue("Maria")
        space_traveler.enqueue("Eva")
        space_traveler.enqueue("Jack")
        space_traveler.enqueue("Terry")
        space_traveler.enqueue("Jack")
        space_traveler.enqueue("Terry")
        space_traveler.enqueue("Aunik")
        print(
            f"{category} SHOULD BOARD NOW. Remember - We can only take 4 {category} at once. So, we will go through a lottery process")
        # Call the lottry function to randomly select four people
        lucky_people = lottery(space_traveler)
        total_people += len(lucky_people)
        print(f"Lucky {category}", lucky_people)
        time.sleep(2)
        print(f"Drop off the {category} to Mars")
        #     Run a while loop to drop off the people (FIFO) method to Mars
        while True:
            space_traveler.dequeue()
            if space_traveler.is_empty():
                break

        print(f"Four seats are empty in the spaceship since {category}  dropped off to Mars: ", space_traveler.size())
        print()

    print()
    print("...SUMMARY...")
    print("Total People boarded on the spaceship: ", total_people)









