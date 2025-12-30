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

    return dx*dx + dy*dy <= r*r