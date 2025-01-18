meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "CREEPY": "İngilizce kelime anlatımını yansıtarak garip, ürkünç anlamına gelmektedir",
    "GG": "İngilizce 'good game' cümlesinin kısaltması olarak 'iyi oyundu' demektir",
    "ASAP": "İngilizce 'as soon as possible' cümlesinin kısaltmasıdır, Türkçe karşılığı ise 'mümkün olduğunca yakın/kısa zamanda'dır"
}
for i in range(5):
   word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
   if word in meme_dict.keys():
       print(meme_dict[word])
    
else:
    print("Maalesef , bu sözük bizim sözlüğümüzde bulunmamaktadır isterseniz internet üzeirnden araştırabilirsiniz")
