# By Evan Dempsy, Dublin
# with modifications by Huilherme Feulo and Fabio Kon 

######################################
####### Abstract Classes #############
######################################

class Observer(object):
    """
    Abstract class to respond to changes in the subject.
    """
    def update():
        """
        Update observer state.
        """
        raise NotImplementedError("method update() was not implemented")

class Subject(object):
    """
    Maintains a list of observers and notifies
    them of state changes
    """

    def __init__(self) -> None:
        """
        Initialize a list of observers
        """
        self.__dict__["state"] = 0
        self.__dict__["observers"] = set()

    def __setattr__(self, __name: str, __value: Observer) -> None:
        """
        Override to notify observers of state 
        changes when the state is updated.
        """
        self.__dict__[__name] = __value
        if __name == "state":            # if the state changes, automatically notify_observer is called.
            self.notify_observers()

    def register(self, observer: Observer) -> None:
        """
        Add an observer to the list of observers
        to be notified of state changes.
        """
        self.observers.add(observer)

    def deregister(self, observer: Observer) -> None:
        """
        Remove a observer.
        """
        self.observers.remove(observer)

    def notify_observers(self) -> None:
        """
        Iterate through observers and call the update method.
        """
        for observer in self.observers:
            observer.update()

######################################
####### Concrete Classes #############
######################################

class BinaryObserver(Observer):
    def __init__(self, subject: Subject) -> None:
        self.subject = subject
        self.subject.register(self)

    def update(self) -> None:
        print(f"\t in binary: {bin(self.subject.state)}")

class HexObserver(Observer):
    def __init__(self, subject: Subject) -> None:
        self.subject = subject
        self.subject.register(self)

    def update(self) -> None:
        print(f"\t in hexadecimal: {hex(self.subject.state)}")

class OctalObserver(Observer):
    def __init__(self, subject: Subject) -> None:
        self.subject = subject
        self.subject.register(self)

    def update(self) -> None:
        print(f"\t in octal: {oct(self.subject.state)}")

def main() -> None:
    subject = Subject()
    BinaryObserver(subject)
    OctalObserver(subject)
    HexObserver(subject)

    print("First state change:\n")
    subject.state = 1024

    print("Second state change:\n")
    subject.state = 255

if __name__=="__main__":
    main()