def format_car_id(car_id):
        persian_marker = "\u200F"  # Right-to-Left Marker
        latin_marker = "\u200E"    # Left-to-Right Marker

        formatted_id = ""
        for char in car_id:
            if '\u0600' <= char <= '\u06FF':  # Persian character range
                formatted_id += persian_marker + char
            else:
                formatted_id += latin_marker + char

        return formatted_id

def remove_format_car_id(car_id):
     return car_id.replace('\u200E', "").replace('\u200F', '')