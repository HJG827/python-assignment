import sys
sys.stdin = open('input.txt', 'r')

import sys
# 7비트 패턴에 해당하는 숫자 딕셔너리
code_dict = {
    "0001101": 0, "0011001": 1, "0010011": 2, "0111101": 3,
    "0100011": 4, "0110001": 5, "0101111": 6, "0111011": 7,
    "0110111": 8, "0001011": 9
}

def hex_to_binary(hex_string):
    """ 16진수를 2진수로 변환하는 함수 """
    return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)

def decode_password(binary_code, ratio):
    """ 56자리의 2진 암호코드를 숫자로 변환하는 함수 """
    numbers = []
    for i in range(0, 56, 7):
        segment = binary_code[i * ratio : (i + 7) * ratio : ratio]  # 비율 적용
        if segment in code_dict:
            numbers.append(code_dict[segment])
        else:
            return None  # 잘못된 코드
    return numbers

def is_valid_code(numbers):
    """ 암호코드가 유효한지 검사하는 함수 """
    odd_sum = sum(numbers[i] for i in range(0, 8, 2))  # 홀수 자리 합
    even_sum = sum(numbers[i] for i in range(1, 8, 2)) # 짝수 자리 합
    return (odd_sum * 3 + even_sum) % 10 == 0

def solve():
    T = int(input())  # 테스트 케이스 개수
    results = []
    
    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        hex_matrix = [input().strip() for _ in range(N)]
        
        binary_lines = set()  # 중복된 줄 제거
        for row in hex_matrix:
            binary_row = hex_to_binary(row)
            if "1" in binary_row:
                binary_lines.add(binary_row.rstrip("0"))  # 0을 제거하고 저장
        
        valid_codes = set()  # 이미 해석한 암호코드 저장
        
        for line in binary_lines:
            end_idx = len(line) - 1  # 끝에서부터 탐색
            while end_idx >= 55:
                if line[end_idx] == "1":
                    start_idx = end_idx - 55
                    raw_code = line[start_idx:end_idx + 1]
                    
                    # 비율 계산 (56의 배수 찾기)
                    for ratio in range(1, (end_idx - start_idx + 1) // 56 + 1):
                        numbers = decode_password(raw_code, ratio)
                        if numbers and tuple(numbers) not in valid_codes:
                            valid_codes.add(tuple(numbers))
                            break  # 여러 비율이 있더라도 한 번만 확인

                end_idx -= 1  # 다음 암호코드 탐색
        
        total_sum = sum(sum(code) for code in valid_codes if is_valid_code(code))
        results.append(f"#{tc} {total_sum}")
    
    for result in results:
        print(result)

solve()
