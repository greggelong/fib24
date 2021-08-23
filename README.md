# fibonacci 24 repeating pattern

## Fibonacci 24 repeating pattern after reduction to single digit

I learned about this pattern from a rather spiritual math Insta post

it linked to the web site:

https://goldennumber.net/fibonacci-24-pattern


The claim is if you do a numeric reduction on the fibonacci sequence

the pattern will repeat after 24 numbers.

I am using an iterative fibonacci generator, because it is faster and I think more

intuitive than a recursive one (however most times recursion is taught using fibonacci as an example!)

However, what I thought was a neat little problem to solve is the reduction

for example take the number 256, 

split into a list [2,5,6]

sum that list= 13

split into a list [1,3]

sum that list = 4

so 256 = 4

Some interesting questions came to mind

how big would the number have to be that you would need to do the reduction

3 times or more?



Answered this question: 

the first fibonacci number that needs to be reduced 3 times is

(index of fib, fibonacci number and (fibonacci reduction and number of times reduced, and [list of reductions]))

18 2584 (1, 3, [19, 10, 1])

18th fibonacci number = 2584, reduces to 1 after 3 reductions

I think it is interesting that some very large numbers 

such as 

> 496 20341574322680408081083829243820203612317308197211964554628215486203974898255803242740333222721700974747 (6, 2, [411, 6])

the 496th fibonacci number reduces to 6 just after 2 reductions!


## bit length of fibonacci numbers

I am making a binary plot visualizer in p5.js 

I would like to make plots of different sequences 

but fibonacci grows quite large and reaches 32 bits by the 47th number

If i am just doing the positive integers N I can get to 255 in just 8 bits

```python
>>> a = 255
>>> a.bit_length()
8
```

here is a link about the binary plot that wolfram mathworld uses

I really like it

https://mathworld.wolfram.com/BinaryPlot.html

link to my binary plot repository

https://github.com/greggelong/binaryPlot

