from cgitb import text
from unicodedata import name
import dearpygui.dearpygui as dpg


dpg.create_context()
dpg.create_viewport(title="Viewport Title", width=600, height=300)


with dpg.window(no_title_bar=True, width=550, height=250):
    dpg.add_input_float(label="Your weight on earth")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()