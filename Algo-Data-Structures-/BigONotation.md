<h1>Big O notation - Time Complexity </h1>
<h2>O(1)</h2>
<p>no for loop or anything just easy transactions</p>
```
Def foo:
    return 1 + 2
```
<h2>O(n)</h2>
One for loop
```
for i in range(0,10):
    print(i)
```
<h2>O(n^2)</h2>
Two for loops one being nested<br>
```
for i in range(0,10):
    for x in range(0,10):
        print(x)
```
If it is
```
for i in range(0,10):
    for x in range(0,10):
        print(x)
for i in range(0,10):
    print(i)
```
This is O(n^2) you keep the slowest running speed
	