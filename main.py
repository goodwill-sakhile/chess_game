from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from touch import TouchBox
from kivy.lang import Builder
root = Builder.load_string("""
<Blocks>:
	md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
<IconButton>:
	size_hint:None, None
	size:"50dp", "50dp"
	id:icon_button
	icon:""
	icon_size:"30dp"
	pos_hint:{"center_x":.5, "center_y":.5}
<ChessBox>:
	size_hint:None, None
	size:"416dp", "416dp"
	spacing:2
	#md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
	pos_hint:{"center_x":.5, "center_y":.5}
	rows:8
	cols:8
<MainBox>:
	md_bg_color:[47/float(255), 79/float(255), 79/float(255), 1]
	orientation:"vertical"
	MDBoxLayout:
		Widget:
		ChessBox:
		Widget:
""")
class Blocks(TouchBox):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.block_number = 0
	def respondToTouch(self):
		print(self.block_number)
class IconButton(MDIconButton):
	pass
class ChessBox(MDGridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.block_number = 0
		self.color_1 = [139/float(255), 69/float(255), 19/float(255), 1]
		self.color_2 = [210/float(255), 180/float(255), 140/float(255), 1]
		self.putBlocks()
	def positionRook(self, block):
		if block.block_number == 1 or block.block_number == 8:
			icon_button = IconButton()
			icon_button.icon = "chess-rook"
			block.add_widget(icon_button)
		elif block.block_number == 57 or block.block_number == 64:
			icon_button = IconButton()
			icon_button.theme_text_color = "Custom"
			icon_button.text_color = [220/float(255), 220/float(255), 220/float(255), 1]
			icon_button.icon = "chess-rook"
			block.add_widget(icon_button)
	def positionNight(self, block):
		if block.block_number == 2 or block.block_number == 7:
			icon_button = IconButton()
			icon_button.icon = "chess-knight"
			block.add_widget(icon_button)
		elif block.block_number == 58 or block.block_number == 63:
			icon_button = IconButton()
			icon_button.theme_text_color = "Custom"
			icon_button.text_color = [220/float(255), 220/float(255), 220/float(255), 1]
			icon_button.icon = "chess-knight"
			block.add_widget(icon_button)
	def positionBishop(self, block):
		if block.block_number == 3 or block.block_number == 6:
			icon_button = IconButton()
			icon_button.icon = "chess-bishop"
			block.add_widget(icon_button)
		elif block.block_number == 59 or block.block_number == 62:
			icon_button = IconButton()
			icon_button.theme_text_color = "Custom"
			icon_button.text_color = [220/float(255), 220/float(255), 220/float(255), 1]
			icon_button.icon = "chess-bishop"
			block.add_widget(icon_button)
	def positionQueen(self, block):
		if block.block_number == 4:
			icon_button = IconButton()
			icon_button.icon = "chess-queen"
			block.add_widget(icon_button)
		elif block.block_number == 60:
			icon_button = IconButton()
			icon_button.theme_text_color = "Custom"
			icon_button.text_color = [220/float(255), 220/float(255), 220/float(255), 1]
			icon_button.icon = "chess-queen"
			block.add_widget(icon_button)
	def positionKing(self, block):
		if block.block_number == 5:
			icon_button = IconButton()
			icon_button.icon = "chess-king"
			block.add_widget(icon_button)
		elif block.block_number == 61:
			icon_button = IconButton()
			icon_button.theme_text_color = "Custom"
			icon_button.text_color = [220/float(255), 220/float(255), 220/float(255), 1]
			icon_button.icon = "chess-king"
			block.add_widget(icon_button)
	def positionPawn(self, block):
		if block.block_number in [9, 10, 11, 12, 13, 14, 15, 16]:
			icon_button = IconButton()
			icon_button.icon = "chess-pawn"
			block.add_widget(icon_button)
		elif block.block_number in [ 49, 50, 51, 52, 53, 54, 55, 56]:
			icon_button = IconButton()
			icon_button.icon = "chess-pawn"
			icon_button.theme_text_color = "Custom"
			icon_button.text_color = [220/float(255), 220/float(255), 220/float(255), 1]
			block.add_widget(icon_button)
	def putBlocks(self):
		j = 1
		for i in range(64):
			box = Blocks()
			self.block_number += 1
			box.block_number = self.block_number
			
			if (box.block_number % 2) == 0:
				box.md_bg_color = self.color_1
			else:
				box.md_bg_color = self.color_2
			if (j %8) == 0:
				temp = self.color_1
				self.color_1 = self.color_2
				self.color_2 = temp
				j = 1
			else:
				j += 1
			self.positionRook(box)
			self.positionNight(box)
			self.positionBishop(box)
			self.positionBishop(box)
			self.positionQueen(box)
			self.positionKing(box)
			self.positionPawn(box)
			self.add_widget(box)
class MainBox(MDBoxLayout):
	pass
class MainApp(MDApp):
	def build(self):
		root = MainBox()
		return root
if __name__ == "__main__":
	MainApp().run()