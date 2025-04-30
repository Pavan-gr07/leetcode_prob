def sort012(arr):
    def helper(n,start):
        i=start
        j=start
        while i<len(arr):
            if arr[i] == n:
                arr[i],arr[j] = arr[j] ,arr[i] 
                j+=1
            i+=1
        return j
    

    if not arr:
        return []
    l= 0
    l = helper(0,l)
    l=helper(1,l)
    l= helper(2,l)
    print(arr)
    
# Yes, 100%! 🌟  
# The **Dutch National Flag Algorithm** is a **must-know** for every beginner — it builds strong intuition for **in-place swaps**, **3-pointer techniques**, and **partition-based sorting**, all in just one pass. Let's break it down **step-by-step with full clarity** and **zero assumptions**.
# ---

# ## ✅ Problem:
# Sort an array that only contains **0s, 1s, and 2s** in ascending order.  
# 🔹 You **cannot use sorting functions**.  
# 🔹 You **must do it in one pass** and **in-place (no extra array)**.

# ---

# ## 🔥 The Idea:

# You use **three pointers**:

# | Pointer | Purpose                          |
# |---------|----------------------------------|
# | `low`   | Boundary where **0s** should go  |
# | `mid`   | Current element being processed  |
# | `high`  | Boundary where **2s** should go  |

# ---

# ## 🛠️ Core Algorithm:

# ```python
def sortColors(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
# ```

# ---

# ## 🧠 Why Not Increment `mid` After Swapping with `high`?

# ### ❓ Let’s say `arr[mid] = 2`:

# We swap `arr[mid]` with `arr[high]` and do:
# ```python
# high -= 1
# ```

# But **we do NOT increment `mid`** immediately.

# ---

# ### 🤔 Why?

# Because the element we just **swapped from the end (arr[high])** is **unknown**.  
# It could be:
# - `0` → needs to go to the left
# - `1` → fine in middle
# - `2` → needs to go back to right again!

# So, we need to **re-check** the new `arr[mid]` after swap. Hence, no `mid += 1`.

# ---

# ### ✔️ On the other hand, when we get a `0`:
# - We swap it to the front
# - Both `low` and `mid` are incremented because:
#   - `low` moves forward (0 is placed correctly)
#   - `mid` also moves forward (current element handled)

# ---

# ## 🧪 Example Walkthrough:

# ```python
# arr = [2, 0, 1]

# Step 0: low=0, mid=0, high=2
# arr[mid]=2 → swap arr[mid] and arr[high]
# arr = [1, 0, 2]
# now high = 1

# Step 1: arr[mid]=1 → mid += 1

# Step 2: arr[mid]=0 → swap arr[low] and arr[mid]
# arr = [0, 1, 2]
# ```

# Final result: `[0, 1, 2]`

# ---

# ## 🧮 Time and Space:

# | Complexity  | Value     |
# |-------------|-----------|
# | Time        | `O(n)`    |
# | Space       | `O(1)`    |

# ---

# ## 🏁 Summary for Beginners:
# - ✅ 3 pointers: `low`, `mid`, `high`
# - ✅ If `0`, send it to the **left**
# - ✅ If `2`, send it to the **right**
# - ✅ If `1`, **leave it**, just move on
# - ✅ **Never increment `mid`** after a swap with `high` — you don't know what value you just swapped in!

# ---

# Let me know if you want this visualized or converted into **C / Java**, or if you want to solve a similar pattern problem yourself 🔁
sortColors([0,1,2,0,1,2])