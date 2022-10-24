import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Viewport Title", width=600, height=300)
with dpg.window(label="Window Name", width=550, height=250):
    dpg.add_text("Somthing")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()