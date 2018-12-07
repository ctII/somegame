import curses
from curses import wrapper
from threading import Thread
import time
from time import sleep
import queue
import uuid
from entity import entity

from entityTest import entityTest


def initCurses():
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)
    #screen.nodelay(1)
    return screen


def terminateCurses(screen):
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.endwin()


class Display(Thread):
    def __init__(self, entityQueue, screen):
        Thread.__init__(self)
        self.entityQueue = entityQueue
        self.screen = screen

    def run(self):
        entities = list()
        while True:
            try:
                entityUpdate = self.entityQueue.get(True, 0.01)
                if entityUpdate == ord('q'):
                    break
                inList = False
                for i in range(len(entities)):
                    if entities[i].getUUID() == entityUpdate.getUUID():
                        inList = True
                        entities[i] = entityUpdate
                        break
                if not inList:
                    entities.append(entityUpdate)
            except BaseException:
                pass
            self.screen.clear()
            for i in range(0, curses.COLS - 1):
                self.screen.addstr(0, i, '#')
                self.screen.addstr(curses.LINES - 1, i, '#')
            for i in range(0, curses.LINES - 1):
                self.screen.addstr(i, 0, '#')
                self.screen.addstr(i, curses.COLS - 1, '#')
            for e in entities:
                self.screen.addstr(e.getY(), e.getX(), e.getForm())
            self.screen.move(curses.LINES - 1, curses.COLS - 1)
            self.screen.refresh()


class Game(Thread):
    def __init__(self, inputQueue, entityQueue, screen):
        Thread.__init__(self)
        self.entityQueue = entityQueue
        self.inputQueue = inputQueue
        self.screen = screen
        self.entities = list()

    def run(self):
        self.mainChar = entity(1, 1, 'X')
        self.entityQueue.put(self.mainChar)
        self.entities.append(self.mainChar)

        self.entityTest = entityTest(1, 1)
        self.entityQueue.put(self.entityTest)
        self.entities.append(self.entityTest)

        while True:
            try:
                input = self.inputQueue.get(True, 0.001)
                if input == ord('q'):
                    break
                elif input == ord('w'):
                    self.mainChar.setY(self.mainChar.getY() - 1)
                    self.entityQueue.put(self.mainChar)
                elif input == ord('s'):
                    self.mainChar.setY(self.mainChar.getY() + 1)
                    self.entityQueue.put(self.mainChar)
                elif input == ord('d'):
                    self.mainChar.setX(self.mainChar.getX() + 1)
                    self.entityQueue.put(self.mainChar)
                elif input == ord('a'):
                    self.mainChar.setX(self.mainChar.getX() - 1)
                    self.entityQueue.put(self.mainChar)
                with self.inputQueue.mutex:
                    self.inputQueue.clear()
            except BaseException:
                pass
            oldTime = time.time()
            self.tick()
            sleep(time.time() - oldTime - 0.05 * -1)

    def tick(self):
        for e in self.entities:
            e.tick()

def main():
    screen = initCurses()
    inputQueue = queue.Queue(1000)
    entityQueue = queue.Queue(1000)

    game = Game(inputQueue, entityQueue, screen)
    game.start()

    display = Display(entityQueue, screen)
    display.start()

    while True:
        input = screen.getch()
        if input is not -1:
            print(input)
            inputQueue.put(input)
            if(input == ord('q')):
                entityQueue.put(input)
                break

    game.join()
    display.join()

    terminateCurses(screen)


if __name__ == "__main__":
    try:
        main()
    finally:
        curses.nocbreak()
        curses.echo()
        curses.endwin()
