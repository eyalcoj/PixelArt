def get_color(color_number: int, all_colors):
    for i in range(len(all_colors)):
        if color_number == i:
            return all_colors[i]

    return None
