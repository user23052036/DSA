**`typing` is a module used to describe what types your variables *should* have — for humans and tools, not for Python itself.**

Key points:

* It adds **type hints**, not behavior
* Python **ignores it at runtime**
* Used by **linters, IDEs, and type checkers**
* Makes code **easier to read, review, and maintain**

Example:

```python
from typing import List

nums: List[int] = [1, 2, 3]
```

This does **not** enforce integers.
It only **documents intent**.

Bottom line:

* `typing` = documentation + static analysis
* `list`, `int`, etc. = actual runtime objects

---
`enumerate` lets you loop **with both index and value at the same time**.

```python
for i, num in enumerate(nums):
```

Means:

* `i` → index (0, 1, 2, …)
* `num` → value at that index

So this:

```python
ans[i] = ans[i + n] = num
```

* Puts `num` at position `i`
* Also puts `num` at position `i + n`

Equivalent to writing (but worse):

```python
i = 0
for num in nums:
    ans[i] = ans[i + n] = num
    i += 1
```

Why `enumerate` is better:

* Cleaner
* No manual counter
* Fewer bugs

In short:
**`enumerate` = index + value in one loop.**

---

