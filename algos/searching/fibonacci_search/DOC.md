# Fibonacci Search
Fibonacci search technique is a method of searching a sorted array using
a divide and conquer algorithm that narrows down possible locations with
the aid of Fibonacci numbers.

Beginning with an array containing Fj-1 elements, the length of the
subset is bounded to Fj-1-1 elements. To search through a range with a
length of Fn-1 at the beginning we have to make n comparisons in the
worst case. Fn=(1/sqrt(5))*((1+sqrt(5))/2)n, that's approximately
c*1,618n (with a constant c). For N+1 = c*1,618n elements we need n
comparisons, i.e. the maximum number of comparisons is O (ld N).

# Algorithm:
Given a table of records R1, R2, ..., RN whose keys are in increasing
order K1 < K2 < ... < KN, the algorithm searches for a given argument K.
Assume N+1 = Fk+1

	Step 1 − [Initialize] i ← Fk, p ← Fk-1, q ← Fk-2 (throughout the algorithm, p and q will be consecutive Fibonacci numbers)
    Step 2 − [Compare] If K < Ki, go to Step 3; if K > Ki go to Step 4; and if K = Ki, the algorithm terminates successfully.
    Step 3 − [Decrease i] If q=0, the algorithm terminates unsuccessfully. Otherwise set (i, p, q) ← (p, q, p - q) (which moves p and q one position back in the Fibonacci sequence); then return to Step 2
    Step 4 − [Increase i] If p=1, the algorithm terminates unsuccessfully. Otherwise set (i,p,q) ← (i + q, p - q, 2q - p) (which moves p and q two positions back in the Fibonacci sequence); and return to Step 2

# Pseudocode
```
 1  function fibonacci_search(item: integer; arr: sort_array) return index
 2  is
 3      l : index := arr'first; -- first element of array
 4      u : index := arr'last; -- last element of array
 5      m : index := (u+l)/2;
 6      x,a,b : integer;
 7  begin
 8      a := (Fn-3);
 9      b := (Fn-2)-(Fn-3);
10      discrete (f2,f1) := (Fn-2,Fn-3)
11          new (f2,f1) := (f2-f1,2*f1-f2) | (a,b)
12      with i := u-l+1
13          new i=i/2 loop
14      loop
15          if item < arr(m) then
16              m := m-f1; -- compute new position of compared element
17              f2 := f2-f1;
18              f1 := f1-f2;
19          elsif item > arr(m) then
20              m := m+f1; -- compute new position of compared element
21              x := f1;
22              f1 := f2-f1;
23              f2 := x;
24              a := f2; b := f1;
25          else
26              return m; -- return index of found item
27          end if;
28          i := i/2;
29      end loop;
30  end fibonacci_search;
```
