from textnode import TextNode, TextType
import os
import shutil
import re
import sys
from markdown_blocks import markdown_to_html_node
from inline_markdown import extract_title
from pathlib import Path

def generate_page(from_path, template_path, dest_path, basepath):
    print (f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f: filecontent = f.read()
    with open(template_path) as f: templatecontent = f.read()
    nodes = markdown_to_html_node(filecontent)
    htmlstring = nodes.to_html()
    title =  extract_title(filecontent)

    templatecontent = templatecontent.replace("{{ Title }}", title)
    templatecontent = templatecontent.replace("{{ Content }}", htmlstring)

    templatecontent = templatecontent.replace("href=\"/", f"href=\"{basepath}")
    templatecontent = templatecontent.replace("src=\"/", f"src=\"{basepath}")

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(templatecontent)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if os.path.isdir(dir_path_content):
        contents = os.listdir(dir_path_content)
        for content in contents:
            new_dir_path_content = os.path.join(dir_path_content, content)
            generate_pages_recursive(new_dir_path_content, template_path, dest_dir_path, basepath)
    else:
        destfilename = dir_path_content.replace("content", "docs")
        destfilename = destfilename.replace(".md", ".html")
        generate_page(dir_path_content,template_path, destfilename, basepath)

def copy_static_to_public(source, dest):
    #delete all content
    
    if os.path.exists(dest):
        shutil.rmtree(dest)
        os.mkdir(dest)
    shutil.copytree(source,dest, dirs_exist_ok=True)

def main():
    basepath = "/"
    if sys.argv[1] != None and sys.argv[1] != "":
        basepath = sys.argv[1] 


    source = "/home/sebo/Dokumente/dev/staticsite/static"
    dest = "/home/sebo/Dokumente/dev/staticsite/docs"
    copy_static_to_public(source, dest)
    source = "/home/sebo/Dokumente/dev/staticsite/content/"
    template = "/home/sebo/Dokumente/dev/staticsite/template.html"
    dest = "/home/sebo/Dokumente/dev/staticsite/docs/"
    generate_pages_recursive(source, template, dest, basepath)


main()
