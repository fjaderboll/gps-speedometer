import time
from epd2in9 import EPD_2in9_Portrait
from large_font import draw_large_text

use_knots = True  # True for knots, False for km/h


if __name__=='__main__':
    start_time = time.ticks_ms()

    epd = EPD_2in9_Portrait()
    epd.Clear(epd.black)

    x_title = 0
    y_title = 0
    y_space = 60
    x_unit = 97
    y_unit = 36
    x_value = 2
    y_value = 15
    
    epd.fill(epd.white)
    epd.text("Speed", x_title, y_title + 0*y_space, epd.black)
    draw_large_text(epd, " 5.8", x_value, y_value, scale=4)
    epd.text("kt" if use_knots else "km/h", x_unit, y_unit + 0*y_space, epd.black)

    epd.text("Peak speed", x_title, y_title + 1*y_space, epd.black)
    draw_large_text(epd, "12.3", x_value, y_value + y_space, scale=4)
    epd.text("kt" if use_knots else "km/h", x_unit, y_unit + 1*y_space, epd.black)

    epd.text("Distance", x_title, y_title + 2*y_space, epd.black)
    draw_large_text(epd, " 9.6", x_value, y_value + 2*y_space, scale=4)
    epd.text("nm" if use_knots else "km", x_unit, y_unit + 2*y_space, epd.black)

    epd.text("Time", x_title, y_title + 3*y_space, epd.black)
    draw_large_text(epd, '--:--', x_value, y_value + 3*y_space, scale=4)

    epd.text("Clock", x_title, y_title + 4*y_space, epd.black)
    draw_large_text(epd, '12:34', x_value, y_value + 4*y_space, scale=4)
    epd.display(epd.buffer)

    for i in range(0, 5):
        uptime_s = int(time.ticks_diff(time.ticks_ms(), start_time) / 1000)
        time_str = '00:' + str(uptime_s // 10) + str(uptime_s % 10)

        draw_large_text(epd, time_str, x_value, y_value + 3*y_space, scale=4)
        epd.display_Partial(epd.buffer)

        epd.delay_ms(1000)
    
    draw_large_text(epd, '--:--', x_value, y_value + 3*y_space, scale=4)
    epd.display_Partial(epd.buffer)    
    
    print("sleep")
    epd.sleep()
