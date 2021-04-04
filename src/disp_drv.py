import SDL
import lvgl as lv

def register():
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