# Ivern Buala
# (PSU) Integrative Programming BSIT2-B1
# Enhancing Guessing Game - Server Part

import socket
import random

# Main Variable/Host
host = "192.168.1.9"
port = 7777
banner = """Input IGN/Username:"""

# Player Leaderboard Dictionary type
leaderboard = []

# Difficulty List
# Used import random for random selection of guessing number game
def generate_random_int(difficulty):
    valid_difficulties = ["easy", "medium", "hard"]

    if difficulty.lower() not in valid_difficulties:
        raise ValueError("Invalid difficulty level.\n")
    
    if difficulty == "easy":
        return random.randint(1, 50)
    elif difficulty == "medium":
        return random.randint(1, 100)
    elif difficulty == "hard":
        return random.randint(1, 500)

# Client Handler
def client_handler(conn, addr):
    try:
        conn.sendall(banner.encode())

        # Player Connect
        player_name = conn.recv(1024).decode().strip()
        print(f"Player {player_name} has joined the game.")

        # Difficulty selection loop
        while True:
            conn.sendall(b"Choose Difficulty (easy, medium, hard):\n")
            difficulty = conn.recv(1024).decode().strip().lower()

            try:
                generate_random_int(difficulty)
                break  # Break the loop if the difficulty is valid
            except ValueError as e:
                conn.sendall(str(e).encode())

        # Guessing Game (Main Loop)
        while True:
            guessme = generate_random_int(difficulty)
            conn.sendall(b"Guess the Number: \n")
            game_attempts = 0
            
            # Loop
            while True:
                try:
                    client_input = conn.recv(1024)

                    # if player left the game
                    if not client_input:
                        print(f"Player {player_name} has left the game.")
                        return
                    
                    guess = int(client_input.decode().strip())
                    game_attempts += 1

                    # If player guessed the Correct Answer 
                    if guess == guessme:
                        score = 100 // game_attempts
                        conn.sendall(f"Correct Answer!\nYour score: {score}\n".encode())

                        # Leaderboard & Player number of attempts
                        leaderboard.append({'name': player_name, 'score': score, 'difficulty': difficulty})
                        print(f"Player {player_name} guessed the correct number in just {game_attempts} attempts!")
                        break
                    
                    # Guess Lower/Higher elif statement
                    elif guess > guessme:
                        conn.sendall(b"Guess Lower!\n")

                    elif guess < guessme:
                        conn.sendall(b"Guess Higher!\n")

                # If player closed the game or by the host
                except ConnectionResetError:
                    print(f"Player {player_name} connection closed by the host.")
                    return

    except ConnectionAbortedError:
        print(f"Player {player_name} connection stopped.")

    finally:
        conn.close()

# Display Leaderboard (Persistence)
def show_leaderboard():
    global leaderboard

    print("\n----- Player Leaderboard -----\n")
    for i, player in enumerate(sorted(leaderboard, key=lambda x: x['score'], reverse=True)):
        print(f"Player Rank - {i+1}")
        print(f"Player Name: {player['name']}")
        print(f"Player Score: {player['score']}")
        print(f"Player Last Difficulty: {player['difficulty']}\n")

    # The Player Score gets divided by two once the player/user did not guess the correct answer.

# Socket feature
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)


print(f"Server Port: {port}")

while True:
    conn, addr = s.accept()
    print(f"New Player connection from {addr}")
    client_handler(conn, addr)

    # Show leaderboard after each player finishes
    show_leaderboard()
