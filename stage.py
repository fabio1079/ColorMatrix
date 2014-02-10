import gtk
import blocks
import colors
from random import randint

TOTAL_LINES = 100
TOTAL_COLUMNS = 80
BLOCK_WD = 8
BLOCK_HG = 8

class Stage(gtk.DrawingArea):
  START_I = 0
  START_J = 0

  def __init__(self, color_grade, side_temp):
    gtk.DrawingArea.__init__(self)

    self.color_grade = color_grade
    self.blocks = []
    self.side_temp = side_temp

    self.connect("expose_event", self.expose)

  def expose(self, widget, event):
    self.context = widget.window.cairo_create()
    self.draw_all()

    return False

  def draw(self, block):
    drawable = self.window
    gc = drawable.new_gc()
    gc.set_foreground(self.get_colormap().alloc_color(colors.get_color(block.temp, self.color_grade)))
    gc.fill = gtk.gdk.SOLID
    drawable.draw_rectangle(gc, True, block.px, block.py, BLOCK_WD, BLOCK_HG)

  def draw_all(self):
    self.blocks = blocks.generate_block_list(
            TOTAL_LINES, 
            TOTAL_COLUMNS, 
            self.side_temp[0],
            self.side_temp[1], 
            self.side_temp[2], 
            self.side_temp[3],
            BLOCK_WD, 
            BLOCK_HG
          )

    for i in range(TOTAL_LINES):
      for j in range(TOTAL_COLUMNS):
        self.draw(self.blocks[i][j])

    gtk.timeout_add(1000, self.calculate, 0, self.START_I+1, TOTAL_LINES-2, self.START_J+1, TOTAL_COLUMNS-2)

  def calculate(self, position, min_i, max_i, min_j, max_j):
    k = 0
    while k < 1024:
      position = randint(0, 3)
      if position == 0:
        i = min_i
        j = randint(min_j, max_j)
      elif position == 1:
        j = max_j
        i = randint(min_i, max_i)
      elif position == 2:
        i = max_i
        j = randint(min_j, max_j)
      elif position == 3:
        j = min_j
        i = randint(min_i, max_i)

      temp = self.blocks[i][j].temp
      t = self.blocks[i-1][j].temp
      t += self.blocks[i][j+1].temp
      t += self.blocks[i+1][j].temp
      t += self.blocks[i][j-1].temp
      t *= 0.25

      if temp != t:
        self.blocks[i][j].temp = t
        self.draw(self.blocks[i][j])

      k += 1

    min_i += 1
    max_i -= 1

    min_j += 1
    max_j -= 1

    

    if min_i > max_i or min_j > max_j:
      #print "Min I: %d\nMax I: %d\nMin J: %d\nMax J: %d\n" % (min_i, max_i, min_j, max_j), "="*80
      min_i = self.START_I+1
      max_i = TOTAL_LINES-2
      min_j = self.START_J+1
      max_j = TOTAL_COLUMNS-2

    gtk.timeout_add(1, self.calculate, position, min_i, max_i, min_j, max_j)
