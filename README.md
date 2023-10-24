[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/h1zN233T)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12544721&assignment_repo_type=AssignmentRepo)
# Python-algorithmic_thinking-bubblesort

Implement the bubblesort presented in pseudo code below in Python in the ``bubblesort.py`` file. Then run the ``app.py`` file to test your implementation. The output should be "Congratulations! No error detected.".

```
BEGIN BubbleSort(list)
  swaps = false
  FOR i FROM zero TO (LENGTH OF list MINUS 1)
    IF list[i] > list[i+1]
      SWAP(list[i], list[i+1])
      swaps = true
    ENDIF
  ENDFOR
  IF swaps == true
    BubbleSort(list)
  ENDIF
  RETURN list
END BubbleSort
```
