## Installation

Clone and change into the repository. 
```bash
git clone https://github.com/AFKlex/Habit-Tracker.git
cd Habit-Tracker
```

Now install requirements: 
```bash
pip install -r requirements.txt
```

Now run the habit-tracker typing in the virutal python enviorment. 
```bash 
./venv3/bin/python3 main.py
```

## Commands Overview:
### 1. **getHabits**
**Function:** Retrieve and display habits based on the frequency filter.

**Parameters:**
- `-f`, `--frequency` (optional): The filter for frequency of habits. Can be one of the following values:
  - `daily`
  - `weekly`
  - `all` (default)
  
**What Happens:**
- Retrieves and displays a list of habits that match the specified frequency.
- If no frequency is specified, all habits will be returned by default.

```bash
habitShell getHabits --frequency daily
```

---

### 2. **createHabit**
**Function:** Create a new habit.

**Parameters:**
- `-n`, `--name` (required): The name of the new habit.
- `-f`, `--frequency` (required): The frequency of the habit. Can be one of the following:
  - `daily`
  - `weekly`
- `-d`, `--description` (optional): A description for the habit.
- `-s`, `--startdate` (optional): The start date for the habit. Default is today.
- `--customDateFormat` (optional): A custom date format (default is `%Y-%m-%d`).

**What Happens:**
- Adds a new habit to the habit manager with the specified parameters. 
- If a habit with the same name already exists, an error message will be shown.
  
```bash
habitShell createHabit --name "Exercise" --frequency daily --description "Morning workout" --startdate 2025-03-20
```

---

### 3. **changeHabit**
**Function:** Modify an existing habit.

**Parameters:**
- `-n`, `--name` (required): The name of the habit to modify.
- `-f`, `--frequency` (optional): Change the frequency of the habit. Options:
  - `daily`
  - `weekly`
- `-d`, `--description` (optional): Modify the description of the habit.
- `-s`, `--startdate` (optional): Change the start date of the habit.
- `-N`, `--newName` (optional): Change the name of the habit.
- `--customDateFormat` (optional): A custom date format (default is `%Y-%m-%d`).

**What Happens:**
- Updates the specified habit with the new parameters.
- If no changes are made, or if the habit is not found, a message will indicate that no changes were applied.

```bash
habitShell changeHabit --name "Exercise" --frequency weekly --description "Evening workout" --startdate 2025-03-21
```

---

### 4. **deleteHabit**
**Function:** Delete a habit by name.

**Parameters:**
- `-n`, `--name` (required): The name of the habit to delete.

**What Happens:**
- Removes the specified habit from the habit manager.
- If the habit is not found, an error message will appear.

```bash
habitShell deleteHabit --name "Exercise"
```

---

### 5. **deleteAllHabit**
**Function:** Delete all habits from the manager.

**Parameters:**
- No parameters are required.

**What Happens:**
- Clears all stored habits from the habit manager.

```bash
habitShell deleteAllHabit
```

---

### 6. **checkHabit**
**Function:** Mark a habit as completed for a specific date.

**Parameters:**
- `-n`, `--name` (required): The name of the habit to check.
- `-d`, `--date` (optional): The date to mark the habit as completed. Default is today's date.
- `--customDateFormat` (optional): A custom date format (default is `%Y-%m-%d`).

**What Happens:**
- Marks the specified habit as completed for the given date.
  
```bash
habitShell checkHabit --name "Exercise" --date 2025-03-20
```

---

### 7. **deletecheck**
**Function:** Remove a check (completion mark) for a habit on a specific date.

**Parameters:**
- `-n`, `--name` (required): The name of the habit to remove the completion for.
- `-d`, `--date` (optional): The date to remove the completion mark. Default is today's date.
- `--customDateFormat` (optional): A custom date format (default is `%Y-%m-%d`).

**What Happens:**
- Removes the completion mark (check) for the habit on the given date.
  
```bash
habitShell deletecheck --name "Exercise" --date 2025-03-20
```

---

### 8. **getLongestStreak**
**Function:** Retrieve the longest streak for a specific habit.

**Parameters:**
- `-n`, `--name` (optional): The name of the habit to check the longest streak for. If no name is provided, the longest streak for all habits is retrieved.

**What Happens:**
- Displays the longest completion streak for the specified habit.

```bash
habitShell getLongestStreak --name "Exercise"
```

---

