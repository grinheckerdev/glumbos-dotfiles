import gi
import random
from datetime import datetime

gi.require_version("Gtk", "3.0")
gi.require_version("PangoCairo", "1.0")
from gi.repository import Gtk, Gdk, cairo, GLib, Pango, PangoCairo


class GlumbocoinStockWidget(Gtk.Window):
    def __init__(self):
        super().__init__(title="Glumbocoin Stock Price")
        self.set_decorated(False)  # Disable window decorations
        self.set_app_paintable(True)
        self.set_resizable(False)  # Fixed size window

        # Get screen size
        screen = Gdk.Screen.get_default()
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        # Set window size
        self.set_default_size(450, 350)
        self.move_to_top_right()

        # Apply dark theme
        self.set_dark_theme()

        # Initialize data
        self.prices = [random.uniform(30, 70) for _ in range(10)]
        self.timestamps = [datetime.now().strftime("%H:%M") for _ in range(10)]
        self.x_positions = [50 + i * 40*0.8 for i in range(len(self.prices))]  # Initial x positions
        print(self.x_positions)

        # Create a vertical layout
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        # Add a label for the title
        title_label = Gtk.Label(label="Glumbocoin Stock Price")
        title_label.set_name("title_label")
        title_label.set_halign(Gtk.Align.CENTER)
        vbox.pack_start(title_label, False, False, 0)

        # Create a DrawingArea for the graph
        self.drawing_area = Gtk.DrawingArea()
        self.drawing_area.set_size_request(450, 300)
        self.drawing_area.connect("draw", self.on_draw)
        vbox.pack_start(self.drawing_area, True, True, 0)

        # Apply styles
        self.set_style()

        # Update the stock price every 10 seconds
        GLib.timeout_add_seconds(10, self.update_prices)

        # Animate the graph horizontally every frame
        self.animation_in_progress = False
        self.shift_speed = 5  # Speed of horizontal shift in pixels per frame
        GLib.timeout_add(16, self.animate_prices)

    def set_dark_theme(self):
        """Set the window's background to dark."""
        self.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse("#1B1A25"))

    def set_style(self):
        """Set the theme styles for the widget."""
        css_provider = Gtk.CssProvider()
        css = b"""
        * {
            background-color: #1B1A25;
            color: white;
        }
        #title_label {
            font-size: 20px;
            font-weight: bold;
            color: white;
        }
        """
        css_provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
        )

    def move_to_top_right(self):
        """Move the window to the top-right corner."""
        screen = Gdk.Screen.get_default()
        monitor = screen.get_monitor_geometry(screen.get_primary_monitor())
        self.move(monitor.width - 560, 10)  # Adjust for padding and window size

    def update_prices(self):
        """Update stock prices with new random data."""
        if not self.animation_in_progress:
            # Remove the oldest price and x position
            self.prices.pop(0)
            self.x_positions.pop(0)

            # Add a new price and x position at the end
            last_x = self.x_positions[-1] if self.x_positions else 52
            self.prices.append(self.prices[-1] + random.uniform(-5, 5))
            self.x_positions.append(last_x + 32)  # Add new x position

            # Start animation
            self.animation_in_progress = True

        return True  # Keep the timeout running

    def animate_prices(self):
        """Animate the graph by shifting points horizontally."""
        if self.animation_in_progress:
            # Shift all x positions to the left
            for i in range(len(self.x_positions)):
                self.x_positions[i] -= self.shift_speed

            # Check if the oldest x position is off-screen
            if self.x_positions[0] <= 52:
                self.animation_in_progress = False  # Animation complete

            # Redraw the graph with the current positions
            self.drawing_area.queue_draw()
        return True  # Keep the animation running

    def on_draw(self, widget, cr):
        """Draw the stock price graph."""
        width = widget.get_allocated_width()
        height = widget.get_allocated_height()

        # Padding for the graph
        padding_left = 50
        padding_right = 100
        padding_bottom = 40
        padding_top = 20

        # Draw background
        cr.set_source_rgb(0.105, 0.101, 0.144)  # Dark background
        cr.rectangle(0, 0, width, height)
        cr.fill()

        # Draw axes
        cr.set_source_rgb(1, 1, 1)  # White lines
        cr.set_line_width(2)

        # X-axis
        cr.move_to(padding_left, height - padding_bottom)
        cr.line_to(width - padding_right, height - padding_bottom)

        # Y-axis
        cr.move_to(padding_left, height - padding_bottom)
        cr.line_to(padding_left, padding_top)
        cr.stroke()

        # Add y-axis price labels and horizontal grid lines
        self.draw_y_axis_labels_and_grid(
            cr, width, height, padding_left, padding_right, padding_bottom, padding_top
        )

        # Calculate scaling
        max_price = max(self.prices) + 5  # Add padding to max price
        min_price = min(self.prices) - 5  # Add padding to min price
        price_range = max_price - min_price or 1  # Avoid division by zero
        y_scale = (height - padding_top - padding_bottom) / price_range

        # Draw the graph line
        cr.set_source_rgb(1, 1, 1)  # White line
        cr.set_line_width(2)
        for i, price in enumerate(self.prices):
            x = self.x_positions[i]
            y = height - padding_bottom - (price - min_price) * y_scale
            if i == 0:
                cr.move_to(x, y)
            else:
                cr.line_to(x, y)
        cr.stroke()

        # Draw price points
        cr.set_source_rgb(1, 1, 1)  # White points
        for i, price in enumerate(self.prices):
            x = self.x_positions[i]
            y = height - padding_bottom - (price - min_price) * y_scale
            cr.arc(x, y, 3, 0, 2 * 3.14159)  # Smaller circle
            cr.fill()


    def draw_y_axis_labels_and_grid(self, cr, width, height, padding_left, padding_right, padding_bottom, padding_top):
        """Draw labels for the y-axis and horizontal grid lines."""
        max_price = max(self.prices) + 5
        min_price = min(self.prices) - 5
        price_range = max_price - min_price
        y_scale = (height - padding_top - padding_bottom) / price_range

        cr.set_line_width(1)  # Thinner line for grid lines
        cr.set_source_rgb(0.5, 0.5, 0.5)  # Gray color for grid lines

        # Draw evenly spaced labels and grid lines
        for i in range(6):  # 6 labels
            price = min_price + i * (price_range / 5)
            y = height - padding_bottom - i * (y_scale * (price_range / 5))

            # Draw horizontal grid line
            cr.move_to(padding_left, y)
            cr.line_to(width - padding_right, y)
            cr.stroke()

            # Draw the label to the right of the graph
            self.draw_text(cr, width - padding_right + 15, y-12, f"{price:.2f}", center=False)

    def draw_text(self, cr, x, y, text, center=False, rotate=False):
        """Draw text using Pango."""
        layout = PangoCairo.create_layout(cr)
        layout.set_text(text, -1)

        # Set font
        desc = Pango.FontDescription("Sans 12")
        layout.set_font_description(desc)

        # Get text dimensions
        width, height = layout.get_size()
        width /= Pango.SCALE
        height /= Pango.SCALE

        # Adjust position for centering
        if center:
            x -= width / 2
            y -= height / 2

        # Apply rotation if specified
        cr.save()
        if rotate:
            cr.translate(x, y)
            cr.rotate(-3.14159 / 2)
            cr.translate(-x, -y)

        # Move to the position and show the text
        cr.move_to(x, y)
        PangoCairo.show_layout(cr, layout)
        cr.restore()


# Run the widget
win = GlumbocoinStockWidget()
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()
