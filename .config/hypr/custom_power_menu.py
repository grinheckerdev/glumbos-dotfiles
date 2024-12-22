import gi
import subprocess

gi.require_version("Gtk", "3.0")
gi.require_version("GLib", "2.0")
from gi.repository import Gtk, Gdk, GLib


class PowerMenu(Gtk.Window):
    def __init__(self):
        super().__init__(title="Power Menu")
        self.set_decorated(False)  # Disable window decorations
        self.set_app_paintable(True)
        self.set_resizable(True)  # Allow resizing for dynamic updates

        # Get screen size
        screen = Gdk.Screen.get_default()
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        # Set window size (initial fullscreen)
        self.set_default_size(self.screen_width, self.screen_height)
        self.set_position(Gtk.WindowPosition.CENTER)

        # Transparent window background
        visual = screen.get_rgba_visual()
        self.set_visual(visual)
        rgba = Gdk.RGBA()
        rgba.parse("rgba(0, 0, 0, 0.0)")  # Fully transparent
        self.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        # Close the menu when clicking outside the buttons
        self.connect("button-press-event", self.on_global_click)

        # Close the menu on Escape key
        self.connect("key-press-event", self.on_key_press)

        # Create a fixed layout for positioning
        self.fixed = Gtk.Fixed()
        self.add(self.fixed)

        # Icon details (icon character, action, color)
        self.icons = [
            ("", self.lock, "#6817fd"),  # Lock - Purple
            ("", self.logout, "#edfd10"),  # Logout - Yellow
            ("", self.reboot, "#18fcdf"),  # Reboot - Cyan
            ("", self.shutdown, "#fe0eea"),  # Shutdown - Pink
        ]

        # Button size
        self.button_size = 55

        # Horizontal spacing between buttons
        self.spacing = 200

        # Create icon buttons
        self.buttons = []
        for icon, action, color in self.icons:
            # Create a button
            button = Gtk.Button()
            button.set_size_request(self.button_size, self.button_size)
            button.connect("clicked", action)

            # Style the button
            button_css = Gtk.CssProvider()
            button_css.load_from_data(f"""
            button {{
                background-color: transparent;
                border-radius: 50%;
                border: none;
                opacity: 0;  /* Fully transparent but clickable */
            }}
            """.encode())
            button_context = button.get_style_context()
            button_context.add_provider(button_css, Gtk.STYLE_PROVIDER_PRIORITY_USER)

            # Create a label for the icon
            label = Gtk.Label(label=icon)
            label.set_halign(Gtk.Align.CENTER)
            label.set_valign(Gtk.Align.CENTER)

            # Style the label
            label_css = Gtk.CssProvider()
            label_css.load_from_data(f"""
            label {{
                background-color: transparent;
                color: {color};        /* Icon color */
                font-size: 55px;       /* Icon size */
            }}
            """.encode())
            label_context = label.get_style_context()
            label_context.add_provider(label_css, Gtk.STYLE_PROVIDER_PRIORITY_USER)

            # Overlay the button on the label
            overlay = Gtk.Overlay()
            overlay.add(label)  # Add the label first
            overlay.add_overlay(button)  # Add the button on top

            # Store the button and add it to the fixed layout
            self.buttons.append((overlay, 0, 0))  # Track button and position
            self.fixed.put(overlay, 0, 0)  # Temporary position

        # Connect window size allocation signal to dynamically reposition buttons
        self.connect("size-allocate", self.on_resize)

    def on_resize(self, widget, allocation):
        """Dynamically center the buttons when the window size changes."""
        window_width = allocation.width
        window_height = allocation.height

        # Calculate the total width required for all buttons and spacings
        total_width = len(self.buttons) * self.button_size + (len(self.buttons) - 1) * self.spacing

        # Calculate starting X position to center horizontally
        start_x = (window_width - total_width) / 2

        # Calculate vertical center
        center_y = (window_height - self.button_size) / 2

        # Update button positions
        for i, (button, _, _) in enumerate(self.buttons):
            x_position = int(start_x + i * (self.button_size + self.spacing))
            y_position = int(center_y)
            self.fixed.move(button, x_position, y_position)

            # Update stored button positions
            self.buttons[i] = (button, x_position, y_position)

    def is_click_outside(self, event_x, event_y):
        """Check if the click is outside the bounds of all buttons."""
        for _, x, y in self.buttons:
            if (
                x <= event_x <= x + self.button_size
                and y <= event_y <= y + self.button_size
            ):
                return False  # Click is inside a button
        return True  # Click is outside all buttons

    # Event to handle global clicks
    def on_global_click(self, widget, event):
        if event.type == Gdk.EventType.BUTTON_PRESS:
            # Check if the click is outside the buttons
            if self.is_click_outside(event.x, event.y):
                Gtk.main_quit()

    # Button actions
    def lock(self, widget):
        print("Locking...")
        subprocess.Popen(["hyprlock"])  # Use Popen to avoid blocking
        Gtk.main_quit()

    def logout(self, widget):
        print("Logging out...")
        subprocess.Popen(["hyprctl", "dispatch", "exit"])
        Gtk.main_quit()

    def reboot(self, widget):
        print("Rebooting...")
        subprocess.Popen(["systemctl", "reboot"])
        Gtk.main_quit()

    def shutdown(self, widget):
        print("Shutting down...")
        subprocess.Popen(["systemctl", "poweroff"])
        Gtk.main_quit()

    # Event to close the menu on Escape key
    def on_key_press(self, widget, event):
        if event.keyval == Gdk.KEY_Escape:
            Gtk.main_quit()


# Run the application
win = PowerMenu()
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()
