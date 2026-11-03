# 배운 것 노트

## 2026-11-01 — 1주차 완료 (GET / POST / pydantic)
- **pydantic = zod**: 함수 파라미터에 `pc: PcCreate`라고 쓰면 FastAPI가 알아서 검증하고, 실패하면 내 함수 실행 전에 422를 돌려준다. (path param도 body도 같은 원리)
- **점 vs 대괄호**: dict는 `pc["name"]`, 클래스 인스턴스(pydantic 모델)는 `pc.name`. JS는 둘이 같지만 Python은 구분한다. `len(pcs)`는 함수이고 `.length`가 아니다.
- **메모리 변수는 서버 끄면 사라진다**: `pcs` 리스트는 프로세스 RAM에 있어서 재시작하면 코드의 초기값 3개로 돌아감 (`useState` 새로고침과 같음). 그래서 DB가 필요하다.
- 다음 할 일: SQLite로 `pcs`를 디스크에 저장하기

## 2026-11-02 — 2주차 시작 (sqlite3 기본)
- **SQLite = 파일 하나짜리 DB**: `sqlite3.connect("app.db")`로 열고, SQL 문자열을 `cur.execute()`로 던진다. Python이 SQL로 바뀌는 게 아니라, Python이 SQL을 DB에 전달하는 구조. 서버 꺼도 파일은 남는다.
- **흐름은 항상 connect → cursor → execute → (commit) → fetch → close**. INSERT/UPDATE/DELETE는 `commit()` 없으면 저장 안 됨. 서버 안에선 요청마다 함수 **안에서** 열고 꼭 `close()`.
- **fetchone()은 없으면 None** (JS의 null). 그래서 `if row is None: 404`. 원소 1개 튜플은 `(2,)` 쉼표 필수, `(2)`는 그냥 숫자. SELECT 결과 기본은 튜플이라 `row[1]`로 꺼내야 함.
- 다음 할 일: `conn.row_factory = sqlite3.Row` + `[dict(row) for row in rows]`로 `/pcs` 응답을 `{"id":1,"name":"mac"}` 모양으로 바꾸기. 그다음 GET /pcs/{id}, POST 순서로 DB화.
