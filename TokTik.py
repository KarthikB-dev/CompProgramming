n = int(input())
views = {}
max_views = 0
most_viewed = ""

for __ in range(n):
    line = input().split()
    name = line[0] 
    view_count = int(line[1])
    if name in views:
        views[name] += view_count
    else:
        views[name] = view_count

    if views[name] > max_views:
        max_views = views[name]
        most_viewed = name

print(most_viewed)
