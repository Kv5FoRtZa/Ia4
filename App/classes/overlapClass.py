def overlap(sx, sy, L, cx, cy, r):
    h = L / 2

    left   = sx - h
    right  = sx + h
    bottom = sy - h
    top    = sy + h

    closest_x = max(left, min(cx, right))
    closest_y = max(bottom, min(cy, top))

    dx = cx - closest_x
    dy = cy - closest_y

    return dx * dx + dy * dy <= r * r
def square_square_overlap(x1, y1, L1, x2, y2, L2):
    h1 = L1 / 2
    h2 = L2 / 2

    if abs(x1 - x2) > h1 + h2:
        return False
    elif abs(y1 - y2) > h1 + h2:
        return False
    else:
        return True