from mongoengine import connect
from models import Authors, Quotes

connect(host='mongodb+srv://user599:qwerty123@cluster0.vprpbbg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

def find_by_author(name):
    author = Authors.objects(fullname=name).first()
    if author:
        quotes = Quotes.objects(author=author)
        print(f"Quotes author {name}:")
        for quote in quotes:
            print(f"- {quote.quote}")
    else:
        print(f"Author {name} no find.")

def find_by_tag(tag):
    quotes = Quotes.objects(tags=tag)
    if quotes:
        print(f"Quotes with tag '{tag}':")
        for quote in quotes:
            print(f"- {quote.quote}")
    else:
        print(f"Quotes with tag '{tag}' no find.")

def find_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quotes.objects(tags__in=tags_list)
    if quotes:
        print(f"Quotes with tags '{', '.join(tags_list)}':")
        for quote in quotes:
            print(f"- {quote.quote}")
    else:
        print(f"Quotes with tags '{', '.join(tags_list)}' no find.")

while True:
    command = input("Enter command (name: <name author>, tag: <tag>, tags: <tags>, exit with exit): ").strip()

    if command.startswith("name:"):
        name = command.split(":")[1].strip()
        find_by_author(name)
    elif command.startswith("tag:"):
        tag = command.split(":")[1].strip()
        find_by_tag(tag)
    elif command.startswith("tags:"):
        tags = command.split(":")[1].strip()
        find_by_tags(tags)
    elif command == "exit":
        print("Exit")
        break
    else:
        print("Unknown command")
