# Introduction

When the correct solution to the Monty Hall Problem was given by Maralyn vos Savant in 1990 it divided even experienced staticians (https://en.wikipedia.org/wiki/Monty_Hall_problem). The probabilities of winning the game can seem counter-intuitive to many people. This repository was created to show Savant's interpretation to be true using simulated experiments.

## The Monty Hall Problem
The Monty Hall Problem is based around the idea of a gameshow with three doors for which a contestant can choose one in hopes to win the prize. The success of winning the prize is nuanced by the fact that after the contestant selects the first door the host then removes a door and the contestant is given the option to keep their original selection or to switch to the other remaining door.

It seems logical to assume that choosing between three doors should yield a 1/3 probability of success and between two doors a 1/2 probability of success. In actuality, however, by switching doors there is a 2/3 probability of winning the prize while keeping the original door choice maintains the initial 1/3 probability.

An intuitive explanation for why this is the case is that the host is never going to remove the door that contains the prize or the door that was chosen by the contestant. If the contestant did not initially choose the prize door and then switches doors in the second round they will win the prize which explains the 2/3 probability. The contestant initially had a 1/3 chance of winning, which also explains the 1/3 probability of losing if the contestant switches doors. If the contestant did not switch doors at all then they still retain the original 1/3 probability of winning.

## Description

This program performs a number of experiments specified by ITERS in both the not-switching-doors case and the switching-doors case to generate the distributions of winning games. The contestant selected door and the door containing the prize are randomly sampled using the Python random.choice function from the standard library. The results from both cases are output to the console.

## Dependencies

1. Python

## Executing program

```
python index.py
```

## Authors

Steven Berdak<br/>
stevenberdak@gmail.com

## Acknowledgments

Wikipedia: https://en.wikipedia.org/wiki/Monty_Hall_problem