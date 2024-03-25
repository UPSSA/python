import webbrowser
print("안녕하세요", end="")
print(" 무엇이든..입력해봐라")
q=input("검색어를 입력하세요 : ")
webbrowser.open("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="+q)
