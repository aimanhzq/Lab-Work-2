def calculate_cost(room_type, num_rooms, num_nights):

    room_rates = {
        "Single": 100,
        "Double": 150,
        "Suite": 250
    }
    discount_threshold = 5
    discount_rate = 0.1
    min_suite_nights = 3
    complimentary_breakfast_nights = 7

    if room_type not in room_rates:
        print("Invalid room type. Please choose again.")
        return None

    if num_rooms <= 0 or num_nights <= 0:
        print("Number of rooms and nights must be greater than 0.")
        return None

    room_rate = room_rates[room_type]
    total_cost = room_rate * num_nights * num_rooms

    if num_rooms > discount_threshold:
        total_cost *= (1 - discount_rate)

    if room_type == "Suite" and num_nights < min_suite_nights:
        print("Minimum stay for a Suite is ONLY 3 nights.")
        return None

    if room_type == "Single" and num_nights > complimentary_breakfast_nights:
        print("You have received a complimentary breakfast voucher!")

    return total_cost


def get_room_type():

    print("Choose Your Suitable Room Types:")
    print("1. Single (RM100 per night)")
    print("2. Double (RM150 per night)")
    print("3. Suite (RM250 per night)")

    room_type = input("Enter room type (1 for Single, 2 for Double, 3 for Suite): ")
    room_types = {1: "Single", 2: "Double", 3: "Suite"}
    while room_type not in ["1", "2", "3"]:
        print("Invalid room type. Please enter number of rooms again.")
        room_type = input("Enter room type (1 for Single, 2 for Double, 3 for Suite): ")

    return room_types[int(room_type)]


if __name__ == "__main__":
    print("Welcome to Mystic Moon Hotel!")

    room_type = get_room_type()
    num_rooms = int(input("Enter number of rooms: "))
    num_nights = int(input("Enter number of nights: "))

    total_cost = calculate_cost(room_type, num_rooms, num_nights)
    if total_cost is not None:
        print(f"Total cost of reservation: RM{total_cost:.2f}")
