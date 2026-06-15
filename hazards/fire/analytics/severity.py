def calculate_severity(fire_area, smoke_area, persistence, object_count):
    score = (fire_area * 0.5) + (smoke_area * 0.2) + (persistence * 0.1) + (object_count * 0.2)
    return min(1.0, score)
