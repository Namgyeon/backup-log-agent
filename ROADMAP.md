# AI 엔지니어 전환 로드맵 (12주)

**목표**: AI 엔지니어로 커리어 전환. 포트폴리오 = "백업일지 에이전트" 하나를 끝까지 배포.
**조건**: 주 3~5시간, Python/FastAPI, 프론트는 React 직접, LLM은 Claude SDK 직접 호출.
**학습법**: 코드는 Claude가 짜고, 나는 읽고 판단한다. 단계마다 직접 치는 것 1개, 읽을 자료 1개, 배포되는 결과물 1개.

## 조사 근거 (2026-11-03)
- 채용공고 3,449건 분석: Python 71%, LLM 66%, RAG 40%, API 33%, 모니터링 31%, SQL 19%, Docker 18%, 벡터DB 18%. 신입 공고 6%. 대부분 "배포한 LLM 프로젝트 1개 이상" 요구. ([dev.to 분석](https://dev.to/gnana_6392e836fd500a957dc/ai-engineer-skills-companies-want-in-2026-3449-posting-analysis-5f9l))
- Anthropic "Building Effective Agents": 프레임워크보다 API 직접 호출부터, 에이전트보다 워크플로우 패턴 먼저, 복잡도는 측정하고 올려라. ([원문](https://www.anthropic.com/research/building-effective-agents))
- 오픈소스 로드맵 공통: 코스 1개 + 프레임워크 문서 1개 → 깨지는 프로젝트 2~3개 → evals/트레이싱/배포. 수학·모델학습·파인튜닝 스킵. ([start-ai-engineering](https://github.com/louisfb01/start-ai-engineering), [ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) Phase 11→13→14→17)
- 무료 공식 코스: [Anthropic Academy](https://anthropic.skilljar.com/) (Building with the Claude API, Intro to MCP, MCP Advanced), [MS ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners), [HF Agents Course](https://huggingface.co/learn/agents-course)

## 주차별 계획

| 주 | 단계 | 결과물 | 병행 코스 |
|---|---|---|---|
| 1 | **백엔드 바닥 마무리**: SQLModel CRUD(GET/POST/PUT/DELETE), `async def`, `.env`, router 분리, git+GitHub | 백업일지 API 공개 레포 | - |
| 2~3 | **LLM API 직접 호출**: Claude SDK, pydantic 구조화 출력, prompt caching, 스트리밍(SSE) → React 채팅 UI | 자유 텍스트 백업일지 → 구조화 → DB 저장 + 채팅 | Academy: Building with the Claude API |
| 4~5 | **Tool use + 에이전트 루프 직접 구현**: DB CRUD를 도구로 노출, 워크플로우 패턴 5개(chaining/routing/parallel/orchestrator/evaluator) | "어제 백업 안 된 PC 뭐야?" 채팅 | MS ai-agents-for-beginners 4, 7강 |
| 6 | **MCP 서버**: FastMCP로 내 API를 Claude Code/데스크탑에서 쓰게 | MCP 서버 | Academy: Intro to MCP |
| 7~8 | **RAG**: 임베딩, 벡터 저장(sqlite-vec 또는 pgvector), 청킹, 출처 표시, 검색 디버깅 | 매뉴얼·로그 문서 질의 | MS 5강 (Agentic RAG) |
| 9~10 | **백그라운드 자동화 + Evals + 관측**: 스케줄러로 로그 분류·요약·알림, pytest+LLM judge 회귀 테스트, 트레이싱(Logfire 등). LangGraph로 한 번 포팅 | 자동 일일 리포트 + eval 세트 | Hamel Husain evals 글 |
| 11~12 | **Docker + 배포 + README** | 실제 URL + 포트폴리오 README | Academy: MCP Advanced (선택) |

## 스킵하는 것 (필요하면 나중에)
수학, PyTorch, 모델 학습, 파인튜닝, 멀티 에이전트 스웜, 자체 모델 서빙(vLLM), Kubernetes.

## 진행 기록
- 2026-11-03: 로드맵 확정. 1주차 시작.
