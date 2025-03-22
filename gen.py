import os
import argparse

def create_folder_structure(course, subjects, labs, current_sem):
    base_path = f"{course}"
    
    # Create base directory for the course and semester
    if current_sem:
        os.makedirs(f"{base_path}/{current_sem}", exist_ok=True)
        
        # Create the main index.md file for the semester
        with open(f"{base_path}/{current_sem}/index.md", "w") as f:
            f.write(f"""---
layout: home

hero:
  name: "{current_sem}"

  actions:
    - theme: brand
      text: Edit Content
      link: https://github.com/examdawn/{course}/tree/contents/{current_sem}
    - theme: alt
      text: Go Back
      link: ..

features:
  - icon: <svg xmlns="http://www.w3.org/2000/svg" height="40px" viewBox="0 -960 960 960" width="40px" fill="#6a5acd"><path d="M186.67-120q-27.5 0-47.09-19.58Q120-159.17 120-186.67v-586.66q0-27.5 19.58-47.09Q159.17-840 186.67-840h192.66q7.67-35.33 35.84-57.67Q443.33-920 480-920t64.83 22.33Q573-875.33 580.67-840h192.66q27.5 0 47.09 19.58Q840-800.83 840-773.33v586.66q0 27.5-19.58 47.09Q800.83-120 773.33-120H186.67Zm0-66.67h586.66v-586.66H186.67v586.66ZM280-280h275.33v-66.67H280V-280Zm0-166.67h400v-66.66H280v66.66Zm0-166.66h400V-680H280v66.67Zm200-181.34q13.67 0 23.5-9.83t9.83-23.5q0-13.67-9.83-23.5t-23.5-9.83q-13.67 0-23.5 9.83t-9.83 23.5q0 13.67 9.83 23.5t23.5 9.83Zm-293.33 608v-586.66Z"/></svg>
    title: Assignments
    details: Click here to view Assignments for {current_sem}
    link: ./assignment
---
""")

    # Create directories and files for each subject
    for subject in subjects:
        os.makedirs(f"{base_path}/{current_sem}/{subject}/assignments", exist_ok=True)
        os.makedirs(f"{base_path}/{current_sem}/{subject}/solved", exist_ok=True)
        os.makedirs(f"{base_path}/{current_sem}/{subject}/notes", exist_ok=True)

        with open(f"{base_path}/{current_sem}/{subject}/index.md", "w") as f:
            f.write(f"""---
order: 0
title: {subject} - Syllabus
---
# {subject}
""")
        
        with open(f"{base_path}/{current_sem}/{subject}/assignments/index.md", "w") as f:
            f.write(f"""---
order: 0
title: {subject} - Assignments
---
# {subject}
## Assignments
""")
        
        with open(f"{base_path}/{current_sem}/{subject}/solved/index.md", "w") as f:
            f.write(f"""---
order: 0
title: {subject} - Solved Questions
---
# {subject}
## Solved Questions
""")
        
        with open(f"{base_path}/{current_sem}/{subject}/notes/index.md", "w") as f:
            f.write(f"""---
order: 0
title: {subject} - Notes
---
# {subject}
## Notes
""")
        
        print(f"Done generating folder and files for subject: {base_path}/{current_sem}/{subject}")

    # Create directories and files for each lab (treated similarly to subjects)
    for lab in labs:
        os.makedirs(f"{base_path}/{current_sem}/{lab}/lab", exist_ok=True)

        with open(f"{base_path}/{current_sem}/{lab}/index.md", "w") as f:
            f.write(f"""---
order: 0
title: {lab} - Syllabus
---
# {lab}
""")
        
        with open(f"{base_path}/{current_sem}/{lab}/lab/index.md", "w") as f:
            f.write(f"""---
order: 0
title: {lab} - Lab Records
---
# {lab}
## Lab Records
""")
        
        print(f"Done generating folder and files for lab: {base_path}/{current_sem}/{lab}")

    # Create a root-level index.md file for the course
    with open(f"{base_path}/index.md", "w") as f:
        f.write(f"""---
layout: home

hero:
  name: "Exam Dawn - {course}"
  tagline: "{course}"

actions:
    - theme: brand
      text: Edit Content
      link: https://github.com/examdawn/{course}
    - theme: alt
      text: Go Back
      link: ../../..

features:
    - title: {current_sem}
      details: Click here to view options for {current_sem}
      link: ./{current_sem}

---

{course} is a comprehensive course designed to teach the fundamentals of Computer Science.

### Content Contributors

<a href="https://github.com/examdawn/{course}/graphs/contributors">
<img src="https://contrib.rocks/image?repo=examdawn/{course}" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
""")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate folder structure for subjects and labs.")
    
    parser.add_argument("--course", required=True, help="Course year and name (e.g., '2023_BCA')")
    parser.add_argument("--subjects", nargs="+", help="List of subjects")
    parser.add_argument("--labs", nargs="+", help="List of labs")
    parser.add_argument("--addsem", help="Current semester folder name (e.g., '3rdsem')")
    
    args = parser.parse_args()

    course = args.course
    subjects = args.subjects if args.subjects else []
    labs = args.labs if args.labs else []
    current_sem = args.addsem

    # Combine subjects and labs into a single list since labs are also treated as subjects.
    subjects += labs

    create_folder_structure(course, subjects, labs, current_sem)
