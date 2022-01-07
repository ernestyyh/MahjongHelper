import constants as ct

# Contains the representation of a mahjong hand
class MahjongHand:
	def __init__(self, tiles):
		self.num_of_tiles = 0
		self.mahjong_tiles = [0] * ct.NUM_TILE_TYPES

		for tile in tiles:
			#TODO: add the output (set of tiles) from the model to the hand (mahjong_tiles)