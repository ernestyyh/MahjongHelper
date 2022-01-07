tiles = model.predict(input)
hand = MahjongHand(tiles)

analyser = MahjongHandAnalyser()
results = analyser.analyser(hand)
#send_telegram(results)