import random

def print_ansi_header():
    red = "\033[31m"
    green = "\033[32m"
    blue = "\033[34m"
    reset = "\033[0m"

    print(f"{red} ██████╗{reset}{green} ██████╗{reset}{blue}  ██████╗{reset}")
    print(f"{red}██╔════╝{reset}{green}██╔═══██╗{reset}{blue}██╔════╝{reset}")
    print(f"{red}██║     {reset}{green}██║   ██║{reset}{blue}╚█████╗{reset} ")
    print(f"{red}██║     {reset}{green}██║   ██║{reset}{blue} ╚═══██╗{reset}")
    print(f"{red}╚██████╗{reset}{green}╚██████╔╝{reset}{blue}██████╔╝{reset}")
    print(f"{red} ╚═════╝{reset}{green} ╚═════╝ {reset}{blue}╚═════╝{reset} ")


def generate_random_numbers():
    return [random.randint(0, 9) for _ in range(3)]

def play_lottery(playstyle, user_numbers, winning_numbers):
    if playstyle == "straight":
        return user_numbers == winning_numbers
    elif playstyle == "box":
        return sorted(user_numbers) == sorted(winning_numbers)
    elif playstyle == "straight/box":
        return user_numbers == winning_numbers or sorted(user_numbers) == sorted(winning_numbers)

def main():
    playstyles = ["straight", "box", "straight/box"]
    print("Welcome to the Daily 3 Lottery!\n")
    
    user_input = input("Enter 'q' for Quick Pick or type 3 numbers between 0-9 separated by spaces: ")
    if user_input.lower() == "q":
        user_numbers = generate_random_numbers()
    else:
        user_numbers = list(map(int, user_input.split()))

    playstyle_input = input("Choose your playstyle (straight, box, straight/box): ")
    playstyle = playstyle_input.lower()
    while playstyle not in playstyles:
        playstyle = input("Invalid input. Choose your playstyle (straight, box, straight/box): ").lower()

    winning_numbers = generate_random_numbers()
    print(f"Winning numbers: {winning_numbers}")

    is_winner = play_lottery(playstyle, user_numbers, winning_numbers)
    if is_winner:
        print("Congratulations! You won!")
    else:
        print("Sorry, better luck next time.")

if __name__ == "__main__":
    main()
