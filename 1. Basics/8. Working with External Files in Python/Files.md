**Modes**

* `r`	Opens a file for reading. (default)

* `r+`	Opens a file for reading and writing to file.

* `w`	Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.

* `w+`	Opens a file for writing and reading.

* `x`	Opens a file for exclusive creation. If the file already exists, the operation fails.

* `a`	Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.

* `t` Opens in text mode. (default)

* `b`	Opens in binary mode. (Images or videos)

* `+`	Opens a file for updating (reading and writing)



**Python File Handling Built-in Functions**

* `open()` Used to open files. Takes two arguments; filename & mode

* `read()` Used to read the entire file content.

* `readline()` Used to read one line in a file.

* `readlines()` Used to read file and returns a list of lines.

* `write()` Used to write to a file.

* `writelines()` Used write a list of strings.

* `append()` Used to append to existing file.

* `close()` Used to close file when you are done.


**File Pointer**

* Determines where any operation on a file starts.
* If files is in default access `r` mode it is set to the start of the file.
* `tell()` can show your current file pointer position.
* `seek()` is used to set position of pointer.