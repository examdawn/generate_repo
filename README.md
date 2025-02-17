# Folder Structure Generation Script

This repository contains a script `generate_structure.py` that generates a generic folder structure when provided with a list of subjects and labs. 

## Usage

To use the script, follow the instructions below:

1. Ensure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory where `generate_structure.py` is located.
4. Run the script with the following command:

```sh
python generate_structure.py --course <your_course> --subjects <subject1> <subject2> ... --labs <lab1> <lab2> ...
```

### Example

To generate a folder structure for subjects "Math" and "Science" and labs "PhysicsLab" and "ChemistryLab", use the following command:

```sh
python generate_structure.py --course NEP2020_2023_BCA --subjects Sub1 Sub2 --labs Sub1 Sub3
```

### Folder Structure

The script will create the following folder structure for each subject and lab:

```
<subject>
├── assignments
│   └── index.md
├── solved
│   └── index.md
├── notes.md
│
└── index.md

<lab>
├── lab
│   └── index.md
├── assignments
│   └── index.md
├── solved
│   └── index.md
├── notes.md
│
└── index.md
```

### Placeholders

The script places placeholders in the `index.md` files to maintain consistency and ensure the frontmatter is understandable.

## Frontmatter

The frontmatter in the generated files is as follows:

- `index.md`:

```markdown
---
order: 0
title: <Subject> - Syllabus
---
# <Subject>
```

- `assignments/index.md`:

```markdown
---
order: 0
title: <Subject> - Assignments
---
# Assignments - <Subject>
```

- `solved/index.md`:

```markdown
---
order: 0
title: <Subject> - Solved Questions
---
# Solved Questions - <Subject>
```

- `notes/index.md`:

```markdown
---
order: 0
title: <Subject> - Notes
---
# Notes - <Subject>
```

- `lab/index.md` (for labs):

```markdown
---
order: 0
title: <Lab> - Lab Records
---
# Lab Records - <Lab>
```
