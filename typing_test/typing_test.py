import curses
from curses import wrapper
import time
from words import words
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Press Enter to start the typing test")
    stdscr.refresh()
    stdscr.getkey()

def load_text():
    NUM_OF_WORDS = 14
    text = []
    for i in range(NUM_OF_WORDS):
        text.append(random.choice(words))
    text = " ".join(text)
    return text

def type_test(stdscr):
    text = load_text()
    key_pressed = []
    start_time = time.time()
    wpm = 0
    stdscr.nodelay(True)
    while True:
        #progress on screen
        elapsed_time = max(time.time() - start_time, 1)
        wpm = round( len(("".join(key_pressed)).split(" ")) / (elapsed_time / 60))
        
        stdscr.clear()
        stdscr.addstr(text, curses.color_pair(3))
        stdscr.addstr(2, 0, f"speed: {wpm} wpm", curses.color_pair(3))
        for i, char in enumerate(key_pressed):
            if char == text[i]:
                stdscr.addstr(0,i,char,curses.color_pair(1))
            else:
                stdscr.addstr(0,i,char,curses.color_pair(2))
        stdscr.refresh()
        
        if "".join(key_pressed) == text:
            stdscr.nodelay(False)
            break
            
        #checking key input
        try:
            key = stdscr.getkey()
        except:
            continue
        
        if ord(key) == 27:
            break
        if key == '\b':
            if len(key_pressed)>0:
                key_pressed.pop()
        elif len(key_pressed) < len(text):
            key_pressed.append(key)
              

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_screen(stdscr)
    while True:
        type_test(stdscr)
        stdscr.addstr(4, 0, "Press any key to continue...")
        key = stdscr.getkey()
        if ord(key) == 27:
            break

wrapper(main)