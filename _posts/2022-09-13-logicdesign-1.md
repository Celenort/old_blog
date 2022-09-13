---
title: '논리설계 및 실험 1'
layout: single
categories:
  - study
  - logicdesign
tags: []
---

## Ch 1. Introduction

### Introduction to Digital Logic

- Design : the process of coming up with a solution to a problem while meeting some criteria (ex : size, cost, power, performance)
- Divide-and-conquer approach -> reducing the complexity of the design process by breaking down the problem into smaller pieces. 

### Logic Design

- logic components : have input, output wires that carry digital logic vals.
- Arbitary information can be represented using digital abstraction.
- Transistors react to the voltage lvls on the input wires.
- Sequential logic circuits : react to current vals on the input + past history of values.
- ex) number counter. -> 3, Next (4), Next (5) ...

### Contemporary Logic Design

- Important trends : larger design, shorter time, cheaper product 
- Scale : pervasive use of CAD over hand method. multiple lvls of design
- Time : Abstract design representations, programmable function components, automatic synthesis techniques
- Cost : higher levels of integration. use of simulation to debug -> simulate and verify before you build

### History of Logic Design

- before 19th century
  - Theories of logic (논리학)
- 1850's : George Boole, Boolean algebra
  - Logic -> Algebra. And : x+y, not : x', or : xy
  - x+y = (x' y')' , (x+y)+x'y' = 1 ...
- 1938 : Claude Shannon (Boolean algebra link to switches)
  - Any circuit is represented by a set of equeations.
  - and : 직렬, or : 병렬 연결

### Computation : abstract concept

- Compute (계산) : Abstract view => output = F(input) = f(f(f(... f(input))))
- state : values.
- Functions : sequence of mutators of states.

### Turing machine

- 1936, Alan Turing : invented turing machine. A hypothetical device that manipulates according to a table of rules.

### Turing meets Shannon

- Functions can be implemented by switches.
- ex) 010 + 011 = 101, 
- x, y, Sum, Carry, Sum = xy' + x'y  /  Carry = xy
- Boolean algebra can be used to perform Turing-complete computations.

### History of Logic Design

- 1946, ENIAC. World's first automatic machine to perform Turing-Complete computations -> Computer, 17468 vaccum tubes -> switches.
- 1947 : Transistor. Replaces vaccum tubes. Enable integration of multiple devices into one pachage. 
- 1960's Catalog of logic components
- 1978 : Programmable Array Logic(PAL) -> Undefined function -> must be reconfigured.
- 1984 : Field-programmable gate arrays

### Basic function units of computation

- Representation : "0", "1" on a wire, set of wires (e.g. or binary numbers)
- Assignment : x= y
- Data Operators : x+y-5
- Control : 
  - Sequential statements : A;B;C (A->B->C)
  - Conditionals : if x==1 then y
  - Loops : for(i=1;i<=10;i++)
  - Procedures : A;foo(...);B;
