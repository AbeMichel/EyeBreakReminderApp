import tkinter as tk
from tkinter import Toplevel


class BreakApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Break Reminder")
        self.root.geometry("400x200")

        self.timer_title_text = tk.StringVar(value="Time before next break")
        self.timer_time_text = tk.StringVar(value="00:00")

        self.timer_title_label = tk.Label(self.root, textvariable=self.timer_title_text)
        self.timer_title_label.pack(pady=10)
        self.timer_time_label = tk.Label(self.root, textvariable=self.timer_time_text)
        self.timer_time_label.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start", command=self.start)
        self.start_button.pack(pady=10)
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack(pady=10)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_window_close)

        self.running = False
        self.current_after = None
        self.popup = None
        self.time_left_main_timer_sec = 0

        self.time_between_breaks_min = 20
        self.duration_of_breaks_sec = 20

    def start(self):
        """Starts the reminder cycle."""
        self.running = True
        self.start_break_reminders()  # Start the break reminder cycle

    def stop(self):
        """Stops the reminder cycle."""
        if self.current_after:
            self.root.after_cancel(self.current_after)
        if self.popup:
            self.popup.destroy()
        self.running = False
        self.current_after = None
        self.popup = None

    def on_window_close(self):
        self.stop()
        self.root.destroy()

    def start_break_reminders(self):
        """Start the break reminder cycle with a set interval."""
        if self.running:
            # Schedule the next reminder
            if self.current_after:
                self.root.after_cancel(self.current_after)
            self.current_after = self.root.after(int(self.time_between_breaks_min * 60 * 1000), self.blank_screen, self.duration_of_breaks_sec)

            # Update the main window timer (countdown before next break)
            self.start_main_timer()

    def start_main_timer(self):
        """Updates the main window timer in real-time."""
        self.time_left_main_timer_sec = self.time_between_breaks_min * 60
        def update_timer():
            """Decrements time and updates the timer in real-time."""
            if self.time_left_main_timer_sec > 0 and self.running:
                self.time_left_main_timer_sec -= 1
                minutes = int(self.time_left_main_timer_sec // 60)
                seconds = int(self.time_left_main_timer_sec % 60)
                self.timer_time_text.set(f"{minutes:02}:{seconds:02}")
                # Update every second
                self.root.after(1000, update_timer)

        update_timer()

    def blank_screen(self, duration_sec):
        """Displays a full-screen popup and runs a timer."""
        if self.popup and self.popup.winfo_exists():
            return

        self.popup = Toplevel(self.root)
        self.popup.attributes("-fullscreen", True)
        self.popup.attributes("-topmost", True)
        self.popup.configure(bg="black")
        self.popup.bind("<Escape>", lambda e: self.popup.withdraw())
        self.popup.focus_force()

        # Create label
        instruction_label = tk.Label(self.popup, text="Look away", font=("Arial", 80), fg="white", bg="black")
        instruction_label.place(relx=0.5, rely=0.2, anchor="center")
        # Create timer
        timer_label = tk.Label(self.popup, text="", font=("Arial", 80), fg="white", bg="black")
        timer_label.place(relx=0.5, rely=0.5, anchor="center")

        def run_timer(remaining_time: int):
            """Handles the countdown timer for the popup."""
            if remaining_time >= 0:
                # Format time to mm:ss
                minutes = remaining_time // 60
                seconds = remaining_time % 60
                timer_label.config(text=f"{minutes:02}:{seconds:02}")
                self.popup.after(1000, run_timer, remaining_time - 1)
            else:
                self.popup.destroy()  # Close popup when time is up
                self.popup = None
                if self.running:
                    self.start_break_reminders()  # Start the next reminder

        run_timer(duration_sec)

    def run(self):
        self.root.mainloop()


def main():
    """Main function to run the Tkinter app."""
    app = BreakApp()
    app.run()

if __name__ == "__main__":
    main()
