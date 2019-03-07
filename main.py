import curses
from curses import wrapper
from threading import Thread
import time
from time import sleep
import queue
import uuid
import copy

from world import world
from entity import entity
from entityTest import entityTest


def initCurses():
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)
    screen.nodelay(1)
    return screen


def terminateCurses(screen):
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.endwin()


class Game(Thread):
    def __init__(self, inputQueue, entityQueue, screen):
        Thread.__init__(self)
        self.entityQueue = entityQueue
        self.inputQueue = inputQueue
        self.screen = screen
        self.world = world(curses.LINES - 1, curses.COLS - 1)

    def run(self):
        self.mainChar = entity(self.world, 1, 1, 'X')
        self.world.addEntity(self.mainChar)
        self.world.addEntity(entityTest(self.world, 1, 1))

        self.entityQueue.put(copy.copy(self.world))

        while True:
            try:
                input = self.inputQueue.get(True, 0.01)
                if input == ord('q'):
                    break
                elif input == ord('w'):
                    self.mainChar.setY(self.mainChar.getY() - 1)
                elif input == ord('s'):
                    self.mainChar.setY(self.mainChar.getY() + 1)
                elif input == ord('d'):
                    self.mainChar.setX(self.mainChar.getX() + 1)
                elif input == ord('a'):
                    self.mainChar.setX(self.mainChar.getX() - 1)
                with self.inputQueue.mutex:
                    self.inputQueue.queue.clear()
            except BaseException:
                pass
            oldTime = time.time()
            self.tick()
            self.entityQueue.put(copy.copy(self.world))
            with self.entityQueue.mutex:
                self.entityQueue.queue.clear()
            sleep(time.time() - oldTime - 0.05 * -1)

    def tick(self):
        for e in self.world.getEntities():
            e.tick()


def main():
    screen = initCurses()
    inputQueue = queue.Queue(1000)
    entityQueue = queue.Queue(1000)

    game = Game(inputQueue, entityQueue, screen)
    game.start()

    newWorld = None
    while True:
        input = screen.getch()
        if input is not -1:
            inputQueue.put(input)
            if input == ord('q'):
                break
        try:
            newWorld = entityQueue.get(True, 0.05) #note this is wasting time (GIL, also we are sharing the same accross threads instead of passing copy)
        except BaseException:
            pass
        for i in range(0, curses.LINES - 1):
            screen.addstr(i, 0, " "*(curses.COLS - 1))
        if newWorld is not None:
            for e in newWorld.getEntities():
                screen.addstr(e.getY(), e.getX(), e.getForm())
            for t in newWorld.getTerrain():
                screen.addstr(t.getY(), t.getX(), t.getForm())
        screen.move(curses.LINES - 1, curses.COLS - 1)
        screen.refresh()
    game.join()
    terminateCurses(screen)


if __name__ == "__main__":
    try:
        main()
    finally:
        curses.nocbreak()
        curses.echo()
        curses.endwin()
