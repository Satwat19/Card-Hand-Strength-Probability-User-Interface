import tkinter as tk
from tkinter import messagebox
import math

# Function to calculate combinations
def comb(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# Function to calculate hand probability
def calculate_probability():
    try:
        # Input values
        hand_cards = int(hand_cards_entry.get())
        community_cards = int(community_cards_entry.get())
        desired_outcome_cards = int(desired_outcome_entry.get())
        total_outcome_cards = int(total_outcome_entry.get())

        # Remaining cards in the deck
        remaining_deck_cards = 52 - (hand_cards + community_cards)

        # Total possible outcomes (drawing cards from the remaining deck)
        total_possible = comb(remaining_deck_cards, total_outcome_cards)

        # Favorable outcomes (drawing desired cards from remaining cards)
        favorable_outcomes = comb(desired_outcome_cards, total_outcome_cards)

        # Probability calculation
        probability = (favorable_outcomes / total_possible) * 100

        result_label.config(text=f"Probability: {probability:.2f}%")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("Card Hand Strength Probability")
root.geometry("500x600")  # Adjusted window size for better fit

# Add a banner image (resized to fit the window width)
try:
    banner_image = tk.PhotoImage(file=r"C:\\Users\\user\\Downloads\\banner.png")  # Replace with your banner image path
    banner_image = banner_image.subsample(2, 2)  # Resize the image to fit the window
    banner_label = tk.Label(root, image=banner_image)
    banner_label.grid(row=0, column=0, columnspan=2, pady=10)
except Exception as e:
    tk.Label(root, text="Card Hand Strength Probability", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

# Inputs
tk.Label(root, text="Cards in Hand:").grid(row=1, column=0, padx=10, pady=5)
hand_cards_entry = tk.Entry(root)
hand_cards_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Community Cards:").grid(row=2, column=0, padx=10, pady=5)
community_cards_entry = tk.Entry(root)
community_cards_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Desired Outcome Cards:").grid(row=3, column=0, padx=10, pady=5)
desired_outcome_entry = tk.Entry(root)
desired_outcome_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Cards Needed for Outcome:").grid(row=4, column=0, padx=10, pady=5)
total_outcome_entry = tk.Entry(root)
total_outcome_entry.grid(row=4, column=1, padx=10, pady=5)

# Add a decorative image (resized)
try:
    decorative_image = tk.PhotoImage(file=r"C:\\Users\\user\\Downloads\\decorative.png")  # Replace with your decorative image path
    decorative_image = decorative_image.subsample(2, 2)  # Resize the image to fit the window
    decorative_label = tk.Label(root, image=decorative_image)
    decorative_label.grid(row=5, column=0, columnspan=2, pady=10)
except Exception:
    pass  # If the image fails to load, just skip it

# Calculate button
calculate_button = tk.Button(root, text="Calculate Probability", command=calculate_probability, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
calculate_button.grid(row=6, column=0, columnspan=2, pady=10)

# Result display
result_label = tk.Label(root, text="Probability: -", font=("Arial", 12, "bold"))
result_label.grid(row=7, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
