**Python Operators**

* **Arithmetic Operators**
  * Used to perform _mathematical operations_
  
    `+` _Addition_ => `a + b`
  
    `-` _Subtraction_ => `a - b`
  
    `*` _Multiplication_ => `a * b`
  
    `/` _Division_ => `a / b`
  
    `%` _Modulus_ => `a % b`
  
    `**` _Power(pow)_ => `a ** b`
  
    `//` _Floor Division_ => `a // b`
  

* **Assignment Operators**
  * Used to _assign values_
  
    `=` => `a = 7`
  
    `+=` => ` a += 5`
  
    `-=` => `a -= 2`
  
    `*=` => `a *= 88`
  
    `/=` => `a /= 223`
  
    `%=` => `a %= 73`
  
    `**=` => `a **= 5`
  
    `//=` => `a //= 9`
  

* **Comparison Operators**
  * They are used to _compare values_  

    `==` _Equal_
  
    `!=` _Not Equal_
  
    `>` _Greater than_
  
    `<` _Less than_
  
    `>=` _Greater than or Equal to_
  
    `<=` _Less than or Equal to_
  

* **Logical Operators**
  * They are used to _combine conditional statements_
  
    `and` _Returns **True** if all conditions **True**_
  
    `or` _Returns **True** either conditions is **True**_
  
    `not` _Returns **False** if result is **True**_


* **Identity Operators**
  * They are used _to compare_ **if** _objects_ are the _same type_
  
    `is` _Returns **True** if of same object._
  
    `is not` _Returns **True** if not same object._
  

* **Membership Operators**
  * They are used to **test** if a _sequence is present in an object_
  
    `in` _Returns **True** if a value found._

    `not in` _Returns **True** if value is not found._


* **Bitwise Operators**
  * They are used to _compare binary numbers_

    `&`	Bitwise `AND`	`x & y` = 0 (0000 0000)
  
    `|`	Bitwise `OR`	`x | y` = 14 (0000 1110)
  
    `~`	Bitwise `NOT`	`~x` = -11 (1111 0101)
  
    `^`	Bitwise `XOR`	`x ^ y` = 14 (0000 1110)
  
    `>>`	Bitwise right shift	`x >> 2` = 2 (0000 0010)
  
    `<<`	Bitwise left shift	`x << 2` = 40 (0010 1000)


**Operator Precedence**
  * This determines the _order_ in which operators should be _evaluated_ if there are multiple operators used in a statement or expression.

    1. `()`	Parentheses
    2. `**`	Exponent
    3. `+x`, `-x`, `~x`	Unary plus, Unary minus, Bitwise NOT
    4. `*`, `/`, `//`, `%`	Multiplication, Division, Floor division, Modulus
    5. `+`, `-`	Addition, Subtraction
    6. `<<`, `>>`	Bitwise shift operators
    7. `&`    Bitwise AND
    8. `^`	Bitwise XOR
    9. `|`	Bitwise OR
    10. `==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in`	Comparisons, Identity, Membership operators
    11. `not`	Logical NOT
    12. `and`	Logical AND
    13. `or`	Logical OR
  
  **Associativity of Python Operators**

  This is the _order_ in which an _expression_ is evaluated that _multiple operators_ of the _same precedence_.
  Almost all operators have _left-right_ associativity