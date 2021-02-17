# 피클은 텍스트 상태의 데이터가 아닌 객체 자체를 저장한다
# 텍스트 파일보다 속도면에서 우위
import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수","나이":30,"취미":["축구","농구","골프"]}
# print(profile)
# pickle.dump(profile,profile_file) # profile 에 있는 정보를 file에 저장
# profile_file.close()

profile_file = open("profile.pickle","rb") # read binary
profile = pickle.load(profile_file) # file 에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
