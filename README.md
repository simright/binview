# binview
A Python command line utility for printing data in binary files


# Usage: 
  ```python /path/to/binview.py [OPTIONS]```

# OPTIONS:
  ```
  -h --help:    List instructions
  -t DATA_TYPE: DATA_TYPE defines data type as consistent as python array:
               (https://docs.python.org/2/library/array.html)
              
                f=float
                i=singned int
                I=unsigned int
                h=signed short
                H=unsigned short
              
  -f BIN_FILE:  BIN_FILE is the binary file path
  -s START:     Starting entry for output (default=0, the first value in data)
  -e END:       Ending entry for output (default=-1, the last value in data)
                -s 0 -e 100, prints data[0], ..., data[99]
  ```