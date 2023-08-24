def intersect_rectangle(R1, R2):
    def is_intersect(R1, R2):
        return (R1.x <= R2.x + R2.width and R1.x + R1.width >= R2.x
                and R1.y <= R2.y + R2.height and R1.y + R1.height >= R2.y)

    if not is_intersect(R1, R2):
        return Rectangle(0, 0, -1, -1)  # No intersection
    return Rectangle(
        max(R1.x, R2.x),
        max(R1.x, R2.y),
        min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x),
        min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y))


# Example rectangles
rectangle1 = Rectangle(2, 3, 6, 4)  # Rectangle with (x=2, y=3, width=6, height=4)
rectangle2 = Rectangle(4, 2, 4, 5)  # Rectangle with (x=4, y=2, width=4, height=5)
rectangle3 = Rectangle(14, 20, 4, 5)

# Calculate the intersection
intersection1 = intersect_rectangle(rectangle1, rectangle2)
intersection2 = intersect_rectangle(rectangle1, rectangle3)

# Print the results
print("Rectangle 1:", rectangle1)
print("Rectangle 2:", rectangle2)
print("Rectangle 3:", rectangle3, "\n")
print("Intersection:", intersection1)
print("Intersection:", intersection2)
