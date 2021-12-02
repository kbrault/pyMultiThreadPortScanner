# pyMultiThreadPortScanner
A simple python multithreaded port scanner

# Usage
Change these following variables 
``` python
ports = range(1, 999)
host = "1.1.1.1"
threads_number = 200
```
And run
``` sh
$ .\python main.py

1.1.1.1        :   80 open
1.1.1.1        :   53 open
1.1.1.1        :  443 open
```
