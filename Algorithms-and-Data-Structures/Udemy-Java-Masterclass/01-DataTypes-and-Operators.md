# Primitive data types

* 8 Primitive Data Types
  * 4 data types of whole numbers
    * byte
      * Occupies 8 bits
      * Wrapper class: Byte
      * `Byte.MIN_VALUE = -128 = -2^7`
      * `Byte.MIN_VALUE = 127 = 2^7 - 1`
    * short
      * Occupies 16 bit
      * Wrapper class: Short
      * `Short.MIN_VALUE = -2^15`
      * `Short.MIN_VALUE = 2^15 - 1`
    * int
      * Occupies 32 bits
      * Wrapper class: Integer
      * `Integer.MIN_VALUE = -2^31`
      * `Integer.MAX_VALUE = 2^31 - 1`
    * long
      * Occupies 64 bit (include L at the end of number)
      * Wrapper class: Long
      * `Long.MIN_VALUE = -2^63`
      * `Long.MIN_VALUE = 2^64 - 1`
  * 2 data tyeps for floating point numbers
    * float
      * Occupies 32 bits
      * Wrapper class: Float
      * `Float.MIN_VALUE = 1.4E-45`
      * `Float.MIN_VALUE = 3.4028235E38`
    * double
      * Occupies 64 bits
      * Wrapper class: Double
      * `Double.MIN_VALUE = 4.9E-324`
      * `Double.MIN_VALUE = 1.7976931348623157E308`
  * 2 other data types
    * char
      * Occupies 16 bits
      * Can store only one character, e.g. `char myChar = 'D';`
      * Note the use of single quotation instead of double quotation mark. Double quotation mark is used for String data type.
      * Unicode equivalent: `char myChar = '\u0044';`
        * Unicode table: unicode-table.com
    * boolean
      * Takes a value of either `true` or `false`
      * Example: `boolean isCustomerOverTweentyOne = true;`


# Operators
* Basics and terminologies
  * Let say, `int myVal = valA + valB`
  * Operator: `=` and `+`
  * Operand: `valA` and `valB`
  * Expression: `myVal = valA + valB`
  * Statement: `int myVal = valA + valB`

* Commenting in Java
  * Line comment
  ```
  // This is a commented line
  ```
  * Section comment
  ```
  /*
  Commented code here, could be
  in different lines
  */
  ```
  
* Arithmetic operators
  * Add `+`, subtract `-`, divide `/`, multiply `*`, modulus `%`
  * Abbreviations: `i++`, `i--`, `i += 2`, `i *= 2`
  
* Assignment operator
  * `=`

* Comparison operators
  * `==`, `!=`, `<`, `>`, `<=`, `>=`

* Logical operators
  * Logical AND `&&`, Logical OR `||`, Logical NOT `!`

* Bitwise operators
  * AND `&`, OR `|`, XOR `^`, NOT `~`

* Ternary operators
  * Example: Following code implies: if isWater is true then isLife is true, else isLife is false)
  ```
  boolean isWater = false;
  boolean isLife = isWater ? true : false;
  ```
