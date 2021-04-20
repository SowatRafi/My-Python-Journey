**Abstraction**

    Abstraction hides the internal details and shows only functionalities.

**Abstract Classes**

    They are classes that contain one or more abstact methods.
    They can not be instantiated.
    They require subclasses to provide implementation for the abstract methods.
    Subclasses of an abstract class in Python are not required to implement abstract methods of the parent class.

**Abstract Methods**

    They are methods that are declared but contains no implementation.
    Requires subclasses to provide implementation for them.



**Python** does not have its own provided ~~abstract classes~~.
**However**, **Python** comes with a module which provides the _infrastructure_ that allows you to define _abstract classes_.
The name of the module in **ABC** => **Abstract Based Classes**

`from abc import ABC, abstractmethod`

`@absractmethod`