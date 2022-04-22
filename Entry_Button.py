from graphics import *
from EasyRectangle import EasyRectangle

class EntryButton:
    def __init__(self, top_left: Point, title: str, body: str):
        tl_x = top_left.getX() # For easier use
        tl_y = top_left.getY()
        self.title_rectangle = EasyRectangle(
            top_left, 
            Point(tl_x + 112.5, tl_y + 50)
        )

        self.title_text = Text(Point(tl_x + 56.25, tl_y + 25), self.limit_text(title, 12))
        self.title_text.setSize(10)
        self.title_text.setStyle("bold")
        self.title_text.setFace("times roman")
        self.title_text.setTextColor(color_rgb(166, 112, 169))
      
        self.body_rectangle = EasyRectangle(
            Point(tl_x + 112.5, tl_y),
            Point(tl_x + 112.5 + 225, tl_y + 50),
        )

        self.body_text = Text(Point(tl_x + 225, tl_y + 25), self.limit_text(body, 24))
        self.body_text.setSize(10)
        self.body_text.setStyle("bold")
        self.body_text.setFace("times roman")
        self.body_text.setTextColor(color_rgb(166, 112, 169))
      
        self.go_button = EasyRectangle(
            Point(tl_x + 112.5 + 225, tl_y),
            Point(tl_x + 112.5 + 225 + 112.5, tl_y + 50)
        )

        self.go_text = Text(Point(tl_x + 112.5 + 225 + (112.5 / 2), tl_y + 25), "Read →")

    def draw(self, window: GraphWin):
        self.title_rectangle.draw(window)
        self.title_text.draw(window)
        self.body_rectangle.draw(window)
        self.body_text.draw(window)
        self.go_button.draw(window)
        self.go_text.draw(window)

    def limit_text(self, text: str, length: int):
      if len(text) > length:
        return text[0:length - 4] + "..."

      return text
        
