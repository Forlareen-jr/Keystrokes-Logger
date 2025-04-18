import keyboard

def on_key_press(event):
    """
    This function is called whenever a key is pressed.
    It prints the key that was pressed to the console.

    Args:
        event: A keyboard.KeyboardEvent object representing the key press.
    """
    # Use a try-except block to handle potential errors, such as special key combinations.
    try:
        print(f"Key pressed: {event.name}")  # Print the key name
    except AttributeError:
        # Handle cases where the event doesn't have a 'name' attribute.
        print(f"Key pressed: (Unknown)")

def main():
    """
    Main function to start the keylogger.
    It sets up the keyboard listener and keeps the program running.
    """
    print("Keylogger started. Press Esc to stop.")
    # `suppress=True` prevents the pressed keys from being printed to the console.
    keyboard.on_press(on_key_press, suppress=True)

    # Keep the program running until the user presses the escape key.
    keyboard.wait('esc')
    print("Keylogger stopped.")

if __name__ == "__main__":
    main()

