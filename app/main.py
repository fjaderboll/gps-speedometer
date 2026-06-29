import time
from epd2in9 import EPD_2in9_Portrait

use_knots = False

font = {
    '0': ("01110", "10001", "10011", "10101", "11001", "10001", "01110"),
    '1': ("00100", "01100", "00100", "00100", "00100", "00100", "01110"),
    '2': ("01110", "10001", "00001", "00110", "01000", "10000", "11111"),
    '3': ("01110", "10001", "00001", "00110", "00001", "10001", "01110"),
    '4': ("00010", "00110", "01010", "10010", "11111", "00010", "00010"),
    '5': ("11111", "10000", "11110", "00001", "00001", "10001", "01110"),
    '6': ("00110", "01000", "10000", "11110", "10001", "10001", "01110"),
    '7': ("11111", "00001", "00010", "00100", "01000", "01000", "01000"),
    '8': ("01110", "10001", "10001", "01110", "10001", "10001", "01110"),
    '9': ("01110", "10001", "10001", "01111", "00001", "00010", "01100"),
    ':': ("00000", "00100", "00000", "00000", "00100", "00000", "00000"),
    '-': ("00000", "00000", "00000", "11111", "00000", "00000", "00000"),
    '.': ("00000", "00000", "00000", "00000", "00000", "00100", "00100"),
    ' ': ("00000", "00000", "00000", "00000", "00000", "00000", "00000"),
}

def draw_large_text(epd, text, x, y, scale=2):
    font_color = epd.black
    background_color = epd.white

    # clear background
    epd.fill_rect(x, y, len(str(text)) * (6 * scale), 7 * scale, background_color)

    # draw text
    for index, char in enumerate(str(text)):
        glyph = font.get(char)
        if glyph is None:
            continue

        for row, line in enumerate(glyph):
            for col, pixel in enumerate(line):
                if pixel == '1':
                    epd.fill_rect(
                        x + index * (6 * scale) + col * scale,
                        y + row * scale,
                        scale,
                        scale,
                        font_color,
                    )


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
    draw_large_text(epd, '--:--', x_value, y_value + 4*y_space, scale=4)
    epd.display(epd.buffer)

    for i in range(0, 5):
        uptime_s = int(time.ticks_diff(time.ticks_ms(), start_time) / 1000)
        time_str = '00:' + str(uptime_s // 10) + str(uptime_s % 10)

        draw_large_text(epd, time_str, x_value, y_value + 3*y_space, scale=4)
        epd.display_Partial(epd.buffer)

        epd.delay_ms(1000)
    
    #epd.vline(10, 90, 60, 0x00)
    #epd.vline(120, 90, 60, 0x00)
    #epd.hline(10, 90, 110, 0x00)
    #epd.hline(10, 150, 110, 0x00)
    #epd.line(10, 90, 120, 150, 0x00)
    #epd.line(120, 90, 10, 150, 0x00)
    #epd.display(epd.buffer)
    #epd.delay_ms(2000)
    
    #epd.rect(10, 180, 50, 80, 0x00)
    #epd.fill_rect(70, 180, 50, 80, 0x00)
    #epd.display_Base(epd.buffer)
    #epd.delay_ms(2000)
    
    #for i in range(0, 10):
    #    epd.fill_rect(40, 270, 40, 10, 0xff)
    #    epd.text(str(i), 60, 270, 0x00)
    #    epd.display_Partial(epd.buffer)

    #epd.init_4Gray()
    #epd.image4Gray.fill_rect(0, 0, 127, 74, epd.black)  
    #epd.image4Gray.text('GRAY1',10, 33, epd.white)
    #epd.image4Gray.fill_rect(0, 74, 127, 74, epd.darkgray)
    #epd.image4Gray.text('GRAY2',10, 107, epd.grayish)
    #epd.image4Gray.fill_rect(0, 148, 127, 74, epd.grayish)
    #epd.image4Gray.text('GRAY3',10, 181, epd.darkgray)
    #epd.image4Gray.fill_rect(0, 222, 127, 74, epd.white)
    #epd.image4Gray.text('GRAY4',10, 255, epd.black)
    #epd.display_4Gray(epd.buffer_4Gray)
    #epd.delay_ms(5000)

    #epd.init()
    #epd.Clear(0xff)
    #epd.delay_ms(2000)
    print("sleep")
    epd.sleep()