

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
Code in plain language: Interface "MyStrategy" acts up 2 variables through a method. Under it, there is a class MyConcreteAddition that implements MyStrategy and returns the result of an addition; there is also the same for substration. Now we can extend with division and multiplication without any issues.

Examples of when?: You have a lot of duplicate code within your classes. You can extract it into the interface the part that is common.  - You want to be able to select an behaviour at run time. - solving issues following Open/Closed principle.

Similar but dissimilar to other patterns: Strategy is more about changing parts of the object behaviours that Decorator, Template and State don't have. It solves other problems than Command, State, Bridge and Adapter.

### Strategy pattern - python overview
Key syntax considerations:
1 - from abc import ABC, abstractmethod => key imports to get coding



# Observer pattern
Main idea: You want to leave things open for run time. You extract as much as possible individual classes into separate "strategies" classes and have an interface that can call them all. you can extend you code just "under" the interface by adding new behviours as long as they can cope with the interface that interacts with them all.
some state or at least data object to pull data from. subject vs observer

Buzz-words: get/set/update/somethingHasChanged, publisher and subscribers, data 


### Strategy pattern - technical overview
Code in plain language: Interface "MyStrategy" acts up 2 variables through a method. Under it, there is a class MyConcreteAddition that implements MyStrategy and returns the result of an addition; there is also the same for substration. Now we can extend with division and multiplication without any issues.

Examples of when?: You have a lot of duplicate code within your classes. You can extract it into the interface the part that is common.  - You want to be able to select an behaviour at run time. - solving issues following Open/Closed principle.

Similar but dissimilar to other patterns: Strategy is more about changing parts of the object behaviours that Decorator, Template and State don't have. It solves other problems than Command, State, Bridge and Adapter.

### Strategy pattern - python overview
Key syntax considerations:
1 - from abc import ABC, abstractmethod => key imports to get coding
2- put a i at the beggining if doing it with an interface




2- put a i at the beggining if doing it with an interface