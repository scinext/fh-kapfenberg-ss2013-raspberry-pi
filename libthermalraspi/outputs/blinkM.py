import struct

from i2c_device import I2CDevice

class BlinkM(I2CDevice):
    GO_TO_RGB = '\x6e'
    FADE_TO_RGB = '\x63'
    FADE_TO_HSB = '\x68'
    FADE_TO_RANDOM_RGB = '\x43'
    FADE_TO_RANDOM_HSB = '\x48'
    PLAY_LIGHT_SCRIPT = '\x70'
    STOP_SCRIPT = '\x6f'
    SET_FADE_SPEED = '\x66'
    SET_TIME_ADJUST = '\x74'
    GET_CURRENT_RGB = '\x67'
    WRITE_SCRIPT_LINE = '\x57'
    READ_SCRIPT_LINE = '\x52'
    SET_SCRIPT_LENGTH_AND_REPEATS = '\x4c'
    SET_BLINKM_ADDRESS = '\x41'
    GET_BLINKM_ADDRESS = '\x61'
    GET_BLINKM_FIRMWARE_VERSION = '\x5a'
    SET_STARTUP_PARAMETERS = '\x42'  
    
    def __init__(self, bus, addr):
        I2CDevice.__init__(self, bus, addr)
    
    def go_to_rgb(self, rgb):
        self.write(self.GO_TO_RGB)
        for color in rgb:
            self.write(struct.pack('B', color))
    
    def fade_to_rgb(self, rgb):
        self.write(self.FADE_TO_RGB)
        for color in rgb:
            self.write(struct.pack('B', color))
    
    def fade_to_hsb(self, hsb):
        self.write(self.FADE_TO_HSB)
        for color in rgb:
            self.write(struct.pack('B', color))
    
    def fade_to_random_rgb(self, rgb):
        self.write(self.FADE_TO_RANDOM_RGB)
        for color in rgb:
            self.write(struct.pack('B', color))
            
    def fade_to_random_hsb(self, rgb):
        self.write(self.FADE_TO_RANDOM_HSB)
        for color in rgb:
            self.write(struct.pack('B', color))
            
    def play_light_script(self, script_number):
        self.write(self.PLAY_LIGTH_SCRIPT)
        self.write(struct.pack('B', script_number))
        
    def stop_script(self):
        self.write(self.STOP_SCRIPT)
    
    def set_fade_speed(self, speed):
        self.write(self.SET_FADE_SPEED)
        self.write(struct.pack('B', speed))

    def set_time_adjust(self, time_adjust):
        self.write(self.SET_TIME_ADJUST)
        self.write(struct.pack('B', time_adjust))
        
    def get_current_rgb(self):
        self.write(self.GET_CURRENT_RGB)
        return self.__readInt(3)
    
    def set_blinkm_address(self, address):
        self.write(self.SET_BLINKM_ADDRESS)
        self.write(struct.pack('B'), address)
        self.write('\xd0')
        self.write('\x0d')
        self.write(struct.pack('B'), address)
        
    def get_blinkm_address(self):
        self.write(self.GET_BLINKM_ADDRESS)
        return self.__readInt(1)
    
    def get_blinkm_firmware_version(self):
        self.write(self.GET_BLINKM_FIRMWARE_VERSION)
        return self.__readInt(2) 
    
    def set_startup_parameters(self, startup_mode, script_number, repeats, fade_speed, time_adjust):
        self.write(self.SET_STARTUP_PARAMETERS)
        self.write(struct.pack('B', startup_mode))
        self.write(struct.pack('B', script_number))
        self.write(struct.pack('B', repeats))
        self.write(struct.pack('B', fade_speed))
        self.write(struct.pack('B', time_adjust))
    
    def __readInt(self, count):
        return struct.unpack('B' * count, self.read(count))[:count]

class LightScript(object):
    STARTUP = 0
    RGB = 1
    WHITE_FLASH = 2
    RED_FLASH = 3
    GREEN_FLASH = 4
    BLUE_FLASH = 5
    CYAN_FLASH = 6
    MAGENTA_FLASH = 7
    YELLOW_FLASH = 8
    BLACK = 9
    HUE_CYCLE = 10
    MOOD_LIGHT = 11
    VIRTUAL_CANDLE = 12
    WATER_REFLECTIONS = 13
    OLD_NEON = 14
    THE_SEASONS = 15
    THUNDERSTORM = 16
    STOP_LIGHT = 17
    MORSE_CODE = 18
