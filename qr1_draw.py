def draw_qr(canvas, x_left, y_top, size, qr):
    rows = len(qr)

    cols = len(qr[0])

    total_width = size
    total_height = size

    cell_width = total_width / cols
    cell_height = total_height / rows

    for i in range(rows):
        for j in range(cols):
            
            if qr[i][j] == 1:
                color ="Black"
            else:
                color ="White"

            cell_x1 = x_left + j * cell_width
            cell_y1 = y_top + i * cell_height

            cell_x2 = cell_x1 + cell_width
            cell_y2 = cell_y1 + cell_height

            canvas.create_rectangle(cell_x1, cell_y1, cell_x2, cell_y2,
                fill= color, outline = "")



