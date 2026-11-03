import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "hello"}


pcs = [
    {"id": 1, "name": "mac", "disk": "80%", "last_backup": "2026-10-24"},
    {"id": 2, "name": "window", "disk": "90%", "last_backup": "2026-09-23"},
    {"id": 3, "name": "rinux", "disk": "67%", "last_backup": "2026-10-14"},
]


@app.get("/pcs")
def read_pc_list():
    conn = sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT * FROM pcs")
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.get("/pcs/{pc_id}")
def read_pc(pc_id: int):
    for pc in pcs:
        if pc["id"] == pc_id:
            return pc
    raise HTTPException(status_code=404, detail="PC를 찾을 수 없음")


# -----------------------------------------------------------------------


class PcCreate(BaseModel):
    name: str
    disk: str
    last_backup: str


@app.post("/pcs", status_code=201)
def create_pc(pc: PcCreate):
    new_pc = {
        "id": len(pcs) + 1,
        "name": pc.name,
        "disk": pc.disk,
        "last_backup": pc.last_backup,
    }
    pcs.append(new_pc)
    return new_pc
