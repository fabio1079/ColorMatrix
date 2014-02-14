class Block:
  def __init__(self, px, py, tp):
    self.px = px
    self.py = py
    self.temp = tp


def generate_block_list(total_lines, total_columns, top_temp, right_temp, bottom_temp, left_temp, wd, hg):
  block_list = []  

  for i in range(total_lines):
    block_list.append([])
    for j in range(total_columns):

      if (0 < i < total_lines-1 ) and j == 0:
        b = Block(i*wd, j*hg, top_temp)
      elif (0 < j < total_columns-1 ) and i == total_lines-1:
        b = Block(i*wd, j*hg, right_temp)
      elif (0 < i < total_lines-1 ) and j == total_columns-1:
        b = Block(i*wd, j*hg, bottom_temp)
      elif (0 < j < total_columns-1 ) and i == 0:
        b = Block(i*wd, j*hg, left_temp)
      else:
        b = Block(i*wd, j*hg, 0.0)

      block_list[i].append(b)

  return block_list
