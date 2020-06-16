# TodoList

Q) 프로젝트를 시작할 때 고려사항
### 필수
- 기능적인 면  
    - 1) 할 일을 입력받기 - 입력만.
    - 2) 해야할 일들 - 수정기능, 삭제기능
    - 3) 완료되었을 경우 => 완료된 일들 (삭제기능, 되돌리기)

- 로그인, 로그아웃, 회원가입

- 보여줄 화면  
    - form입력받아서 
    - 진행중인 일들 리스트로 나타내기 (수정삭제 버튼)
    - 완료된 것 -> 완료된 리스트들을 보여주기 (및 수정삭제)


### 필요한 모델
- UserModel
    - id
    - password
    
- TodoModel
    - id
    - ForeignKey(User)
    - isDone > booleanField() // 내가 한 일, 할 일인지 
    - content 할일내용
    
### 함수
User

Todo
    - add_todo_list(user_input) : 유저가 입력한 값을 toDoList (해야할 일)
    - get_done_list() : 끝난 일들
    - get_do_list() : 해야할 일들
    
로그인 성공시 -> 화면으로 무엇을 보여줄지. -> todolist 불러오기
>(- 비로그인시 - 사이트 소개 및 회원가입 -> 회원가입 -> 로그인 -> TodoList 도착)

    - get_todo_list(user_id) -> do_list / done_list

유저가 할 일 등록 / 수정 / 삭제
끝

- todolist
    - 할 일 목록 (+ 버튼)
        - 할 일 입력

    - 한 일 목록

백엔드 -> 프론트에서 어떤 기능이 필요할지, 어떻게 진행을 할지


**꼭 필요한 기능**
User가 할 일을 입력 -> 일을 확인 -> 완료
(To do, doing, done)


- 사이트 소개 > 회원가입 > 로그인 > 등록된 할일 목록 or 빈 목록

### class-based-view
variable-routing으로 어떤 데이터를 받는지에 따라 class를 나눔

```
class
    - get | x 
    - post | x
    - put | o
    - delete | o
```
DB -> 유저에 해당하는 todolist
Todomodel ~ 

auth-token > 