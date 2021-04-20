**Functions**

    Are pieces(block) of code that does something.
    They are resuable.
    They execute or run when called by their name.
    They can have parameters(variables) and arguments(values)
    They can return data as result.
    There are built-in functions. Example: printt() 

**Creating a Function**

    Descriptive names.
    Same naming rules as variables.

**Calling a Function**

    Also known as: running, executing, invoking
    You can call a function by it's name and parenthesis.
    Any paremeters or arguments are placed inside the parenthesis.

**Parameter vs Arguments**

    A parameter is a variable defined inside a functions's parenthesis.
    An argument is the actual value you pass(give) the function when it is called.

**Return value**

    This is used inside a function to return a value.

**Default Parameter Value**

    This is the value a function uses when called without passing it a value.
    Only parameters at the end of a parameter list can have a default value as Values are assigned by position.
    Example: def greeting(a, b=34)

**Keyword Arguments**

    Allows you to specify what parameters to use from a list of parameters.
    You do not need to worry about the order of the arguments.
    Allows you to give values only to parameters you want provied the other parameters have dafault argument values.

**Global vs Local variable scope**

    Variables defined inside a function body have a local scope.
    Variables defined outside a function body have a global scope.
    Global variables can be accessed anywhere in your python file.
    Local variables can only be accessed inside the function it belongs to.

**Using Global keyword**

    This is to make the value of a local varibale global.

**Pass Statement**

    This is used to indicate the function has empty block or statements.

**VarArgs Parameters**

    Lets you define variable number of arguments for a function.
    This is doing using *
    (*) -> Tuple
    (**) -> Dictionary

**Anonymous Functions(Lambda)**

    They are defined using the lambda keyword.
    They can take several arguments but only have one expression.

**DocStrings(Document String)**

    Allows you to display code documentation when code executes.
    They are accessed by using double underscore with attribute name.
    They are defined using three single quotes and some text.

**Python Decorators**

    Decorators are used to add new functionality to existing objects like functions, methods and classes without modifying its structure.
    Decorators are usually called before the defination of the object (Function, Method, Class) we want to decorate.
    They can be represented by @ followed by name of the decorate object.