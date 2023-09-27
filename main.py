import colorgram

rgb_colors = []
colors = colorgram.extract('hirstpntg.jpeg', 30)
for color in colors:
    rgb_colors.append(color.rgb)
print(rgb_colors)




