def solution(word_list):
    talk_list = ["aya", "ye", "woo", "ma"]
    talkx2_list = ["aya"*2, "ye"*2, "woo"*2, "ma"*2]
    count = 0
    isOk = True
    for word in word_list:
        isOk = True
        for talkx2 in talkx2_list:
            if word.find(talkx2) != -1:
                isOk = False
                break
        if isOk == False:
            continue

        # print("word들:",word,end="!")
        for talk in talk_list:
            word = word.replace(talk,"")
            
        if not word:
            count += 1
    
    return count
    
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
    


    # text.strip("a")
    # str_text.find('a')
