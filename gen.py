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

features:  - icon: <svg xmlns="http://www.w3.org/2000/svg" height="40px" viewBox="0 -960 960 960" width="40px" fill="#6a5acd"><path d="M186.67-120q-27.5 0-47.09-19.58Q120-159.17 120-186.67v-586.66q0-27.5 19.58-47.09Q159.17-840 186.67-840h192.66q7.67-35.33 35.84-57.67Q443.33-920 480-920t64.83 22.33Q573-875.33 580.67-840h192.66q27.5 0 47.09 19.58Q840-800.83 840-773.33v586.66q0 27.5-19.58 47.09Q800.83-120 773.33-120H186.67Zm0-66.67h586.66v-586.66H186.67v586.66ZM280-280h275.33v-66.67H280V-280Zm0-166.67h400v-66.66H280v66.66Zm0-166.66h400V-680H280v66.67Zm200-181.34q13.67 0 23.5-9.83t9.83-23.5q0-13.67-9.83-23.5t-23.5-9.83q-13.67 0-23.5 9.83t-9.83 23.5q0 13.67 9.83 23.5t23.5 9.83Zm-293.33 608v-586.66 586.66Z"/></svg>
    title: Assignments
    details: Click here to view Assignments for {current_sem}
    link: ./assignment
  - icon: <svg xmlns="http://www.w3.org/2000/svg" height="40px" viewBox="0 -960 960 960" width="40px" fill="#6a5acd"><path d="M186.67-306.33q12-6.34 25.09-10Q224.84-320 240-320h40v-493.33h-40q-23 0-38.17 15.33-15.16 15.33-15.16 38v453.67ZM240-80q-50 0-85-35t-35-85v-560q0-50 35-85t85-35h286.67v66.67h-180V-320H600v-126.67h66.67v193.34H240q-22.67 0-38 15.33-15.33 15.33-15.33 38T202-162q15.33 15.33 38 15.33h533.33v-340H840V-80H240Zm-53.33-226.33V-813.33v507ZM700-486.67q0-89.21 62.06-151.27Q824.12-700 913.33-700q-89.21 0-151.27-62.06Q700-824.12 700-913.33q0 89.21-62.06 151.27Q575.88-700 486.67-700q89.21 0 151.27 62.06Q700-575.88 700-486.67Z"/></svg>
    title: Solved Questions
    details: Click here to view Solved Questions for {current_sem}
    link: ./solved
  - icon: <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#6a5acd"><path d="M80-40v-80h800v80H80Zm80-120v-240q-33-54-51-114.5T91-638q0-61 15.5-120T143-874q8-21 26-33.5t40-12.5q31 0 53 21t18 50l-11 91q-6 48 8.5 91t43.5 75.5q29 32.5 70 52t89 19.5q60 0 120.5 12.5T706-472q45 23 69.5 58.5T800-326v166H160Zm80-80h480v-86q0-24-12-42.5T674-398q-41-20-95-31t-99-11q-66 0-122.5-27t-96-72.5Q222-585 202-644.5T190-768q-10 30-14.5 64t-4.5 66q0 58 20.5 111.5T240-422v182Zm240-320q-66 0-113-47t-47-113q0-66 47-113t113-47q66 0 113 47t47 113q0 66-47 113t-113 47Zm0-80q33 0 56.5-23.5T560-720q0-33-23.5-56.5T480-800q-33 0-56.5 23.5T400-720q0 33 23.5 56.5T480-640ZM320-160v-37q0-67 46.5-115T480-360h160v80H480q-34 0-57 24.5T400-197v37h-80Zm160-80Zm0-480Z"/></svg>
    title: '"Exam Preparation" Questions'
    details: Click here to view Faculty-Shared Solved Questions for {current_sem}
    link: ./exam-preparation
  - icon: <svg xmlns="http://www.w3.org/2000/svg" height="40px" viewBox="0 -960 960 960" width="40px" fill="#6a5acd"><path d="M448-259.33v-416q-43.67-28-94.08-43t-101.92-15q-37.33 0-73.5 8.66Q142.33-716 106.67-702v421.33Q139-294 176.83-300.33q37.84-6.34 75.17-6.34 51.38 0 100.02 11.84Q400.67-283 448-259.33ZM481.33-160q-50-38-108.66-58.67Q314-239.33 252-239.33q-38.36 0-75.35 9.66-36.98 9.67-72.65 25-22.4 11-43.2-2.33Q40-220.33 40-245.33v-469.34q0-13.66 6.5-25.33Q53-751.67 66-758q43.33-21.33 90.26-31.67Q203.19-800 252-800q74.67 0 129 18.67 54.33 18.66 114.33 55.66 9 5.34 14.17 13.67t5.17 20v432.67q48-23.67 94.83-35.5 46.83-11.84 98.5-11.84 37.33 0 75.83 6t69.5 16.67v-491q10.23 3.43 20.12 7.55 9.88 4.12 19.88 9.45 13 6.33 19.84 18 6.83 11.67 6.83 25.33v469.34q0 26.26-21.5 39.96t-43.17.7q-35-16-71.98-25.33-36.99-9.33-75.35-9.33-62 0-119.33 21-57.34 21-107.34 58.33Zm133.34-231.33v-442L753.33-880v443.33l-138.66 45.34Zm-337.34-105Z"/></svg>
    title: Lab Records
    details: Click here to view Lab Records for {current_sem} 
    link: ./lab
  - icon: <svg xmlns="http://www.w3.org/2000/svg" height="40px" viewBox="0 -960 960 960" width="40px" fill="#6a5acd"><path d="M680-326.67q-50 0-85-35t-35-85q0-50 35-85t85-35q50 0 85 35t35 85q0 50-35 85t-85 35Zm0-66.66q22.67 0 38-15.34 15.33-15.33 15.33-38 0-22.66-15.33-38Q702.67-500 680-500t-38 15.33q-15.33 15.34-15.33 38 0 22.67 15.33 38 15.33 15.34 38 15.34ZM440-46.67v-116q0-21 10-39.5t28-29.5q29.33-17.66 61.17-30.16 31.83-12.5 65.5-19.84L680-186l75.33-95.67q33.67 7.34 65 19.84 31.34 12.5 60.67 30.16 18 11 28.5 29.5t10.5 39.5v116H440Zm66.33-66.66H652L579.33-206q-19.33 7-37.66 16-18.34 9-35.34 19.33v57.34Zm201.67 0h145.33v-57.34q-16.66-10.66-34.66-19.5-18-8.83-37.34-15.83L708-113.33Zm-56 0Zm56 0ZM186.67-120q-27.5 0-47.09-19.58Q120-159.17 120-186.67v-586.66q0-27.5 19.58-47.09Q159.17-840 186.67-840h586.66q27.5 0 47.09 19.58Q840-800.83 840-773.33V-542q-12.67-20-29-37.33-16.33-17.34-37.67-28v-166H186.67v586.66h188.66q-1 6-1.5 12t-.5 12V-120H186.67ZM280-613.33h320.67q18-10 38.22-15 20.23-5 41.11-5V-680H280v66.67Zm0 166.66h213.33q0-17 3.17-34t9.17-32.66H280v66.66ZM280-280h151.33q15-11.67 31.84-19.67 16.83-8 34.5-15.33v-31.67H280V-280Zm-93.33 93.33v-586.66 165.66-25.66V-186.67Zm493.33-260Z"/></svg>
    title: Notes
    details: Click here to view Notes for {current_sem} 
    link: ./notes
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
        with open(f"{base_path}/{current_sem}/{subject}/examprep/index.md", "w") as f:
            f.write(f"""---
order: 0
title: {subject} - "Exam Preparation" Questions
---
# {subject}
## Faculty-Shared Solved Questions
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
