from textnode import TextNode, TextType
import os
import shutil
import re
from markdown_blocks import markdown_to_html_node
from inline_markdown import extract_title

def generate_page(from_path, template_path, dest_path):
    print (f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f: filecontent = f.read()
    with open(template_path) as f: templatecontent = f.read()
    nodes = markdown_to_html_node(filecontent)
    htmlstring = nodes.to_html()
    title =  extract_title(filecontent)

    templatecontent = templatecontent.replace("{{ Title }}", title)
    templatecontent = templatecontent.replace("{{ Content }}", htmlstring)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(templatecontent)

def copy_static_to_public(source, dest):
    #delete all content
    
    if os.path.exists(dest):
        shutil.rmtree(dest)
        os.mkdir(dest)
    shutil.copytree(source,dest, dirs_exist_ok=True)

def main():
    source = "/home/sebo/Dokumente/dev/staticsite/static"
    dest = "/home/sebo/Dokumente/dev/staticsite/public"
    copy_static_to_public(source, dest)
    source = "/home/sebo/Dokumente/dev/staticsite/content/index.md"
    template = "/home/sebo/Dokumente/dev/staticsite/template.html"
    dest = "/home/sebo/Dokumente/dev/staticsite/public/index.html"
    generate_page(source, template, dest)


main()
