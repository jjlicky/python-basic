oreo={"식품유형":"과자","과자명":"오레오",
      "중량":"100g", "원재료명":"밀가루, 설탕, 식물성유지",
      "제조원":"미가방 유한회사"}
print(oreo)

oreo["과자명"]="마일드 오레오"
print(oreo)

del oreo["중량"]

if"유통기한"in oreo:
    print("True")
else:
    print("False")
    oreo["유통기한"] = "20121.09.10까지"
print(oreo)

