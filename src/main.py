from full_converter import extract_title, markdown_to_html_node
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

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as file:
        markdown = file.read()
        file.close()
    with open(template_path, 'r') as file:
        template = file.read()
        file.close()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    with open(dest_path, 'w') as f:
        f.write(html)
        f.close()

def main():
    copy(os.path.abspath("static"), os.path.abspath("public"))
    generate_page(os.path.abspath("content/index.md"), os.path.abspath("template.html"), os.path.abspath("public/index.html"))

if __name__ == "__main__":
    main()