import time
from epd2in9 import EPD_2in9_Portrait

if __name__=='__main__':
    start_time = time.ticks_ms()

    epd = EPD_2in9_Portrait()
    epd.Clear(epd.black)
    
    epd.fill(epd.white)
    epd.text("Speed", 0, 0, epd.black)
    epd.text("Peak speed", 0, 80, epd.black)
    epd.text("Distance", 0, 160, epd.black)
    epd.text("Time", 0, 240, epd.black)
    epd.display(epd.buffer)

    for i in range(0, 10):
        uptime_s = int(time.ticks_diff(time.ticks_ms(), start_time) / 1000)

        epd.fill_rect(40, 270, 40, 10, epd.black)
        epd.text(str(uptime_s), 60, 270, epd.white)
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