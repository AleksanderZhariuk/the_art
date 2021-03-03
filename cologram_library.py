import colorgram

colors_from_pic = colorgram.extract('image.jpg', 30)
list_with_colors = []

for element in colors_from_pic:
    r = element.rgb.r
    g = element.rgb.g
    b = element.rgb.b
    color = (r, g, b)
    list_with_colors.append(color)

print(list_with_colors)