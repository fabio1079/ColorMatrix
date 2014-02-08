import gtk
import blocks
import colors

TOTAL_LINES = 80
TOTAL_COLUMNS = 60
BLOCK_WD = 10
BLOCK_HG = 10
BLOCK_TEMP_TOP = 40.0
BLOCK_TEMP_RIGHT = 30.0
BLOCK_TEMP_BOTTOM = 20.0
BLOCK_TEMP_LEFT = 10.0

class Stage(gtk.DrawingArea):
  def __init__(self, color_grade):
    gtk.DrawingArea.__init__(self)

    self.color_grade = color_grade
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
    bks = blocks.generate_block_list(
            TOTAL_LINES, 
            TOTAL_COLUMNS, 
            BLOCK_TEMP_TOP, 
            BLOCK_TEMP_RIGHT, 
            BLOCK_TEMP_BOTTOM, 
            BLOCK_TEMP_LEFT,
            BLOCK_WD, 
            BLOCK_HG
          )

    for i in range(TOTAL_LINES):
      for j in range(TOTAL_COLUMNS):
        self.draw(bks[i][j])


if __name__ == "__main__":
  window = gtk.Window()
  window.set_size_request(800, 600)

  stg = Stage(max(BLOCK_TEMP_TOP, BLOCK_TEMP_RIGHT, BLOCK_TEMP_BOTTOM, BLOCK_TEMP_LEFT)/64.0)
  window.add(stg)

  window.connect("destroy", gtk.main_quit)
  window.show_all()
  gtk.main()