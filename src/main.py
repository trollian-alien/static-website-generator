import os, shutil

def wipe_directory_content(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir() and not entry.is_symlink():
                shutil.rmtree(entry.path)
            else:
                os.remove(entry.path)

def copy(source, target): #copies from source directory path to target path
    wipe_directory_content(target)
    changelog = f"{target} content wiped"
    with os.scandir(source) as entries:
        for entry in entries:
            if entry.is_dir() and not entry.is_symlink():
                newdir = f"{target}/{entry.name}"
                os.mkdir(newdir)
                copy(entry, newdir)
                changelog += f"\n directory {entry.name} added to {target}"
            else:
                shutil.copy(entry, target)
                changelog += f"\n file {entry.name} copied to {target}"
    print(changelog)

def main():
    copy(os.path.abspath("static"), os.path.abspath("public"))

if __name__ == "__main__":
    main()