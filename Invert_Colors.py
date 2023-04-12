def color_invert(rgb):
    opposite_colors = list(rgb)

    for i in range(len(opposite_colors)):
        opposite_colors[i] = 255 - opposite_colors[i]

    return tuple(opposite_colors)

print(color_invert((255, 255, 255)))
