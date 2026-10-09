def process_image(image_id):
    """Simulate a CPU-heavy image operation."""
    result = 0
    for i in range(5_000_000):
        result += (i ** 2) / 3.14159
    return result
