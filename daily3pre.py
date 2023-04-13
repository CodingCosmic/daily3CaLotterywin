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



def generate_random_sequences(num_sets=4, seq_length=3, min_value=0, max_value=9):
    sequences = []
    for _ in range(num_sets):
        sequence = [random.randint(min_value, max_value) for _ in range(seq_length)]
        sequences.append(sequence)
    return sequences

def main():
    sets_count = 2
    for i in range(sets_count):
        sequences = generate_random_sequences()
        print(f"Set {i + 1}: {sequences}")

        # Ask user if they want to generate another set
        if i < sets_count - 1:
            user_input = input("Do you want to generate another set of random sequences? (y/n): ")
            if user_input.lower() != "y":
                break

if __name__ == "__main__":
    main()
def main():
    print_ansi_header()  # Add this line to call the print_ansi_header function

    sets_count = 2
    for i in range(sets_count):
        sequences = generate_random_sequences()
        print(f"Set {i + 1}: {sequences}")

        # Ask user if they want to generate another set
        if i < sets_count - 1:
            user_input = input("Do you want to generate another set of random sequences? (y/n): ")
            if user_input.lower() != "y":
                break

if __name__ == "__main__":
    main()
