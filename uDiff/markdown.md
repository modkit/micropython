# Micropython unsupported operations
  
Generated Tue 24 Jan 2017 14:55:28 AEDT
## Function
---
Assign instance variable to function

Unsupported

Sample code:  

```python
def f():
    pass

f.x = 0
print(f.x)
```

CPy output:  

```python
0
```

uPy output:  

```python
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
AttributeError: 'function' object has no attribute 'x'
```

## Modules
---
### .array
---
Looking for integer not implemented

Unsupported

Sample code:  

```python
import array
print(1 in array.array('B', b'12'))
```

CPy output:  

```python
False
```

uPy output:  

```python
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NotImplementedError: 
```

Array deletion not implemented

Unsupported

Sample code:  

```python
import array
a = array.array('b', (1, 2, 3))
del a[1]
print(a)
```

CPy output:  

```python
array('b', [1, 3])
```

uPy output:  

```python
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
TypeError: 'array' object does not support item deletion
```

Subscript with step != 1 is not yet implemented

Unsupported

Sample code:  

```python
import array
a = array.array('b', (1, 2, 3))
print(a[3:2:2])
```

CPy output:  

```python
array('b')
```

uPy output:  

```python
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
NotImplementedError: only slices with step=1 (aka None) are supported
```

### .deque
---
Deque not implemented

Unsupported

Sample code:  

```python
import collections
D = collections.deque()
print(D)
```

CPy output:  

```python
deque([])
```

uPy output:  

```python
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
AttributeError: 'module' object has no attribute 'deque'
```

### .struct
---
### ..pack
---
Struct pack with too few args, not checked by uPy

Unsupported

Sample code:  

```python
import struct
try:
    print(struct.pack('bb', 1))
    print("shouldn't get here")
except:
    print('struct.error')
```

CPy output:  

```python
struct.error
```

uPy output:  

```python
b'\x01\x00'
shouldn't get here
```

Struct pack with too many args, not checked by uPy

Unsupported

Sample code:  

```python
import struct
try:
    print(struct.pack('bb', 1, 2, 3))
    print("shouldn't get here")
except:
    print('struct.error')
```

CPy output:  

```python
struct.error
```

uPy output:  

```python
b'\x01\x02'
shouldn't get here
```

## Syntax
---
### .Spaces
---
uPy requires spaces between literal numbers and keywords, CPy doesn't

Unsupported

Sample code:  

```python
try:
    print(eval('1and 0'))
except SyntaxError:
    print('Should have worked')
try:
    print(eval('1or 0'))
except SyntaxError:
    print('Should have worked')
try:
    print(eval('1if 1else 0'))
except SyntaxError:
    print('Should have worked')
```

CPy output:  

```python
0
1
1
```

uPy output:  

```python
Should have worked
Should have worked
Should have worked
```

### .Unicode
---
Unicode name escapes are not implemented

Unsupported

Sample code:  

```python
print(exec('"\\N{LATIN SMALL LETTER A}"'))
```

CPy output:  

```python
None
```

uPy output:  

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NotImplementedError: unicode name escapes
```

## Types
---
### .Exceptions
---
Assign instance variable to exception

Unsupported

Sample code:  

```python
e = Exception()
e.x = 0
print(e.x)
```

CPy output:  

```python
0
```

uPy output:  

```python
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
AttributeError: 'Exception' object has no attribute 'x'
```

### .bytearray
---
Array slice assignment with unsupported RHS

Unsupported

Sample code:  

```python
b = bytearray(4)
b[0:1] = [1, 2]
print(b)
```

CPy output:  

```python
bytearray(b'\x01\x02\x00\x00\x00')
```

uPy output:  

```python
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NotImplementedError: array/bytes required on right side
```

### .bytes
---
bytes(...) with keywords not implemented

Unsupported

Sample code:  

```python
print(bytes('abc', encoding='utf8'))
```

CPy output:  

```python
b'abc'
```

uPy output:  

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NotImplementedError: keyword argument(s) not yet implemented - use normal args instead
```

Bytes subscr with step != 1 not implemented

Unsupported

Sample code:  

```python
print(b'123'[0:3:2])
```

CPy output:  

```python
b'13'
```

uPy output:  

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NotImplementedError: only slices with step=1 (aka None) are supported
```

### .float
---
uPy and CPython outputs formats differ

Unsupported

Sample code:  

```python
print('%.1g' % -9.9)
print('%.1e' % 9.99)
print('%.1e' % 0.999)
```

CPy output:  

```python
-1e+01
1.0e+01
1.0e+00
```

uPy output:  

```python
-10
1.00e+01
1.00e-00
```

### .list
---
List delete with step != 1 not implemented

Unsupported

Sample code:  

```python
l = [1, 2, 3, 4]
del l[0:4:2]
print(l)
```

CPy output:  

```python
[2, 4]
```

uPy output:  

```python
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NotImplementedError: 
```

List store with step != 1 not implemented

Unsupported

Sample code:  

```python
l = []
l[1:2:3] = []
print(l)
```

CPy output:  

```python
[]
```

uPy output:  

```python
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NotImplementedError: 
```

### .str
---
str(...) with keywords not implemented

Unsupported

Sample code:  

```python
print(str(b'abc', encoding='utf8'))
```

CPy output:  

```python
abc
```

uPy output:  

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NotImplementedError: keyword argument(s) not yet implemented - use normal args instead
```

Subscript with step != 1 is not yet implemented

Unsupported

Sample code:  

```python
print('abcdefghi'[0:9:2])
```

CPy output:  

```python
acegi
```

uPy output:  

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NotImplementedError: only slices with step=1 (aka None) are supported
```

### ..endswith
---
str.endswith(s, start) not implemented

Unsupported

Sample code:  

```python
print('abc'.endswith('c', 1))
```

CPy output:  

```python
True
```

uPy output:  

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NotImplementedError: start/end indices
```

### ..format
---
Attributes/subscr not implemented

Unsupported

Sample code:  

```python
print('{a[0]}'.format(a=[1, 2]))
```

CPy output:  

```python
1
```

uPy output:  

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NotImplementedError: attributes not supported yet
```

### ..rsplit
---
str.rsplit(None, n) not implemented

Unsupported

Sample code:  

```python
print('a a a'.rsplit(None, 1))
```

CPy output:  

```python
['a a', 'a']
```

uPy output:  

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NotImplementedError: rsplit(None,n)
```

### .tuple
---
Tuple load with step != 1 not implemented

Unsupported

Sample code:  

```python
print((1, 2, 3, 4)[0:4:2])
```

CPy output:  

```python
(1, 3)
```

uPy output:  

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NotImplementedError: only slices with step=1 (aka None) are supported
```

## sys
---
Override sys.stdin, sys.stdout and sys.stderr. Impossible as they are stored in read-only memory.

Unsupported

Sample code:  

```python
import sys
sys.stdin = None
print(sys.stdin)
```

CPy output:  

```python
None
```

uPy output:  

```python
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
AttributeError: 'module' object has no attribute 'stdin'
```

