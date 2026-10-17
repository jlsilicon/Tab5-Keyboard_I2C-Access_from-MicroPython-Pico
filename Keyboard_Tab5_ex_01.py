##  Keyboard_Tab5_ex_01.py


from machine import I2C, Pin
from time    import sleep_ms

# Initialize I2C0 on standard Pico pins GP4 (SDA) and GP5 (SCL) - need Pullups 4.7k :
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=100000)

#

print("Scanning I2C bus...")
devices = i2c.scan()

if len(devices) == 0:
    print("No I2C devices found!")
else:
    print("Found", len(devices), "devices:")
    for device in devices:
        print("Decimal:", device, "Hex: 0x{:02x}".format(device))

#

print("")

# Tab5 Keyboard default I2C address is 0x6D
KEYBOARD_ADDR      = 0x6D

T5K_SYS_MODE       = 0x00 
T5K_CONFIG_MODE    = 0x10 
T5K_KEY_EVENT      = 0x20 
T5K_HID_EVENT      = 0x30 
T5K_CHAR_EVENT_LEN = 0x40 
T5K_CHAR_EVENT     = 0x50 

print("Starting Tab5 Keyboard reader...")


## i2c.writeto_mem(device_address, register_address, data)
## data_to_send = bytearray([0x2A, 0x4B]) 
# i2c.writeto_mem( KEYBOARD_ADDR , T5K_SYS_MODE    , (0) )
# i2c.writeto_mem( KEYBOARD_ADDR , T5K_SYS_MODE    , ('b\x00') )
i2c.writeto_mem( KEYBOARD_ADDR , T5K_SYS_MODE    , bytearray([ 0x00, 0x00 , 0x00 , 0x00 ]) )
# i2c.writeto_mem( KEYBOARD_ADDR , T5K_CONFIG_MODE , ('b\x00') )
i2c.writeto_mem( KEYBOARD_ADDR , T5K_CONFIG_MODE    , bytearray([ 0x00, 0x00 ]) )

Key_Tbl = [ 
  "ESC" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0" , "-" , "+" , "DEL" , "" , ""  ,  ## - [0] 
  "`~" , "!?" , "@" , "#" , "$" , "%" , "^" , "&" , "*" , "(<" , ">)" , "[{" , "]}" , "\\|" , "" , ""  ,  ## - [16] 
  "TAB" , "q" , "w" , "e" , "r" , "t" , "y" , "u" , "i" , "o" , "p" , ";:" , "'\"" , "BS" , "" , ""  ,  ## - [32] 
  "SYM" , "CAP" , "a" , "s" , "d" , "f" , "g" , "h" , "j" , "k" , "l" , "UP" , "_=" , "ENT" , "" , ""  ,  ## - [48] 
  "CTR" , "ALT" , "z" , "x" , "c" , "v" , "b" , "n" , "m" , ".'" , "LFT" , "DWN" , "RIT" , "_"  "" , ""  ,  ## - [64]
  "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , ""  , "" , ""  ,  ## - [80] 
  "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , ""  , "" , ""  ,  ## - [96] 
  "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , ""  , "" ,  ""  ,  ## - [112]
  "" , 
  "ESC" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0" , "-" , "+" , "DEL" , "" , ""  ,  ## - [128] 
  "`~" , "!?" , "@" , "#" , "$" , "%" , "^" , "&" , "*" , "(<" , ">)" , "[{" , "]}" , "\\|" , "" , ""  ,  ## - [144] 
  "TAB" , "q" , "w" , "e" , "r" , "t" , "y" , "u" , "i" , "o" , "p" , ";:" , "'\"" , "BS" , "" , ""  ,  ## - [160] 
  "SYM" , "CAP" , "a" , "s" , "d" , "f" , "g" , "h" , "j" , "k" , "l" , "UP" , "_=" , "ENT" , "" , ""  ,  ## - [176] 
  "CTR" , "ALT" , "z" , "x" , "c" , "v" , "b" , "n" , "m" , ".'" , "LFT" , "DWN" , "RIT" , "_"  "" , ""  ,  ## - [192]
] 
# print( Key_Tbl[1] )

while True:

  try:

    '''
    # Read 1 byte from the keyboard I2C address
    data = i2c.readfrom( KEYBOARD_ADDR , 1)
    if data and data[0] != 0:
      char_code = data[0] 
      # Print raw byte or character representation
      print(
          f"Pressed Code: {char_code} (Char: {chr(char_code) if 32 <= char_code < 127 else 'Special'})"
      )
    '''

    #

    ## data = i2c.readfrom_mem( DEVICE_ADDR , REG_ADDR , NUM_BYTES )
    key_evt       = i2c.readfrom_mem( KEYBOARD_ADDR , T5K_KEY_EVENT , 1 )
    if key_evt and key_evt[0] != 0 and key_evt[0] != 0xFF:
      char_code = key_evt[0]
      val_code  = int( key_evt[0] )
      key_code  = Key_Tbl[ val_code + 0 ]
#      print( f"Pressed Code: {key_evt} (Char: {chr(key_evt) if 32 <= char_code < 127 else 'Special'})" )
#      print( f"Pressed Code: {char_code} (Char: { Key_Tbl[ char_code + 1 ] })" )
      print( f"Pressed Code: {char_code} (Char: { key_code })" )

    #

    '''
    char_len      = i2c.readfrom_mem( KEYBOARD_ADDR , T5K_CHAR_EVENT_LEN , 1 )
    char_data     = i2c.readfrom_mem( KEYBOARD_ADDR , T5K_CHAR_EVENT , 1 )
#    print("i2c: m5k key_evt=" + str(key_evt[0]) + " , chr_len=" + str(char_len[0]) + " , chr_data=" + str(char_data[0]) )
    if char_len and char_data and char_data[0] != 0 :
      char_code = char_data[0]
      print(
          f"Pressed Code: {char_code} (Char: {chr(char_code) if 32 <= char_code < 127 else 'Special'})"
      )
    '''

  except OSError:
    # Device might not ack if busy or unpowered
    pass

  sleep_ms(100)  # Short delay to prevent flooding the I2C bus
#  sleep_ms(500)  # Short delay to prevent flooding the I2C bus
  

###

