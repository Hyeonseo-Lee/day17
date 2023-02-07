
def isQueueFull() :
    global SIZE, queue, front, rear
    if (rear == SIZE-1) :
        return True
    else :
        return False

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print("큐가 비었습니다.")
        return None
    return queue[front+1]

def call(str):
    global SIZE, queue, front, rear, time
    if str == "사용":
        enQueue("('사용', 9)")
        time += 9
    elif str == "고장":
        enQueue("('고장', 3)")
        time += 3
    elif str == "환불":
        enQueue("('환불', 4)")
        time += 4
    else:
        time += 0

def printqueue():
    global SIZE, queue, front, rear, time
    if not isQueueFull():
        print(f'귀하의 대기 예상시간은 {time}분입니다.')
        print('현재 대기 콜 -->', queue)
    else:
        print('최종 대기 콜 -->', queue)

SIZE = 6
queue = [ None for _ in range(SIZE) ]
front = rear = 0
time = 0
## 메인 코드 부분 ##
if __name__ == "__main__" :

    printqueue()
    call("사용")
    printqueue()
    call("고장")
    printqueue()
    call("환불")
    printqueue()
    call("환불")
    printqueue()
    call("고장")
    printqueue()

    print("프로그램 종료!")
