def pos_to_index(pos,width,grid):
    if pos == width:
        return(pos//grid-1)
    return (pos//grid)
