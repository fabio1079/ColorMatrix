import gtk
import stage

BLOCK_TEMP_TOP = 40.0
BLOCK_TEMP_RIGHT = 40.0
BLOCK_TEMP_BOTTOM = 40.0
BLOCK_TEMP_LEFT = 40.0

def main():
  window = gtk.Window()
  window.set_size_request(800, 640)

  stg = stage.Stage(
    max(BLOCK_TEMP_TOP, BLOCK_TEMP_RIGHT, BLOCK_TEMP_BOTTOM, BLOCK_TEMP_LEFT)/64.0,
    [BLOCK_TEMP_TOP, BLOCK_TEMP_RIGHT, BLOCK_TEMP_BOTTOM, BLOCK_TEMP_LEFT]
  )
  window.add(stg)

  window.connect("destroy", gtk.main_quit)
  window.show_all()
  gtk.main()



if __name__ == "__main__":
  main()
