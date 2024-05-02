
# Guessing Game v1.0

Guessing Game v1.0 with *Sockets & Randomization* for Number Guessing. Used Python as the programming language, included the socket and random as the main imports.

- Enhanced by Ivern Buala
- Prof: Sir Roy Dosado
- BSIT 2 BLOCK 1
- Palawan State University

## Features

1. user/client can repeat the game without disconnecting
2. user can choose difficulty based on the generated random number to guess

- a. easy (1-50)
- b. medium (1-100)
- c. hard (1-500)

### Enhanced features added

1. the game has implemented a scoring mechanism based on the number of tries the user guesses the number to guess (less tries the better), with a  provided player leaderboard which contains the name of the user and her/his score which is displayed after the user/client disconnects from the server. This is where also the import random has been added for the number guessing.
   
2. persistence - the server has added saving the user's name, his/her score, and the last chosen difficulty (should default to easy) into a file and this file will be loaded/updated during leaderboard display and when the user set's the difficulty.



## Server Code Procedure

- The server script begins by importing necessary modules and defining the main variables, including the host IP, port, and a banner message or the main header.
  
- Next it initializes an empty list to store player leaderboard info.
  
- There's a function `generate_random_int(difficulty)` which generates a random number based on the selected difficulty level.
  
- There is also a `ValueError/Input Error Handling` inside the function above this message when the player or user accidently types an invalid text or word.
  
- The `client_handler` function manages each client connection. It prompts the player to input their name and select a difficulty level for the game. Then, it initiates the guessing game loop.
  
- Inside the guessing game loop, the server sends prompts to the client to guess the number. It keeps track of the number of attempts and informs the client if the guess is correct or not.
  
- After each game, the player's score or his/her stats are added to the leaderboard, and the leaderboard will be shown.
  
- The server listens for incoming connections which loops and handles each connection by calling the `client_handler` function.

## Client Code Procedure

- The client script establishes a connection to the server using the host IP and a specific port. This part host-IP and the port can be changed depending on your IP Address and host.
  
- Next it defines a function `play_game()` to manage the gameplay loop of the enhanced Guessing Game.
  
- Inside the loop, the client receives the banner message from the server and displays it.
  
- The client will continue prompting the player for input and sends it to the server side code.
  
- After each guess, the client receives feedback from the server, indicating if the guess answer was correct or incorrect.
  
- If the guess is correct, the game loop breaks, and the client asks the user if they want to play again. If the user chooses to play again, the game loop restarts; Otherwise the game will end or the client script will terminate.
