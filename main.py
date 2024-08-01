meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "AGGRO": 'untuk menjadi agresif/marah',
            "SHEESH": 'sedikit ketidaksetujuan',
            "ROFL": 'tanggapan terhadap lelucon'
            }

for i in range(5):
  word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
  if word in meme_dict.keys():
      print(meme_dict[word])
  else:
     print("Word not found")
