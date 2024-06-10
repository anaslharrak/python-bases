languages = ["Python", "Java", "C#", "JavaScript"]

languages.insert(3, "PHP")
languages.insert(0, "C++")
languages.remove("Java")
print("Java" in languages)
print("PHP" in languages)
# languages.clear()


print(len(languages))