import gtk
import blocks
import colors

TOTAL_LINES = 100
TOTAL_COLUMNS = 80
BLOCK_WD = 8
BLOCK_HG = 8

class Stage(gtk.DrawingArea):
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

    gtk.timeout_add(1000, self.calculate)

  def calculate(self):
    for i in range(1, TOTAL_LINES-1):
      for j in range(1, TOTAL_COLUMNS-1):
        temp = self.blocks[i][j].temp
        t = self.blocks[i-1][j].temp
        t += self.blocks[i][j+1].temp
        t += self.blocks[i+1][j].temp
        t += self.blocks[i][j-1].temp
        t *= 0.25

        if temp != t:
          self.blocks[i][j].temp = t
          self.draw(self.blocks[i][j])

    gtk.timeout_add(1, self.calculate)
