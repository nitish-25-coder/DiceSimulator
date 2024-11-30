import random
import tkinter as tk
from PIL import Image, ImageTk
import time

# Function to roll the dice with animation and print the result before completing the animation
def roll_dice_animation():
    """Simulate dice rolling with animation before showing the result."""
    # Determine the final outcome before starting the animation
    final_value = random.randint(1, 6)
    
    # Print the final outcome to the console immediately
    print(f"Rolled dice outcome: {final_value}")
    
    # Display the initial dice face
    for _ in range(10):  # Number of animation frames
        random_face = random.choice(dice_images)
        dice_label.config(image=random_face)
        dice_label.image = random_face
        app.update_idletasks()
        time.sleep(0.3)  # Pause to create animation effect

    # Display the final outcome on the GUI after the animation completes
    dice_label.config(image=dice_images[final_value - 1])
    dice_label.image = dice_images[final_value - 1]

# Create the main application window
app = tk.Tk()
app.title("Dice Simulator with Animation")

# Load the images for each dice face
dice_images = [
    ImageTk.PhotoImage(Image.open(f"dice_{i}.png").resize((100, 100)))
    for i in range(1, 7)
]

# Add a label to display instructions
instruction_label = tk.Label(app, text="Click anywhere to roll the dice!", font=("Helvetica", 14))
instruction_label.pack(pady=20)

# Add a label to display the dice image
dice_label = tk.Label(app)
dice_label.pack(pady=20)

# Set the initial image (first dice face)
dice_label.config(image=dice_images[0])
dice_label.image = dice_images[0]

# Bind mouse click to trigger the dice roll animation
app.bind("<Button-1>", lambda event: roll_dice_animation())

# Run the application
app.mainloop()
