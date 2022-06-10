def pos_to_index(pos,width,grid):
    if pos == width:
        return(-1)
    return (pos//grid)
