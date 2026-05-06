from fastapi import FastAPI, HTTPException, Query
import httpx
import xmltodict
import asyncio
from typing import List, Dict
from pydantic import BaseModel

app = FastAPI(title="Kwangwoon Study Room Total Proxy")

KW_API_URL = "https://mobileid.kw.ac.kr/mobile/MA/xml_Study_Room_Map.php"
HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "kw/2.2.5 (iPhone; iOS 26.1; Scale/3.00)"
}

# 룸 타입 정의
ROOM_TYPES = {
    "4a": "4인실(4-7실)",
    "4b": "4인실(8-11실)",
    "6": "6인실(2,3,12실)",
    "10": "10인실(1,13실)"
}

class RoomStatus(BaseModel):
    time: str
    availability: Dict[str, str]

@app.get("/studyroom/all")
async def get_all_study_room_status(
    search_date: str = Query(..., description="YYYYMMDD 형식")
):
    # 1. 모든 룸 타입에 대해 비동기 요청 생성
    async with httpx.AsyncClient() as client:
        tasks = []
        for code in ROOM_TYPES.keys():
            payload = {"room_seat_no": code, "search_date": search_date}
            tasks.append(client.post(KW_API_URL, data=payload, headers=HEADERS, timeout=10.0))
        
        # 4개 요청을 동시에 실행
        responses = await asyncio.gather(*tasks, return_exceptions=True)

    total_result = {}

    # 2. 각 응답 결과 파싱 및 통합
    for i, response in enumerate(responses):
        if isinstance(response, Exception):
            continue
        
        try:
            data_dict = xmltodict.parse(response.text)
            item = data_dict['root']['item']
            
            # 해당 타입의 룸 이름 추출
            current_rooms = []
            for r in range(4):
                name = item.get(f'room_name_{r}')
                if name and name.strip():
                    current_rooms.append(name)

            # 시간대별 데이터 통합
            time_entries = item.get('time_list', [])
            if isinstance(time_entries, dict):
                time_entries = [time_entries]

            for entry in time_entries:
                time_val = entry.get('time_period')
                # 시간 키 생성 (예: "09000955")
                if time_val not in total_result:
                    total_result[time_val] = {}
                
                # 각 방의 상태 추가
                for idx, name in enumerate(current_rooms):
                    status_code = entry.get(f'time_period_arr_{idx}')
                    total_result[time_val][name] = "예약불가" if status_code == "5" else "예약가능"
        except:
            continue

    # 3. 결과 데이터를 시간순으로 정렬하여 반환
    sorted_schedule = []
    for t_key in sorted(total_result.keys()):
        formatted_time = f"{t_key[:2]}:{t_key[2:4]}~{t_key[4:6]}:{t_key[6:]}"
        sorted_schedule.append({
            "time": formatted_time,
            "availability": total_result[t_key]
        })

    return {
        "date": search_date,
        "total_rooms_count": sum(len(v) for v in total_result.values()) // len(total_result) if total_result else 0,
        "schedule": sorted_schedule
    }