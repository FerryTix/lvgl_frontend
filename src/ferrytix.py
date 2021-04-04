import SDL
import lvgl as lv
import file_drv as fs
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

disp_buf1 = lv.disp_buf_t()
buf1_1 = bytearray(1280*10)
disp_buf1.init(buf1_1, None, len(buf1_1)//4)
disp_drv = lv.disp_drv_t()
disp_drv.init()
disp_drv.buffer = disp_buf1
disp_drv.flush_cb = SDL.monitor_flush
disp_drv.hor_res = 1280
disp_drv.ver_res = 800
disp_drv.rotated = 2 # should (in theory) rotate the display by 180°
disp_drv.register()


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
style_head = lv.style_t()
style_head.set_bg_color(lv.STATE.DEFAULT, lv.color_hex(0xf3f3f3))
style_head.set_border_width(lv.STATE.DEFAULT, 0)
head.add_style(lv.obj.PART.MAIN, style_head)
title = lv.label(head)
title.set_text("Ticketautomat Personenfähre Keer Tröch ||")
# style_title = lv.style_t()
# style_title.set_text_font(lv.STATE.DEFAULT, font_oxygen_bold_54)
# title.add_style(lv.label.PART.MAIN, style_title)
title.align(head, lv.ALIGN.CENTER, 0, -30)
sub_title = lv.label(head)
sub_title.set_text("Bislich --> Xanten")
# style_sub_title = lv.style_t()
# style_sub_title.set_text_font(lv.STATE.DEFAULT, font_oxygen_regular_48)
# title.add_style(lv.label.PART.MAIN, style_title)
sub_title.align(head, lv.ALIGN.CENTER, 0, 30)


# Load the screen

lv.scr_load(scr)


# Do something
while 1:
    pass