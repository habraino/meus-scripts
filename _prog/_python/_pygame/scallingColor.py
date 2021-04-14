def scale_color(color, scale):
    r, g, b = color
    r = int(r*scale)
    g = int(g*scale)
    b = int(b*scale)

    return r, g, b

color = (123, 34, 56)
print(color)
print(scale_color(color, 2.))
