# Rock ✊, Paper ✋, Scissors ✌️, Lizard 🦎, Spock 🖖

A Python command-line implementation of the classic *Big Bang Theory*-inspired game — an extended version of Rock-Paper-Scissors with two extra elements: **Lizard** and **Spock**.

## About the Game

This variant was popularized by the TV show *The Big Bang Theory*. It expands the traditional 3-option game into 5 options, each with two ways to win, making draws less frequent.
link - https://youtu.be/eVYvIaV7N6o?si=I61Zfq1XU2ZpnGT3

## Rules

- **Scissors** cut **Paper**
- **Paper** covers **Rock**
- **Rock** crushes **Lizard**
- **Lizard** poisons **Spock**
- **Spock** smashes **Scissors**
- **Scissors** beat **Lizard**
- **Lizard** eats **Paper**
- **Paper** disproves **Spock**
- **Spock** vaporizes **Rock**
- **Rock** breaks **Scissors**

## How It Works

1. The program displays the rules at the start.
2. The user selects a choice by entering a number:
   - `1` = Rock ✊
   - `2` = Paper ✋
   - `3` = Scissors ✌️
   - `4` = Lizard 🦎
   - `5` = Spock 🖖
3. The computer randomly selects one of the five options.
4. Both choices are displayed, followed by the result:
   - **Computer Wins**
   - **User Wins**
   - **It's a Tie**
5. Each result includes the specific rule that determined the outcome (e.g., *"Scissors cut Paper"*).

## How to Run

1. Make sure Python 3 is installed.
2. Save the script as `rock_paper_scissors_lizard_spock.py`.
3. Run it from the terminal:

   ```bash
   python rock_paper_scissors_lizard_spock.py
   ```

4. Enter a number between 1 and 5 when prompted.

## Example Output

```
What do you choose (1)Rock (2)Paper (3)Scissors (4)Lizard (5)Spock : 1
Your choice : Rock ✊
computer's choice : Paper ✋

Result : Computer Wins
Reason : Paper ✋ covers Rock ✊.
```

## Notes

- Entering a number outside 1–5 will display an "enter a valid number" message and end the game.
- The game currently runs for a single round per execution.

## License

This project is free to use and modify for personal or educational purposes.

