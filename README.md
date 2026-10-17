# Tab5-Keyboard_I2C-Access_from-MicroPython-Pico

How to use the Tab5-Keyboard using I2C in MicroPython on Pico PICO-2 / Esp32 / CYD / Arduino / etc.

<img width="447" height="447" alt="Tab5_Keyboard" src="https://github.com/user-attachments/assets/5a0cdcae-1f7f-4f51-a3b4-a1dd90618f3c" />
https://shop.m5stack.com/cdn/shop/files/Keyboard_for_Tab5_4_1200x1200.webp?v=1786608177


I had purchased one of the Tab5 Keyboards for use on the Rasp PICO.
But, I could not find any software to access it.
Nor, did the manufacturer bother providing software / protocols to do this.

I did go skimming thru the provided code, and found that it was using a simple based I2C protocol.
So, I slapped this code together for I2C in Micropython.

And, voila ! - it worked.

For anybody who wants to use the Tab5 Keyboard on the Pico, etc - here it is !
