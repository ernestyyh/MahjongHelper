from mahjonghand import MahjongHand

# Contains the logic to evaluate current hand and returns tiles_to_keep and tiles_to_discard and missing_tiles
class MahjongHandAnalyser:
    def __init__(self):
        pass
    
    def analyse(self, mahjong_hand):
        # Find ideal hand state for each win and calculate distance
        results = []
        results.append(calculate_all_pong_win(mahjong_hand))
        results.append(calculate_13_wonders_win(mahjong_hand))
        results.append(calculate_eight_flower_suit_tile_win(mahjong_hand))
        results.append(calculate_all_dragon_win(mahjong_hand))
        results.append(calculate_all_wind_win(mahjong_hand))

        results.sort(key=lambda x: len(x[2]))
        return results[0]

    def get_tiles_to_discard(self, mahjong_hand, tiles_to_keep):
        tiles_to_keep_by_type = [0] * NUM_TILE_TYPES

        for tile in tiles_to_keep:
            tiles_to_keep_by_type[tile] += 1

        tiles_to_discard = []

        for x in range(NUM_TILE_TYPES):
            num_tiles = mahjong_hand.mahjong_tiles[x] - tiles_to_keep_by_type[x]

            if num_tiles > 0:
                for _ in range(num_tiles):
                    tiles_to_discard.append(x)

        return tiles_to_discard

    def get_non_playable_tiles_to_keep(self, mahjong_hand):
        tiles_to_keep = []

        for x in NON_PLAYABLE:
            num_tiles = mahjong_hand.mahjong_tiles[x]

            if num_tiles > 0:
                tiles_to_keep.append(x)
        
        return tiles_to_keep

    def calculate_normal_win(self, mahjong_hand):
        """
        Normal win with at least 1 Tai
        """
        pass

    def calculate_all_chow_win(self, mahjong_hand):
        """
        Deferred
        """
        pass
  
    def calculate_ping_wu_win(self, mahjong_hand):
        """
        Deferred
        """
        pass

    def calculate_all_pong_win(self, mahjong_hand):
        """
        Need 4 sets of 3-of-a-kind tiles
        """
        has_eye = False
        tiles_to_keep = get_non_playable_tiles_to_keep(mahjong_hand)
        tiles_to_discard = []
        missing_tiles = []

        num_of_sets_required = 4

        duplicates_dict = {'four': [], 'three': [], 'two': [], 'one': []}

        for index, value in enumerate(mahjong_hand):
            if value == 4:
                duplicates_dict['four'].append(index)
            elif value == 3:
                duplicates_dict['three'].append(index)
            elif value == 2:
                duplicates_dict['two'].append(index)
            elif value == 1:
                duplicates_dict['one'].append(index)
        
        for tile in duplicates_dict['four']:
            if num_of_sets_required == 0:
                break
            for i in range(4):
                tiles_to_keep.append(tile)
            num_of_sets_required -= 1

        for tile in duplicates_dict['three']:
            if num_of_sets_required == 0:
                break
            for i in range(3):
                tiles_to_keep.append(tile)
            num_of_sets_required -= 1

        for tile in duplicates_dict['two']:
            if not has_eye:
                tiles_to_keep.append(tile)
                tiles_to_keep.append(tile)
                has_eye = True
                continue

            if num_of_sets_required == 0:
                break
            for i in range(2):
                tiles_to_keep.append(tile)
            missing_tiles.append(tile)
            num_of_sets_required -= 1

        if num_of_sets_required == 0 and has_eye:
            tiles_to_discard = get_tiles_to_discard(mahjong_hand, tiles_to_keep)
            return tiles_to_keep, tiles_to_discard, missing_tiles
        else:
            for tile in duplicates_dict['one']:
                if not has_eye:
                    tiles_to_keep.append(tile)
                    missing_tiles.append(tile)
                    has_eye = True
                    continue
                if num_of_sets_required == 0:
                    break
                tiles_to_keep.append(tile)
                for i in range(2):
                    missing_tiles.append(tile)
                num_of_sets_required -= 1
        
        tiles_to_discard = get_tiles_to_discard(mahjong_hand, tiles_to_keep)
        return tiles_to_keep, tiles_to_discard, missing_tiles

        
    def calculate_half_colour_win(self, mahjong_hand):
        """
        Deferred
        """


    def calculate_full_colour_win(self, mahjong_hand):
        """
        Deferred
        """
        pass
  
    def calculate_all_ones_and_nines_win(self, mahjong_hand):
        """
        Subset of All Pong Win (Deferred to future development)
        """
        pass

    def calculate_half_ones_and_nines_win(self, mahjong_hand):
        """
        Must at least contain one set of Ones/Nines and at least one set of Dragon/Wind.
        Subset of All Pong Win (Deferred to future development)
        """
        pass

    def calculate_13_wonders_win(self, mahjong_hand):
        has_eye = False
        tiles_to_keep = get_non_playable_tiles_to_keep(mahjong_hand)
        tiles_to_discard = []
        missing_tiles = []

        for x in WONDERS:
            num_tiles = mahjong_hand.mahjong_tiles[x]

            if num_tiles < 1:
                missing_tiles.append(x)
            elif num_tiles == 1:
                tiles_to_keep.append(x)
            elif num_tiles == 2:
                if not has_eye:
                    has_eye = true

                    for _ in range(num_tiles):
                        tiles_to_keep.append(x)
                else:
                    tiles_to_keep.append(x)
            else:
                tiles_to_keep.append(x)
                
        if not has_eye:
            missing_tiles.append(WONDERS)

        tiles_to_discard = get_tiles_to_discard(mahjong_hand, tiles_to_keep)

        return tiles_to_keep, tiles_to_discard, missing_tiles
  
    def calculate_eight_flower_suit_tile_win(self, mahjong_hand):
        tiles_to_keep = []
        tiles_to_discard = []
        missing_tiles = []

        for x in FLOWERS:
            if mahjong_hand.mahjong_tiles[x] < 1:
                missing_tiles.append(x)
        
        for y in range(NUM_TILE_TYPES):
            num_tiles = mahjong_hand.mahjong_tiles[y]

            if num_tiles > 0:
                for _ in range(num_tiles):
                    tiles_to_keep.append(y)

        return tiles_to_keep, tiles_to_discard, missing_tiles

    def calculate_all_dragon_win(self, mahjong_hand):
        tiles_to_keep = get_non_playable_tiles_to_keep(mahjong_hand)
        tiles_to_discard = []
        missing_tiles = []

        for x in DRAGONS:
            num_tiles = mahjong_hand.mahjong_tiles[x]

            if num_tiles > 0:
                for _ in range(num_tiles):
                    tiles_to_keep.append(x)

            if num_tiles < 3:
                for _ in range(3 - num_tiles):
                    missing_tiles.append(x)

        tiles_to_discard = get_tiles_to_discard(mahjong_hand, tiles_to_keep)

        return tiles_to_keep, tiles_to_discard, missing_tiles

    def calculate_all_wind_win(self, mahjong_hand):
        tiles_to_keep = get_non_playable_tiles_to_keep(mahjong_hand)
        tiles_to_discard = []
        missing_tiles = []

        for x in WINDS:
            num_tiles = mahjong_hand.mahjong_tiles[x]

            if num_tiles > 0:
                for _ in range(num_tiles):
                    tiles_to_keep.append(x)

            if num_tiles < 3:
                for _ in range(3 - num_tiles):
                    missing_tiles.append(x)

        tiles_to_discard = get_tiles_to_discard(mahjong_hand, tiles_to_keep)

        return tiles_to_keep, tiles_to_discard, missing_tiles