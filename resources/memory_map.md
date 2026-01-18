
## 0. One rule that kills 80% confusion

> **If a data structure is mutable, it has “add/modify” methods.
> If it is immutable, it has none.**

Keep this in mind while reading.

---

## 1. Core memory map (this is the one to memorize)

```
LIST  → ordered, mutable, indexed
SET   → unordered, mutable, unique
DICT  → key → value, mutable
TUPLE → ordered, immutable
```

Now the **operations map** 👇

---

## 2. Operations memory map (side-by-side)

| Structure | Add ONE item | Add MANY           | Modify       | Remove                    |
| --------- | ------------ | ------------------ | ------------ | ------------------------- |
| **list**  | `append(x)`  | `extend(iterable)` | `lst[i] = x` | `remove(x)`, `pop()`      |
| **set**   | `add(x)`     | `update(iterable)` | ❌ (no index) | `remove(x)`, `discard(x)` |
| **dict**  | `d[k] = v`   | `update({...})`    | `d[k] = v`   | `pop(k)`, `del d[k]`      |
| **tuple** | ❌            | ❌                  | ❌            | ❌                         |

If this table is not crystal clear, do not move forward.

---

## 3. Why names differ (important mental model)

Python names methods based on **intent**, not consistency.

### LIST

* `append` → “attach to the end”
* `extend` → “extend with another sequence”

Example:

```python
lst = [1, 2]
lst.append(3)        # [1, 2, 3]
lst.extend([4, 5])   # [1, 2, 3, 4, 5]
```

⚠️ Trap:

```python
lst.append([4,5])    # [1, 2, 3, [4,5]]  ❌
```

---

### SET

* No order → no index → no `append`
* Uses mathematical language

```python
s = {1, 2}
s.add(3)             # {1,2,3}
s.update([4,5])      # {1,2,3,4,5}
```

⚠️ Trap:

```python
s[0] = 10   # ERROR – sets have no index
```

---

### DICT

Dictionary is **mapping**, not sequence.

```python
d = {}
d["age"] = 21         # add
d["age"] = 22         # modify
```

Same operation. No separate “add vs update” at key level.

Bulk update:

```python
d.update({"city": "Delhi", "year": 2025})
```

---

### TUPLE

Immutable by design.

```python
t = (1, 2)
t.append(3)   # ERROR
```

Why tuples exist?

* Fixed records
* Hashable
* Safer (cannot be modified accidentally)

---

## 4. Ultra-short cheat sheet (pin this)

```
list  → append / extend
set   → add / update
dict  → d[key] = value / update
tuple → nothing (immutable)
```

---

## 5. Common failure modes (read carefully)

### ❌ Expecting consistency

Python is pragmatic, not “perfectly uniform”.

### ❌ Treating set like list

If you think in indexes → use list.

### ❌ Treating tuple like list

If data changes → tuple is wrong choice.

### ❌ Forgetting mutability

If it changes in place → mutable
If it creates new object → immutable

---

## 6. One hard question for you (do not skip)

Answer without running code:

```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

If you hesitate, your mental model of mutability is incomplete.

---

## 7. Minimal fix to your confusion

Do **not** memorize method names randomly.

Instead, memorize **this decision flow**:

```
Do I need order? → list / tuple
Do I need uniqueness? → set
Do I need key-value? → dict
Do I need mutability? → not tuple
```

Then method names become obvious.

---

