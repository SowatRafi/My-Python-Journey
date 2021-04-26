**Exceptions**

 * **Exception**s are **error**s that occurs during the _execution_ of the _program_.

**Handling Exceptions**

 * **Errors** can be handled or caught by embedding your _code_ in `try` and `except` statement blocks.
 * There has to be at least one `except` clause with every `try` clause.
 * The handlers for the _specific_ **errors** are placed inside the `except` block.
 * The default **Python** handler is called if no handler is _specified_.

**Keywords Used in Handling Exceptions**

 * `try` **block**: Lets you **test** a **block** of _code_ for the _errors_.
 * `except` **block**: Lets you _specify_ how to handle the **errors**.
 * `finally` **block**: Lets you _specify_ what _code_ to **execute** regardless of _what happens_ in `try` and `except` **block**.
 * `else` **block**: Lets you _specify_ what _code_ to _execute_ if **no exceptions** occurs. _This is optionally used._


**_Syntax for handling Exceptions:_**

    try:
        code to test for errors

    except:
        code to execute to handle errors

    finally:
        code to execute regardless of errors

    else:
        code to execute if no errors