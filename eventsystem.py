import queue
import event

class eventsystem:
    def __init__(self):
        self.eventList = {}
        pass

    def registerSelf(self, event, callerQueue):
        if event.getName() in self.eventList:
            self.eventList[event.getName()].append(callerQueue)
        else:
            self.eventList[event.getName()] = [callerQueue]

    def callEvent(self, event):
        for evnt, queueList in self.eventList.items():
            if event.getName() == evnt.getName():
                queueList.put(event)
                break;
