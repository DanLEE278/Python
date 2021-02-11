score_file = open("score.txt", "w", encoding="utf8") # "w"를 설정하게되면 덮어쓰게 됨
print("수학 : 91", file=score_file)
print("영어 : 94", file=score_file)
score_file.close()

score_file = open("score.txt","a", encoding="utf8")
score_file.write("과학 : 87")
score_file.write("\n코딩 : 96")
score_file.close()
