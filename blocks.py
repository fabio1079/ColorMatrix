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

      if (i == 0) and (1 <= j < total_columns-1):
        b = Block(i*wd, j*hg, top_temp)
      elif (j == total_columns-1) and (1 <= i < total_lines-1):
        b = Block(i*wd, j*hg, right_temp)
      elif (i == total_lines-1) and (1 <= j < total_columns-1):
        b = Block(i*wd, j*hg, bottom_temp)
      elif (j == 0) and (1 <= i < total_lines-1):
        b = Block(i*wd, j*hg, left_temp)
      else:
        b = Block(i*wd, j*hg, 0.0)

      block_list[i].append(b)

  return block_list

# k = 0
# while k < 1000:
#   for i in range(1, MAX_I-1):
#     for j in range(1, MAX_J-1):
#       t = block_list[i-1][j].temp
#       t += block_list[i][j+1].temp
#       t += block_list[i+1][j].temp
#       t += block_list[i][j-1].temp
#       t *= 0.25

#       block_list[i][j].temp = t

#   k += 1


# b = generate_block_list(8, 6, 4, 3, 2, 1)

# arq = open("temps.txt", "w")

# for i in range(8):
#   for j in range(6):
#     arq.write("%6.2f " % b[i][j].temp)
#   arq.write("\n")

# arq.close()

# from os import system

# system("gedit temps.txt")