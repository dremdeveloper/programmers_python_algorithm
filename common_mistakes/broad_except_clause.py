# 버그 은닉: 지나치게 광범위한 except 절

# try-except 구문은 예외(에러)를 처리하는 강력한 도구입니다.
# 하지만 except 절에 'Exception'이나 아무것도 명시하지 않으면(bare except),
# 모든 종류의 예외를 다 잡아버리게 됩니다.
# 이는 당장의 프로그램 중단은 막을 수 있지만, 어떤 에러가 발생했는지 알 수 없게 만들어
# 버그를 찾기 매우 어렵게 만드는 원인이 됩니다. 심지어 KeyboardInterrupt(Ctrl+C) 같은
# 프로그램 종료 신호까지 무시해버릴 수 있습니다.

# 나쁜 예시: 모든 에러를 숨겨버림
def divide_bad(a, b):
    try:
        result = a / b
        print(f"결과: {result}")
    except: # bare except. 모든 것을 잡는다.
        print("어떤 에러인지 모르지만, 아무튼 에러가 발생했습니다.")

print("--- 나쁜 예시 ---")
divide_bad(10, 2)
divide_bad(10, 0) # ZeroDivisionError가 발생했지만, 메시지는 뭉뚱그려져 나옴
divide_bad(10, 'a') # TypeError가 발생했지만, 똑같은 메시지가 나옴


# 좋은 예시: 예상되는 특정 에러만 처리하기
def divide_good(a, b):
    try:
        # 이 코드 블록에서는 TypeError나 ZeroDivisionError가 발생할 수 있음을 예상할 수 있다.
        result = a / b
    except ZeroDivisionError:
        # 0으로 나누려고 할 때의 처리
        print("에러: 0으로 나눌 수 없습니다.")
    except TypeError:
        # 숫자가 아닌 타입으로 연산하려 할 때의 처리
        print("에러: 숫자 타입의 인자가 필요합니다.")
    except Exception as e:
        # 정말 예상치 못한 다른 모든 에러는 여기서 잡아서 로그를 남긴다.
        print(f"예상치 못한 에러가 발생했습니다: {e}")
    else:
        # 에러가 발생하지 않았을 때만 실행
        print(f"결과: {result}")
    finally:
        # 에러 발생 여부와 상관없이 항상 실행
        print("나눗셈 시도가 완료되었습니다.")


print("\n--- 좋은 예시 ---")
divide_good(10, 2)
print("-" * 10)
divide_good(10, 0)
print("-" * 10)
divide_good(10, 'a')
print("-" * 10)
divide_good(int, 5) # 예상치 못한 에러 (TypeError지만 다른 원인)

# 정리:
# - except 절에는 예측 가능한 구체적인 예외 타입(e.g., ValueError, FileNotFoundError)을 명시하는 것이 좋습니다.
# - 여러 종류의 예외를 처리하려면 여러 개의 except 블록을 사용합니다.
# - 모든 에러를 잡고 싶다면 'except Exception as e:'를 사용하여 에러 객체(e)를 받아
#   로그를 남기는 등의 후처리를 하는 것이 바람직합니다.