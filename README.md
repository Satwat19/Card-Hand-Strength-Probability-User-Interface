🃏 Card Hand Strength Probability Calculator
📖 Overview

This project is a simple graphical user interface (GUI) application that calculates the probability of achieving a specific card hand in poker (e.g., flush, straight, full house, etc.).
It allows users to input different parameters — such as the number of cards in hand and the desired outcome — and computes the probability based on combinatorial mathematics.

💡 Features

User-friendly interface built using Tkinter.

Calculates probabilities using combination formulas.

Real-time display of the result.

Input validation to prevent incorrect entries.

⚙️ Inputs

The GUI contains four input fields:

Cards in Hand – Number of cards you currently hold (e.g., 2).

Community Cards – Number of shared cards on the table (e.g., 3).

Desired Outcome Cards – Total cards required for the desired hand (e.g., 4).

Cards Needed for Outcome – How many more cards are needed to complete that hand (e.g., 3).

🧮 Formula Used

The probability is calculated using combinations:

𝑃
=
(
𝑑
𝑒
𝑠
𝑖
𝑟
𝑒
𝑑
𝑛
𝑒
𝑒
𝑑
𝑒
𝑑
)
×
(
𝑟
𝑒
𝑚
𝑎
𝑖
𝑛
𝑖
𝑛
𝑔
𝑎
𝑣
𝑎
𝑖
𝑙
𝑎
𝑏
𝑙
𝑒
−
𝑛
𝑒
𝑒
𝑑
𝑒
𝑑
)
(
𝑡
𝑜
𝑡
𝑎
𝑙
𝑎
𝑣
𝑎
𝑖
𝑙
𝑎
𝑏
𝑙
𝑒
)
P=
(
available
total
	​

)
(
needed
desired
	​

)×(
available−needed
remaining
	​

)
	​


Where:

desired = desired outcome cards

needed = cards needed for the outcome

remaining = remaining cards in deck after yours

available = cards you can still draw

total = total number of cards left in the deck

This formula essentially measures how likely it is to draw the right combination of cards needed for a winning hand.

🧰 How to Run

Open CMD and navigate to the folder containing the file:

cd Desktop


Run the program using:

python card_hand_probability.py


Enter your values and click "Calculate Probability" to get the result.

🖥️ Example

For example:

Cards in Hand: 2

Community Cards: 3

Desired Outcome Cards: 4

Cards Needed for Outcome: 3

The program will calculate and display a probability (e.g., 0.02%).

👤 Developer

Name: Satwat Rahman
Batch: BSEE 2022-2026
Department: Electrical Engineering
