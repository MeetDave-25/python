movies = ["avengers", "avengers2", "avengers3","avengers4","avengers5"]

print("before :- ")
for i in movies:
    print(i)
print("\n")


movies.pop(-1)
movies.remove("avengers2")

movies.append("avengers6")
movies.insert(4,"mario")

print("after :- ")
for i in movies:
    print(i)
