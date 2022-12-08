

### To keep in mind

Design patterns are best used in large projects and/or large code bases. On single files or 100 or so lines, it is a complete overkill. It decreases readability, increases complexity and bloat on key parts of the code base BUT should improve extensibility and maintability when needed. While these small stubs are too trivial to fully appreciate the problem, they are still good to illustrate the theory and at having a try at coding the solution.

# Strategy aka Policy pattern
Main idea: You want to leave things open for run time. You extract as much as possible individual classes into separate "strategies" classes and have an interface that can call them all. you can extend you code just "under" the interface by adding new behviours as long as they can cope with the interface that interacts with them all.

Buzz-words: extends/implements, new/instantation, manage the concrete, encapsulation/inheritance

Mostly adapted from: 
The strategy pattern: write BETTER PYTHON CODE Part 3 - ArjanCodes on YouTube
https://www.youtube.com/watch?v=WQ8bNdxREHU
https://github.com/ArjanCodes/betterpython/tree/main/3%20-%20strategy%20pattern

### Strategy pattern - technical overview
Code in plain language: Interface "IMyStrategy" acts up 2 variables through a method. Under it, there is a class MyConcreteAddition that implements IMyStrategy and returns the result of an addition; there is also the same for substration. Now we can extend with division and multiplication without any issues. 
"Composition is better than inheritance:" Also you dont need to create sub classes like the wild duck vs the rubber duck when you have a duck class with 3 interfaces  - for how they look, how they quack and how they fly. You then have concrete implementations of the display(), quack() and fly() methods inside the interface. These concrete implementations get injected into the class through the interface (starts with I by convention). You can compose any duck you want without needing the have inheritance chains. The class will typically create variable and have a constructor. The constructor will repeat some variables with this. = to say that the instance created is linked to a variable that stores an object of the given interface.

Examples of when?: You have a lot of duplicate code within your classes. You can extract it into the interface the part that is common.  - You want to be able to select an behaviour at run time. - solving issues following Open/Closed principle.

Similar but dissimilar to other patterns: Strategy is more about changing parts of the object behaviours that Decorator, Template and State don't have. It solves other problems than Command, State, Bridge and Adapter.

### Strategy pattern - python overview
Key syntax considerations:
1 - from abc import ABC, abstractmethod => key imports to get coding 
2- Alternatively you can go less verbose and use Callable without abstract as in the 01-strategy.py
3- Put a I if you use interfaces to compose. Not used in the example.

=======================


# Observer pattern
Main idea: You want to leave things open for run time. You extract as much as possible individual classes into separate "strategies" classes and have an interface that can call them all. you can extend you code just "under" the interface by adding new behaviours as long as they can cope with the interface that interacts with them all. Pull would be querying all the time if something has changed every x seconds. We dont do it  here. We only get info when something has changed. All subscribers get notified. Need some form state or at least data object to push data from and the collection of subscribers to notify. 

Buzz-words: get/set/update/somethingHasChanged, publisher and subscribers, subject (observeable aka data aka publisher) vs observer (ex display or subscriber), push not pull. 

 

### Observer pattern - technical overview
Code in plain language: Interface "IPublisher" has a relationship one (the IPublisher) to many Interface "IObserver"s. Inside the IPublisher you can addSubscriber - removeSubscriber - notifySubscribers. Typically Add and Remove would have an argument of type IObserver but notify would not have any arguments. The IOberserver has a update method -I repeat update is with the subscriber, notify is with the publisher! The update() method will react on notifications - but typically the publisher will directly call the update method of the Iobserver, a method outside of its class. The Concrete implementations should have all these 4 but ALSO get and set that are not needed at Interface level. Set typically would have a lot more code around it. 

The Observable concretes does almost 2 things and is borderline for Single Responsibility. It does pure observable stuff (add/remove/notify) + state stuff (get/set). You pass the concrete subscriber to the concrete publisher so it knows to add/remove. You pass the data and call update through notify on the other direction from publisher to subscriber. It is counterintuitively two ways in the code. This allows to avoid having a argument to update and to notify.

The add method wants to receive also the update function in it so it can call it. The Notify method inside the Publisher will have an iteration over the collection and call update() that it can access on each. There will be a this. to be able to find the right one.

So to remain single responsibility when you instantiation
1- create a new fresh Publisher without argument. 
2- Then a new Subscriber with the Publisher as argument.


Examples of when?: chatroom - weather station - event system

Similar but dissimilar to other patterns: There are many variations around the same concept. "Publish-Subscribe" is more loose on registration requirements (observer/observable know less of each other and/or of the content being exchanged). "Mediator" is another flavour with accents on having a dispatcher that distributes to avoid one to many relationship.  "Hooks" flavour is more towards fixed integration points that allow certain actions. Then there are a lot of patterns around "events", generally the main difference here tends to be that event patterns focus on messages/requests asynchronously as coding blocks while observer calls notify/update coding blocks synchronously.

### Observer pattern - python overview
Key syntax considerations:
1 - there are lots of event libraries that are stand-alone in python, you dont really need to write your own. They each have slightly different variations of observer. Blinker and pydispatcher are amongst the most popular.
2- You can reduce the imports by using these techniques.
3- self is used as first parameter when you use it. It typically indicate that you will instantiate that object and then do a bunch of stuff to it in the code inside the class. See observer_lib/db.py. Also they go along with def __new__ (or most often nothing) to create the blueprint (consturctor) and __init__ to inialize it. Self is great to refactor into better cohesion (do one thing) and loose coupling (one change somewhere else means many changes there). More about this and initializers https://www.youtube.com/watch?v=eiDyK_ofPPM



=======================

Still has observer data inside

# Singleton pattern
Main idea: You want to leave things open for run time. You extract as much as possible individual classes into separate "strategies" classes and have an interface that can call them all. you can extend you code just "under" the interface by adding new behaviours as long as they can cope with the interface that interacts with them all. Pull would be querying all the time if something has changed every x seconds. We dont do it  here. We only get info when something has changed. All subscribers get notified. Need some form state or at least data object to push data from and the collection of subscribers to notify. 

Buzz-words: get/set/update/somethingHasChanged, publisher and subscribers, subject (observeable aka data aka publisher) vs observer (ex display or subscriber), push not pull. 


### Observer pattern - technical overview
Code in plain language: Interface "IPublisher" has a relationship one (the IPublisher) to many Interface "IObserver"s. Inside the IPublisher you can addSubscriber - removeSubscriber - notifySubscribers. Typically Add and Remove would have an argument of type IObserver but notify would not have any arguments. The IOberserver has a update method -I repeat update is with the subscriber, notify is with the publisher! The update() method will react on notifications - but typically the publisher will directly call the update method of the Iobserver, a method outside of its class. The Concrete implementations should have all these 4 but ALSO get and set that are not needed at Interface level. Set typically would have a lot more code around it. 

The Observable concretes does almost 2 things and is borderline for Single Responsibility. It does pure observable stuff (add/remove/notify) + state stuff (get/set). You pass the concrete subscriber to the concrete publisher so it knows to add/remove. You pass the data and call update through notify on the other direction from publisher to subscriber. It is counterintuitively two ways in the code. This allows to avoid having a argument to update and to notify.

The add method wants to receive also the update function in it so it can call it. The Notify method inside the Publisher will have an iteration over the collection and call update() that it can access on each. There will be a this. to be able to find the right one.

So to remain single responsibility when you instantiation
1- create a new fresh Publisher without argument. 
2- Then a new Subscriber with the Publisher as argument.


Examples of when?: chatroom - weather station - event system

Similar but dissimilar to other patterns: There is nothing quite like it. But there are variations of it. Publish-Subscribe is sometimes seem as different as people put more strict sense on the event existing at time of registration or not. Hooks is for fixed integration points that allow certain actions.

### Singleton pattern - main criticisms

### Observer pattern - python overview
Key syntax considerations:
1 - there are lots of event libraries that are stand-alone in python, you dont really need to write your own. They each have slightly different variations of observer. Blinker and pydispatcher are amongst the most popular.
2- You can reduce the imports by using these techniques.
3- self is used as first parameter when you use it. It typically indicate that you will instantiate that object and then do a bunch of stuff to it in the code inside the class. See observer_lib/db.py. Also they go along with def __new__ (or most often nothing) to create the blueprint (consturctor) and __init__ to inialize it. Self is great to refactor into better cohesion (do one thing) and loose coupling (one change somewhere else means many changes there). More about this and initializers https://www.youtube.com/watch?v=eiDyK_ofPPM



