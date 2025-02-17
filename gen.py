import os
import argparse

def create_folder_structure(course, subjects, labs):
    base_path = f"{course}"
    for subject in subjects:
        os.makedirs(f"{base_path}/{subject}/assignments", exist_ok=True)
        os.makedirs(f"{base_path}/{subject}/solved", exist_ok=True)
        os.makedirs(f"{base_path}/{subject}/notes", exist_ok=True)
        with open(f"{base_path}/{subject}/index.md", "w") as f:
            f.write(f"---\norder: 0\ntitle: {subject} - Syllabus\n---\n# {subject}\n")
        with open(f"{base_path}/{subject}/assignments/index.md", "w") as f:
            f.write(f"---\norder: 0\ntitle: {subject} - Assignments\n---\n# Assignments - {subject}\n")
        with open(f"{base_path}/{subject}/solved/index.md", "w") as f:
            f.write(f"---\norder: 0\ntitle: {subject} - Solved Questions\n---\n# Solved Questions - {subject}\n")
        with open(f"{base_path}/{subject}/notes/index.md", "w") as f:
            f.write(f"---\norder: 0\ntitle: {subject} - Notes\n---\n# Notes - {subject}\n")

    for lab in labs:
        os.makedirs(f"{base_path}/{lab}/lab", exist_ok=True)
        with open(f"{base_path}/{lab}/index.md", "w") as f:
            f.write(f"---\norder: 0\ntitle: {lab} - Syllabus\n---\n# {lab}\n")
        with open(f"{base_path}/{lab}/lab/index.md", "w") as f:
            f.write(f"---\norder: 0\ntitle: {lab} - Lab Records\n---\n# Lab Records - {lab}\n")
        with open(f"{base_path}/{lab}/assignments/index.md", "w") as f:
            f.write(f"---\norder: 0\ntitle: {lab} - Assignments\n---\n# Assignments - {lab}\n")
        with open(f"{base_path}/{lab}/solved/index.md", "w") as f:
            f.write(f"---\norder: 0\ntitle: {lab} - Solved Questions\n---\n# Solved Questions - {lab}\n")
        with open(f"{base_path}/{lab}/notes/index.md", "w") as f:
            f.write(f"---\norder: 0\ntitle: {lab} - Notes\n---\n# Notes - {lab}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate folder structure for subjects and labs.")
    parser.add_argument("--course", required=True, help="Course year and name (e.g., 2023_BCA)")
    parser.add_argument("--subjects", nargs="+", help="List of subjects")
    parser.add_argument("--labs", nargs="+", help="List of labs")
    args = parser.parse_args()

    course = args.course
    subjects = args.subjects if args.subjects else []
    labs = args.labs if args.labs else []

    create_folder_structure(course, subjects, labs)
