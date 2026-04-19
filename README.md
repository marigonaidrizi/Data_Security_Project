# Data Security Project — Cipher Console

Desktop GUI tool that demonstrates two classical ciphers:

- **Running Key Cipher**
- **Double Transposition Cipher**

The previous CLI menu has been replaced with a dark, cyber-themed
CustomTkinter interface.

## Requirements

- Python 3.10+
- See `requirements.txt`

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

`main.py` launches the GUI directly — there is no terminal menu anymore.

## How to use

1. Pick a cipher in the left sidebar (always visible).
2. Type the **key** in the Key panel. Helper text shows the constraints
   for the active cipher.
3. Paste your text into the **Input Text** panel.
4. Click **Encrypt** or **Decrypt**. The result appears in the
   **Output Text** panel.
5. **Swap** moves the output back into the input (handy for round-trip
   tests). **Clear** resets all fields. The output panel has its own
   **Copy Text** button.
6. Validation messages and operation feedback appear in the **Status**
   panel in the lower part of the sidebar.

## Cipher behaviour

Both ciphers normalise input the same way the original CLI did:

- spaces are removed
- everything is uppercased
- only A–Z letters are kept

### Running Key
- A=0 … Z=25
- Encrypt: `C = (P + K) mod 26`
- Decrypt: `P = (C − K + 26) mod 26`
- The key must be at least as long as the processed text.

### Double Transposition
- Text is laid out into a matrix with one column per key character.
- Missing cells are padded with `X`.
- Columns are read in the order obtained by sorting the key.
- The whole process is performed twice.

## Project structure

```
project_root/
├─ main.py                  # GUI entry point
├─ requirements.txt
├─ README.md
│
├─ app/                     # GUI layer
│  ├─ __init__.py
│  ├─ launcher.py
│  ├─ main_window.py
│  ├─ layout.py
│  ├─ styles.py
│  └─ widgets.py
│
├─ ciphers/                 # Cipher implementations
│  ├─ __init__.py
│  ├─ running_key.py
│  └─ double_transposition.py
│
└─ utils/                   # Shared helpers
   ├─ __init__.py
   ├─ validators.py
   └─ text_utils.py
```

## Examples

| Cipher                         | Input         | Key                   | Result             |
|--------------------------------|---------------|-----------------------|--------------------|
| Running Key — Encrypt          | `HELLOWORLD`  | `siguriateknologjise` | `ZMRFFEOKPN`       |
| Running Key — Decrypt          | `ZMRFFEOKPN`  | `siguriateknologjise` | `HELLOWORLD`       |
| Double Transposition — Encrypt | `PERSHENDETJE`| `siguriatedhenave`    | `RDEEHXTXXXPENJES` |
| Double Transposition — Decrypt | `RDEEHXTXXXPENJES` | `siguriatedhenave`| `PERSHENDETJEXXXX` |

> Trailing `X` characters in the decrypted output come from the padding
> the encryption step adds to fill the matrix.
