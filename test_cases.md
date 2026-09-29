# Test Cases

## Personal Expense Tracker

The following test cases are used to check whether the Expense Tracker works correctly.

| Test Case | Input                                             | Expected Output                     |
| --------- | ------------------------------------------------- | ----------------------------------- |
| TC01      | Select option 1, enter Food, enter 150            | Expense added                       |
| TC02      | Select option 1, enter Bus, enter 50              | Expense added                       |
| TC03      | Select option 2 after adding expenses             | All recorded expenses are displayed |
| TC04      | Add Food = 150 and Bus = 50, then select option 3 | Total expense = 200.0               |
| TC05      | Select option 2 without adding any expense        | No expenses found                   |
| TC06      | Select option 3 without adding any expense        | Total expense = 0                   |
| TC07      | Select option 4                                   | Thank you                           |
| TC08      | Enter an invalid menu option such as 5            | Invalid choice                      |

## Detailed Test Cases

### TC01 - Add Expense

Input:

```text
1
Food
150
```

Expected Output:

```text
Expense added
```

### TC02 - Add Another Expense

Input:

```text
1
Bus
50
```

Expected Output:

```text
Expense added
```

### TC03 - View Expenses

Input:

```text
2
```

Expected Output:

```text
Expenses:
Food - 150.0
Bus - 50.0
```

### TC04 - Calculate Total Expense

Input:

```text
3
```

Expected Output:

```text
Total expense = 200.0
```

### TC05 - View Empty Expense List

If no expense has been added and the user selects:

```text
2
```

Expected Output:

```text
No expenses found
```

### TC06 - Calculate Total With No Expenses

If no expense has been added and the user selects:

```text
3
```

Expected Output:

```text
Total expense = 0
```

### TC07 - Exit Program

Input:

```text
4
```

Expected Output:

```text
Thank you
```

### TC08 - Invalid Choice

Input:

```text
5
```

Expected Output:

```text
Invalid choice
```

## Result

All the above test cases are used to verify the basic functions of the Personal Expense Tracker.
