#  Pysec Essential

## 1. Project Title
**Pysec Essential** — A first-year academic Python project for **CSE1021: Introduction to Computer Problem Solving and Programming**.

## 2. Project Description
This is a single-file, console-based Python application that implements four small, educational cybersecurity-themed tools: a password strength checker, a Caesar cipher encrypt/decrypt tool, a file integrity checker, and a prime-based key generator. It is written as a menu-driven procedural program using only the Python standard library.

## 3. Objective
To apply core CSE1021 (Units 1–5) programming concepts — top-down design, control flow, functions, basic algorithms, and lists/dictionaries — to build a small, understandable, and testable console project, while demonstrating each concept clearly enough to explain in a viva.

## 4. Features
1. **Password Strength Checker** - checks length, uppercase, lowercase, digit and symbol, and reports Weak / Medium / Strong.
2. **Password Generator** - creates secure passwords satisfying length, case, digit, and symbol rules. 
3. **Caesar Cipher Encrypt/Decrypt Tool** - shifts letters using `ord()`/`chr()` and modulo 26, preserving case and leaving spaces/digits/punctuation unchanged.
4. **File Integrity Checker** - generates a SHA-256 hash of a file and compares it against a previously recorded reference hash.
5. **Prime-based Key Generator** - generates two small primes, computes their GCD, mixes in a pseudo-random value, and produces a simple educational numeric "key."
6. **Exit** - closes the program.



## 5. Technologies Used
- **Language:** Python 3
- **Standard library modules only:** `hashlib`, `random`
- No third-party packages, no frameworks, no databases, no GUI

## 6. Project Structure
```
Pysec-Essential/
├── main.py
└── README.md
```

## 7. How the Program Works
The program is procedural and menu-driven. `main()` runs a `while True` loop that displays the menu, reads the user's choice, and routes to the matching function using `if/elif/else`. Choosing Exit prints a goodbye message and uses `break` to leave the loop. An invalid menu choice prints an error message and simply loops back to the menu, without crashing.

**Simplified pseudocode overview:**

```
1. Password Strength Checker:
   read password
   for each character: update Boolean flags (upper/lower/digit/symbol)
   count satisfied checks (including length)
   if all 5 satisfied -> Strong
   elif 3 or 4 satisfied -> Medium
   else -> Weak

2. Password Generator: 
    read length (minimum 7)
    pick 1 random character from each set: lowercase, uppercase, digits, symbols
    fill remaining (length - 4) characters using random choices from all sets combined
    shuffle character list to randomize order
    join list into a string and display result

3. Caesar Cipher:
   read message, shift, and encrypt/decrypt choice
   for each character:
       if letter: convert to number (ord), shift by +-shift, mod 26, convert back (chr), keep case
       else: leave character unchanged

4. File Hash:
   Generate: read file path -> read file bytes -> SHA-256 hash -> display
   Compare: read file path -> compute current hash -> read reference hash -> if/else compare -> report unchanged/changed

5. Prime-based Key Generator:
   generate prime1, generate prime2 (distinct)
   compute GCD(prime1, prime2)
   generate a pseudo-random value
   compute educational_key = (prime1 * prime2 + random_value) mod 1000
   display all intermediate values

6. Main Menu:
   while True:
       show menu
       read choice
       if/elif choice -> call matching feature
       elif choice is Exit -> break
       else -> show invalid-choice message
```


## 8. How to Run
1. Make sure Python 3 is installed (no extra packages needed).
2. Open a terminal in the project folder.
3. Run:
   ```
   python3 main.py
   ```
4. Choose an option (1–6) from the menu and follow the on-screen prompts.
5. Choose option 6 to exit at any time.

## 9. Sample Usage / Expected Output

**Password Strength Checker**
```
Enter a password to check: Hello123!

Password Strength Analysis
Length (>=7): Yes
Uppercase: Yes
Lowercase: Yes
Digit: Yes
Symbol: Yes
Strength: Strong
```

**Password Generator**
```
Enter desired password length (minimum 7): 12

Generated Password: K9#mP2$xL1!q
Strength Rating: Strong (Passes all 5 criteria)
```

**Caesar Cipher**
```
Choose an option (1 or 2): 1
Enter the message: HELLO
Enter the shift value (whole number): 3
Encrypted message: KHOOR
```

**File Integrity Checker**
```
Choose an option (1-3): 1
Enter the file path: testfile.txt
SHA-256 Hash: 7d7d6f07a3e81aea62c51a088a944795d6e89e6c3342d5509de6e1ea13f7c055
```

**Prime-based Key Generator**
```
Prime 1: 17
Prime 2: 43
GCD of Prime 1 and Prime 2: 1
Pseudo-random value: 60
Educational Key: 791
(This key is for learning purposes only and is not cryptographically secure.)
```


## 10. Test Cases

| # | Test | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| 1 | Weak password | `password` | Weak | Weak | PASS |
| 2 | Strong password | `Cyber@2532` | Strong | Strong | PASS |
| 3 | Medium password | `cyber2532` | Medium | Medium | PASS |
| 4 | Standard length password | 12 | Generates a 12-character password passing all 5 strength criteria | 12-char password containing upper, lower, digit, and symbol; passes Feature 1 check | PASS | 
| 5 | Minimum length enforcement | 7 | Notice displayed; length clamped to minimum of 7 | "Notice: Setting length to default minimum of 7 characters.", 7-char password generated | PASS |
| 6 | Invalid numeric input | abc | Error message; fallback to default length of 12 | "Invalid input! Setting default length to 12 characters.", 12-char password generated | PASS | 
| 7 | Caesar encryption | `ATTACK`, shift 3 | `DWWDFN` | `DWWDFN` | PASS |
| 8 | Caesar decryption | `DWWDFN`, shift 3 | `ATTACK` | `ATTACK` | PASS |
| 10 | File hash generation | sample text file | valid SHA-256 hash | hash generated, matched independent `hashlib` computation | PASS |
| 11 | Hash comparison — unchanged file | same file + matching hash | "unchanged" | "The file contents appear unchanged." | PASS |
| 12  | Hash comparison — changed file | modified file + old hash | "may have changed" | "Hash mismatch: The file contents may have changed." | PASS |
| 13 | Missing file | non-existent path | error, no crash | "Error: File not found or could not be read." | PASS |
| 14 | Prime key generator (5 runs) | menu option 4 | valid distinct primes, correct GCD, correct key formula | verified across 5 runs — all primes genuinely prime, GCD = 1 as expected, key formula matched by hand-calculation | PASS |
| 15 | Invalid menu input | `9` | error message, no crash | "Invalid choice. Please enter a number from 1 to 5." | PASS |
| 16 | Invalid Caesar shift / invalid submenu choice | non-numeric shift, `9` in file menu | error message, no crash | both handled with clear error messages | PASS |
| 17 | Syntax check | `python3 -m py_compile main.py` | no errors | no errors | PASS |
| 18 | Import/load test | dynamic module import | loads cleanly | loaded successfully, all expected functions present | PASS |
| 19 | Syllabus-level AST check | static code analysis | no classes, no recursion, stdlib-only imports | confirmed: 0 classes, 0 recursive functions, only `hashlib` and `random` imported | PASS |


