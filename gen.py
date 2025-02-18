import os
import argparse

def create_folder_structure(course, subjects, labs, current_sem):
    base_path = f"{course}"
    if current_sem:
        os.makedirs(f"{base_path}/{current_sem}", exist_ok=True)
        with open(f"{base_path}/{current_sem}/index.md", "w") as f:
            f.write(f"---\nlayout: home\n\nhero:\n  name: \"{current_sem}\"\n\n  actions:\n    - theme: brand\n      text: Edit Content\n      link: https://github.com/examdawn/{course}/tree/contents/{current_sem}\n    - theme: alt\n      text: Go Back\n      link: ..\n\nfeatures:\n  - icon: <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"40px\" viewBox=\"0 -960 960 960\" width=\"40px\" fill=\"#6a5acd\"><path d=\"M186.67-120q-27.5 0-47.09-19.58Q120-159.17 120-186.67v-586.66q0-27.5 19.58-47.09Q159.17-840 186.67-840h192.66q7.67-35.33 35.84-57.67Q443.33-920 480-920t64.83 22.33Q573-875.33 580.67-840h192.66q27.5 0 47.09 19.58Q840-800.83 840-773.33v586.66q0 27.5-19.58 47.09Q800.83-120 773.33-120H186.67Zm0-66.67h586.66v-586.66H186.67v586.66ZM280-280h275.33v-66.67H280V-280Zm0-166.67h400v-66.66H280v66.66Zm0-166.66h400V-680H280v66.67Zm200-181.34q13.67 0 23.5-9.83t9.83-23.5q0-13.67-9.83-23.5t-23.5-9.83q-13.67 0-23.5 9.83t-9.83 23.5q0 13.67 9.83 23.5t23.5 9.83Zm-293.33 608v-586.66 586.66Z\"/></svg>\n    title: Assignments\n    link: ./assignment\n  - icon: <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"40px\" viewBox=\"0 -960 960 960\" width=\"40px\" fill=\"#6a5acd\"><path d=\"M186.67-306.33q12-6.34 25.09-10Q224.84-320 240-320h40v-493.33h-40q-23 0-38.17 15.33-15.16 15.33-15.16 38v453.67ZM240-80q-50 0-85-35t-35-85v-560q0-50 35-85t85-35h286.67v66.67h-180V-320H600v-126.67h66.67v193.34H240q-22.67 0-38 15.33-15.33 15.33-15.33 38T202-162q15.33 15.33 38 15.33h533.33v-340H840V-80H240Zm-53.33-226.33V-813.33v507ZM700-486.67q0-89.21 62.06-151.27Q824.12-700 913.33-700q-89.21 0-151.27-62.06Q700-824.12 700-913.33q0 89.21-62.06 151.27Q575.88-700 486.67-700q89.21 0 151.27 62.06Q700-575.88 700-486.67Z\"/></svg>\n    title: Solved Questions\n    link: ./solved\n  - icon: <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"40px\" viewBox=\"0 -960 960 960\" width=\"40px\" fill=\"#6a5acd\"><path d=\"M448-259.33v-416q-43.67-28-94.08-43t-101.92-15q-37.33 0-73.5 8.66Q142.33-716 106.67-702v421.33Q139-294 176.83-300.33q37.84-6.34 75.17-6.34 51.38 0 100.02 11.84Q400.67-283 448-259.33ZM481.33-160q-50-38-108.66-58.67Q314-239.33 252-239.33q-38.36 0-75.35 9.66-36.98 9.67-72.65 25-22.4 11-43.2-2.33Q40-220.33 40-245.33v-469.34q0-13.66 6.5-25.33Q53-751.67 66-758q43.33-21.33 90.26-31.67Q203.19-800 252-800q74.67 0 129 18.67 54.33 18.66 114.33 55.66 9 5.34 14.17 13.67t5.17 20v432.67q48-23.67 94.83-35.5 46.83-11.84 98.5-11.84 37.33 0 75.83 6t69.5 16.67v-491q10.23 3.43 20.12 7.55 9.88 4.12 19.88 9.45 13 6.33 19.84 18 6.83 11.67 6.83 25.33v469.34q0 26.26-21.5 39.96t-43.17.7q-35-16-71.98-25.33-36.99-9.33-75.35-9.33-62 0-119.33 21-57.34 21-107.34 58.33Zm133.34-231.33v-442L753.33-880v443.33l-138.66 45.34Zm-337.34-105Z\"/></svg>\n    title: Lab Records\n    link: ./lab\n  - icon: <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"40px\" viewBox=\"0 -960 960 960\" width=\"40px\" fill=\"#6a5acd\"><path d=\"M448-259.33v-416q-43.67-28-94.08-43t-101.92-15q-37.33 0-73.5 8.66Q142.33-716 106.67-702v421.33Q139-294 176.83-300.33q37.84-6.34 75.17-6.34 51.38 0 100.02 11.84Q400.67-283 448-259.33ZM481.33-160q-50-38-108.66-58.67Q314-239.33 252-239.33q-38.36 0-75.35 9.66-36.98 9.67-72.65 25-22.4 11-43.2-2.33Q40-220.33 40-245.33v-469.34q0-13.66 6.5-25.33Q53-751.67 66-758q43.33-21.33 90.26-31.67Q203.19-800 252-800q74.67 0 129 18.67 54.33 18.66 114.33 55.66 9 5.34 14.17 13.67t5.17 20v432.67q48-23.67 94.83-35.5 46.83-11.84 98.5-11.84 37.33 0 75.83 6t69.5 16.67v-491q10.23 3.43 20.12 7.55 9.88 4.12 19.88 9.45 13 6.33 19.84 18 6.83 11.67 6.83 25.33v469.34q0 26.26-21.5 39.96t-43.17.7q-35-16-71.98-25.33-36.99-9.33-75.35-9.33-62 0-119.33 21-57.34 21-107.34 58.33Zm133.34-231.33v-442L753.33-880v443.33l-138.66 45.34Zm-337.34-105Z\"/></svg>\n    title: Notes From Faculty\n    link: ./notes\n---\n")

    for subject in subjects:
        os.makedirs(f"{base_path}/{current_sem}/{subject}/assignments", exist_ok=True)
        os.makedirs(f"{base_path}/{current_sem}/{subject}/solved", exist_ok=True)
        # os.makedirs(f"{base_path}/{current_sem}/{subject}/notes", exist_ok=True)
        with open(f"{base_path}/{current_sem}/{subject}/index.md", "w") as f:
            f.write(f"---\norder: 0\ntitle: {subject} - Syllabus\n---\n# {subject}\n")
        with open(f"{base_path}/{current_sem}/{subject}/assignments/index.md", "w") as f:
            f.write(f"---\norder: 0\ntitle: {subject} - Assignments\n---\n# {subject}\n## Assignments\n")
        with open(f"{base_path}/{current_sem}/{subject}/solved/index.md", "w") as f:
            f.write(f"---\norder: 0\ntitle: {subject} - Solved Questions\n---\n# {subject}\n## Solved Questions\n")
        with open(f"{base_path}/{current_sem}/{subject}/notes.md", "w") as f:
            f.write(f"---\norder: 0\ntitle: {subject} - Notes\n---\n# {subject}\n## Notes\n")
        print(f"Done generating folder: {base_path}/{current_sem}/{subject}")

    for lab in labs:
        os.makedirs(f"{base_path}/{current_sem}/{lab}/lab", exist_ok=True)
        with open(f"{base_path}/{current_sem}/{lab}/index.md", "w") as f:
            f.write(f"---\norder: 0\ntitle: {lab} - Syllabus\n---\n# {lab}\n")
        with open(f"{base_path}/{current_sem}/{lab}/lab/index.md", "w") as f:
            f.write(f"---\norder: 0\ntitle: {lab} - Lab Records\n---\n# {subject}\n## Lab Records\n")

    # Create root level index.md
    with open(f"{base_path}/index.md", "w") as f:
        f.write(f"---\n# https://vitepress.dev/reference/default-theme-home-page\nlayout: home\n\nhero:\n  name: \"Exam Dawn - {course}\"\n  text: \"An All-in-One Resource Site for {course} Students\"\n  actions:\n    - theme: brand\n      text: Edit Content\n      link: https://github.com/examdawn/{course}\n    - theme: alt\n      text: Go Back\n      link: ../../..\n\nfeatures:\n  - title: {current_sem}\n    link: ./{current_sem}\n---\n\n{course} is a 3 years Undergraduate course which teaches the extremely fundamental basics of Computer Science\n\nOngoing: {current_sem}\n\n### Content Contributors\n<a href=\"https://github.com/examdawn/{course}/graphs/contributors\">\n  <img src=\"https://contrib.rocks/image?repo=examdawn/{course}\" />\n</a>\n\nMade with [contrib.rocks](https://contrib.rocks).\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate folder structure for subjects and labs.")
    parser.add_argument("--course", required=True, help="Course year and name (e.g., 2023_BCA)")
    parser.add_argument("--subjects", nargs="+", help="List of subjects")
    parser.add_argument("--labs", nargs="+", help="List of labs")
    parser.add_argument("--addsem", help="Current semester folder name (e.g., 3rdsem)")
    args = parser.parse_args()

    course = args.course
    subjects = args.subjects if args.subjects else []
    labs = args.labs if args.labs else []
    current_sem = args.addsem

    subjects+=labs # Lab subjects are normal subjects too!

    create_folder_structure(course, subjects, labs, current_sem)
