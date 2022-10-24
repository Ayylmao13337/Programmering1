from cgi import test
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Viewport Title", width=600, height=300)


with dpg.window(label="Window Name", width=550, height=250):
    dpg.add_input_text(label="text", default_value="Write sometihing")
    dpg.add_button(label="Click me", callback=test)
    dpg.add_text(test)
    dpg.add_input_text(label="Input text here",width=150)
    dpg.add_input_int(label="Inpunt int here", width=150)
    dpg.add_input_float(label="Float input", width=150)
    dpg.add_button(label="CLick meeee")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()