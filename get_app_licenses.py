import os
import shutil
from argparse import ArgumentParser, Namespace


class Project:
    def __init__(self, name: str, licenseFolder: str) -> None:
        self.name = name
        self.folderPath = licenseFolder


OUTPUT_DIR = "docs/app_licenses"

PROJECTS = [
    Project(
        "driving_license",
        "melos_workspace/apps/driving_license/pkg_workspace/assets/app_licenses",
    )
]


def copy_licenses(project: Project, repo_path: str) -> None:
    destination_folder = os.path.join(OUTPUT_DIR, project.name)
    os.makedirs(destination_folder, exist_ok=True)

    source_folder = os.path.join(repo_path, project.folderPath)
    for file in os.listdir(source_folder):
        shutil.copyfile(
            os.path.join(source_folder, file), os.path.join(destination_folder, file)
        )


def remove_non_existing_projects_from_result_dir():
    for dir in os.listdir(OUTPUT_DIR):
        if not any(dir == project.name for project in PROJECTS):
            shutil.rmtree(os.path.join(OUTPUT_DIR, dir))


def get_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("path", help="Path to the portfolio-projects folder")
    return parser.parse_args()


def main():
    args = get_args()
    remove_non_existing_projects_from_result_dir()

    for project in PROJECTS:
        copy_licenses(project, args.path)


if __name__ == "__main__":
    main()
