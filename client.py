# Ivern Buala
# (PSU) Integrative Programming BSIT2-B1
# Enhancing Guessing Game - Client Part

import socket

# Main Variable/Host
host = "192.168.1.9"
port = 7777

# Client play the Guessing Game
def play_game():
    s = socket.socket()
    s.connect((host, port))

    # Banner Name & Display
    data = s.recv(1024)
    print("\n----- Welcome to Guessing Game! -----\n")
    print(data.decode().strip())

    while True:

        # Player/user input 
        user_input = input("").strip()
        s.sendall(user_input.encode())
        print()

        reply = s.recv(1024).decode().strip()

        if "Correct" in reply:
            print(reply)
            break

        print(reply)
        continue

    s.close()


while True:
    play_game() 
    # If yes, the entire game will start but will save the leaderboard, otherwise the game will end.
    repeat = input("\nDo you want to play Guessing Game again? (yes/no): ").strip().lower()
    if repeat != "yes":
        break
