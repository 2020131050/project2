def block_message(message, blocked_words):
    """
    주어진 메시지에 차단된 단어가 포함되어 있으면 해당 메시지를 차단합니다.
    
    :param message: 사용자로부터 받은 메시지
    :param blocked_words: 차단할 단어 목록
    :return: 차단된 메시지 또는 정상적인 메시지
    """
    # 메시지를 소문자로 변환하여 대소문자 구분 없이 처리
    message_lower = message.lower()

    # 차단된 단어가 포함되어 있으면 메시지를 차단
    for word in blocked_words:
        if word.lower() in message_lower:
            return "차단된 메세지."
    
    # 차단된 단어가 없으면 메시지 그대로 반환
    return message

# 차단할 단어 목록
blocked_words = ["주식", "hot gril", "http", "무료"]

# 사용자로부터 메시지 입력받기
message = input("메시지를 입력하세요: ")

# 메시지 차단 여부 확인
result = block_message(message, blocked_words)

print(result)
