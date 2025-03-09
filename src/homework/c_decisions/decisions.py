def get_options_ratio(options, total):
    return options / total

def get_faculty_rating(ratio):
    if (ratio >= 0.9 and ratio < 1.0):
        return "Excellent"
    elif (ratio > 0.8):
        return "Very Good"
    elif (ratio > 0.7):
        return "Good"
    elif (ratio > 0.6):
        return "Needs Improvement"
    elif (ratio <= 0.59):
        return "Unacceptable"