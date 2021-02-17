# 파일을 쓸떄
with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("턱수염 고양이")

# 파일을 읽을때
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
