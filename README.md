# Rock-paper-Scissors-game

A simple Python implementation of the classic Rock-Paper-Scissors game. This interactive game lets you play against the computer.

**How to Play**
------------------



1.Choose your option:

          0 for Rock 🪨

  
          1 for Paper 📄

  
          2 for Scissors ✂️
  
2.The computer will randomly select its option.

3.The game will determine the winner based on the rules:

        ->Rock beats Scissors
        
        ->Scissors beats Paper
        
        ->Paper beats Rock
        
4.Invalid inputs will result in an automatic loss.




**Features**
--------------------
->User-friendly and interactive gameplay.

->Randomized computer choices using the **random** module.

->Handles invalid user inputs gracefully.


**Getting Started**
--------------------
**Prerequisites**

->Python 3.x installed on your system.

**Running the Game**
1.Clone the repository:


2.Navigate to the project directory:

        cd rock-paper-scissors

        
3.Run the script:

**Code Overview**
-----------------
The code uses a list to store the three game options and the random module to simulate the computer's choice. It includes a series of conditional statements to compare the user's choice with the computer's choice and determine the winner.

**Key sections:**

**User Input Validation**: Ensures the user enters a valid number (0, 1, or 2).

**Game Logic**: Implements the rules of Rock-Paper-Scissors to decide the outcome.

**Randomized Computer Choice**: Makes the game unpredictable and fair.


**Example Output**
-----------------

      What do you choose? Type 0 for Rock, Type 1 for Paper, Type 2 for Scissors: 0  
      rock  
      Computer choice:  
      scissors  
      You win! 

**Contributing**
-----------------
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

**License**
--------------
This project is licensed under the MIT License.



