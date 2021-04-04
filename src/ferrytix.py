import SDL
import lvgl as lv
import file_drv as fs
import disp_drv as ds
SDL.init(w = 1280, h = 800)
lv.init()


# Register file-system driver.

fs_drv = lv.fs_drv_t()
fs.register(fs_drv, 'S')


# Load custom fonts
# TODO: fix ENOENT-Error

font_oxygen_bold_48 = lv.font_load("S:res/font-oxygen-bold-58.bin")
font_oxygen_bold_54 = lv.font_load("S:res/font-oxygen-bold-54.bin")
font_oxygen_regular_36 = lv.font_load("S:res/font-oxygen-regular-36.bin")
font_oxygen_regular_48 = lv.font_load("S:res/font-oxygen-regular-48.bin")


# Register SDL display driver.

ds.register()


# Regsiter SDL mouse driver

indev_drv = lv.indev_drv_t()
indev_drv.init()
indev_drv.type = lv.INDEV_TYPE.POINTER
indev_drv.read_cb = SDL.mouse_read
indev_drv.register()


# Create the welcome page

scr = lv.obj()
style_scr = lv.style_t()
style_scr.set_bg_color(lv.STATE.DEFAULT, lv.color_hex(0xffffff))
scr.add_style(lv.obj.PART.MAIN, style_scr)
head = lv.obj(scr)
head.set_size(1280, 200)
head.set_click(False)
style_head = lv.style_t()
style_head.set_bg_color(lv.STATE.DEFAULT, lv.color_hex(0xf3f3f3))
style_head.set_border_width(lv.STATE.DEFAULT, 0)
style_head.set_radius(lv.STATE.DEFAULT, 0)
head.add_style(lv.obj.PART.MAIN, style_head)
title = lv.label(head)
title.set_text("Ticketautomat Personenfähre Keer Tröch ||")
# style_title = lv.style_t()
# style_title.set_text_font(lv.STATE.DEFAULT, font_oxygen_bold_54)
# title.add_style(lv.label.PART.MAIN, style_title)
title.align(head, lv.ALIGN.CENTER, 0, -30)
sub_title = lv.label(head)
sub_title.set_text("Bislich   Xanten")
# style_sub_title = lv.style_t()
# style_sub_title.set_text_font(lv.STATE.DEFAULT, font_oxygen_regular_48)
# title.add_style(lv.label.PART.MAIN, style_title)
sub_title.align(head, lv.ALIGN.CENTER, 0, 30)
schedule = lv.obj(scr)
schedule.set_size(550, 400)
schedule.set_pos(50, 250)
schedule.set_click(False)
style_schedule = lv.style_t()
style_schedule.set_bg_color(lv.STATE.DEFAULT, lv.color_hex(0xe5e5e5))
style_schedule.set_border_color(lv.STATE.DEFAULT, lv.color_hex(0xe5e5e5))
style_schedule.set_border_width(lv.STATE.DEFAULT, 0)
style_schedule.set_radius(lv.STATE.DEFAULT, 15)
schedule.add_style(lv.obj.PART.MAIN, style_schedule)
schedule_title = lv.label(schedule)
schedule_title.set_text("Fährzeiten")
schedule_title.align(schedule, lv.ALIGN.IN_TOP_LEFT, 10, 1)
# style_schedule_title = lv.style_t()
# style_schedule_title.set_text_font(lv.STATE.DEFAULT, font_oxygen_regular_48)
# schedule_title.add_style(lv.label.PART.MAIN, style_schedule_title)
information = lv.obj(scr)
information.set_size(554, 400)
information.set_pos(680, 250)
information.set_click(False)
style_information = style_schedule
information.add_style(lv.obj.PART.MAIN, style_information)
information_title = lv.label(information)
information_title.set_text("Information")
#information_title.set_pos(114, 1)
#information_title.set_size(436, 77)
information_title.align(information, lv.ALIGN.IN_TOP_LEFT, 114, 1)
# style_information_title = lv.style_t()
# style_information_title.set_text_font(lv.STATE.DEFAULT, font_oxygen_regular_48)
# information_title.add_style(lv.label.PART.MAIN, style_information_title)
style_hidden = lv.style_t()
style_hidden.set_bg_opa(lv.STATE.DEFAULT, 0)
style_hidden.set_border_opa(lv.STATE.DEFAULT, 0)
style_hidden.set_border_width(lv.STATE.DEFAULT, 0)
information_time_label_container = lv.obj(information)
information_time_label_container.set_size(255, 77)
information_time_label_container.set_pos(0, 86)
information_time_label_container.set_click(False)
information_time_label_container.add_style(lv.obj.PART.MAIN, style_hidden)
information_time_label = lv.label(information_time_label_container)
information_time_label.set_text("Uhrzeit:")
information_time_label.align(information_time_label_container, lv.ALIGN.CENTER, 0, 0)
# style_information_time_label = lv.style_t()
# style_information_time_label.set_text_font(lv.STATE.DEFAULT, font_oxygen_regular_36)
# information_time_label.add_style(lv.label.PARTMAIN, style_information_time_label)
information_time_value_container = lv.obj(information)
information_time_value_container.set_size(300, 77)
information_time_value_container.set_pos(250, 86)
information_time_value_container.set_click(False)
information_time_value_container.add_style(lv.obj.PART.MAIN, style_hidden)
information_time_value = lv.label(information_time_value_container)
information_time_value.set_text("15:06 Uhr") # TODO: Set time dynamically
information_time_value.align(information_time_value_container, lv.ALIGN.CENTER, 0, 0)
# style_information_time_value = lv.style_t()
# style_information_time_value.set_text_font(lv.STATE.DEFAULT, font_oxygen_bold_48)
# information_time_value.add_style(lv.label.PARTMAIN, style_information_time_value)
information_last_ride_label_container = lv.obj(information)
information_last_ride_label_container.set_size(255, 77)
information_last_ride_label_container.set_pos(0, 165)
information_last_ride_label_container.set_click(False)
information_last_ride_label_container.add_style(lv.obj.PART.MAIN, style_hidden)
information_last_ride_label = lv.label(information_last_ride_label_container)
information_last_ride_label.set_text("Letzte Fahrt:")
information_last_ride_label.align(information_last_ride_label_container, lv.ALIGN.CENTER, 0, 0)
# style_information_last_ride_label = style_information_time_label
# style_information_last_ride_label.set_text_color(lv.STATE.DEFAULT, lv.color_hex(0x9b9b9b))
# information_last_ride_label.add_style(lv.label.PARTMAIN, style_information_time_label)
information_last_ride_value_container = lv.obj(information)
information_last_ride_value_container.set_size(300, 77)
information_last_ride_value_container.set_pos(250, 165)
information_last_ride_value_container.set_click(False)
information_last_ride_value_container.add_style(lv.obj.PART.MAIN, style_hidden)
information_last_ride_value = lv.label(information_last_ride_value_container)
information_last_ride_value.set_text("19:00 Uhr") # TODO: Set time dynamically
information_last_ride_value.align(information_last_ride_value_container, lv.ALIGN.CENTER, 0, 0)
# style_information_last_ride_value = style_information_time_value
# style_information_last_ride_value.set_text_color(lv.STATE.DEFAULT, lv.color_hex(0x9b9b9b))
# information_last_ride_value.add_style(lv.label.PARTMAIN, style_information_last_ride_value)
information_waiting_room_label_container = lv.obj(information)
information_waiting_room_label_container.set_size(550, 67)
information_waiting_room_label_container.set_pos(0, 242)
information_waiting_room_label_container.set_click(False)
information_waiting_room_label_container.add_style(lv.obj.PART.MAIN, style_hidden)
information_waiting_room_label = lv.label(information_waiting_room_label_container)
information_waiting_room_label.set_text("Aktuell im Wartebereich:")
information_waiting_room_label.align(information_waiting_room_label_container, lv.ALIGN.CENTER, 0, 0)
# style_information_waiting_room_label = lv_style_t()
# style_information_waiting_room_label.set_text_font(lv.STATE.DEFAULT, font_oxygen_regular_36)
# information_waiting_room_label.add_style(lv.label.PARTMAIN, style_information_waiting_room_label)
information_waiting_room_pedestrians_container = lv.obj(information)
information_waiting_room_pedestrians_container.set_size(152, 91)
information_waiting_room_pedestrians_container.set_pos(142, 309)
information_waiting_room_pedestrians_container.set_click(False)
information_waiting_room_pedestrians_container.add_style(lv.obj.PART.MAIN, style_hidden)
information_waiting_room_pedestrians = lv.label(information_waiting_room_pedestrians_container)
information_waiting_room_pedestrians.set_text("🧑🏼 17") # TODO: Set value dynamically
information_waiting_room_pedestrians.align(information_waiting_room_pedestrians_container, lv.ALIGN.CENTER, 0, 0)
# style_information_waiting_room_pedestrians = lv_style_t()
# style_information_waiting_room_pedestrians.set_text_font(lv.STATE.DEFAULT, font_oxygen_regular_36)
# information_waiting_room_pedestrians.add_style(lv.label.PARTMAIN, style_information_waiting_room_pedestrians)
information_waiting_room_bicycles_container = lv.obj(information)
information_waiting_room_bicycles_container.set_size(152, 91)
information_waiting_room_bicycles_container.set_pos(291, 309)
information_waiting_room_bicycles_container.set_click(False)
information_waiting_room_bicycles_container.add_style(lv.obj.PART.MAIN, style_hidden)
information_waiting_room_bicycles = lv.label(information_waiting_room_bicycles_container)
information_waiting_room_bicycles.set_text("🚲 11") # TODO: Set value dynamically
information_waiting_room_bicycles.align(information_waiting_room_bicycles_container, lv.ALIGN.CENTER, 0, 0)
# style_information_waiting_room_bicycles = style_information_waiting_room_pedestrians
# information_waiting_room_bicycles.add_style(lv.label.PARTMAIN, style_information_waiting_room_bicycles)
buy_ticket_button = lv.btn(scr);
buy_ticket_button.set_size(400, 90)
buy_ticket_button.set_pos(200, 680)
# TODO: add btn-click listener
style_buy_ticket = lv.style_t()
style_buy_ticket.set_bg_color(lv.STATE.DEFAULT, lv.color_hex(0x00954d))
style_buy_ticket.set_border_width(lv.STATE.DEFAULT, 0)
style_buy_ticket.set_radius(lv.STATE.DEFAULT, 25)
buy_ticket_button.add_style(lv.btn.PART.MAIN, style_buy_ticket)
buy_ticket_button_label = lv.label(buy_ticket_button)
buy_ticket_button_label.set_text("Ticket kaufen")
style_buy_ticket_button_label = lv.style_t()
style_buy_ticket_button_label.set_text_color(lv.STATE.DEFAULT, lv.color_hex(0xffffff))
# style_buy_ticket_button_label.set_text_font(lv.STATE.DEFAULT, font_oxygen_bold_48)
buy_ticket_button_label.add_style(lv.label.PART.MAIN, style_buy_ticket_button_label)
recharge_membership_card_button = lv.btn(scr);
recharge_membership_card_button.set_size(340, 70)
recharge_membership_card_button.set_pos(680, 690)
# TODO: add btn-click listener
style_recharge_membership_card = lv.style_t()
style_recharge_membership_card.set_bg_color(lv.STATE.DEFAULT, lv.color_hex(0x4c567c))
style_recharge_membership_card.set_border_width(lv.STATE.DEFAULT, 0)
style_recharge_membership_card.set_radius(lv.STATE.DEFAULT, 25)
recharge_membership_card_button.add_style(lv.btn.PART.MAIN, style_recharge_membership_card)
recharge_membership_card_button_label = lv.label(recharge_membership_card_button)
recharge_membership_card_button_label.set_text("FährCard aufladen")
style_recharge_membership_card_button_label = lv.style_t()
style_recharge_membership_card_button_label.set_text_color(lv.STATE.DEFAULT, lv.color_hex(0xffffff))
# style_recharge_membership_card_button_label.set_text_font(lv.STATE.DEFAULT, font_oxygen_bold_48)
recharge_membership_card_button_label.add_style(lv.label.PART.MAIN, style_recharge_membership_card_button_label)
information_button = lv.btn(scr);
information_button.set_size(50, 50)
information_button.set_pos(1030, 700)
# TODO: add btn-click listener
style_information = lv.style_t()
style_information.set_bg_color(lv.STATE.DEFAULT, lv.color_hex(0x4c567c))
style_information.set_border_width(lv.STATE.DEFAULT, 0)
style_information.set_radius(lv.STATE.DEFAULT, 25)
information_button.add_style(lv.btn.PART.MAIN, style_information)
information_button_label = lv.label(information_button)
information_button_label.set_text("i")
style_information_button_label = lv.style_t()
style_information_button_label.set_text_color(lv.STATE.DEFAULT, lv.color_hex(0xffffff))
# style_information_button_label.set_text_font(lv.STATE.DEFAULT, font_oxygen_bold_48)
information_button_label.add_style(lv.label.PART.MAIN, style_information_button_label)



# Load the screen

lv.scr_load(scr)


# Do something
while 1:
    pass