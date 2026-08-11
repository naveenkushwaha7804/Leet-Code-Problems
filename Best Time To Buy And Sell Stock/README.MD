# LeetCode 121 - Best Time to Buy and Sell Stock

## Problem

Given an array of stock prices where `prices[i]` represents the price of a stock on the `i-th` day, find the maximum profit that can be achieved by buying on one day and selling on a later day.

If no profit can be made, return `0`.

## Approach

Use a single pass through the array:

- Keep track of the minimum price seen so far.
- Calculate the profit by selling at the current price.
- Keep track of the maximum profit.

This ensures that the stock is always bought before it is sold.

## Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

## Example

```text
Input:  prices = [7,1,5,3,6,4]
Output: 5