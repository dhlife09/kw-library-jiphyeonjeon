
# kw-library-jiphyeonjeon

광운대학교 도서관에서 그룹스터디룸(집현전) 예약현황을 확인할 수 있는 API 입니다.

> 개인적/연구적 목적으로만 사용할 수 있습니다.


## 분석 과정

프록시 서버 구현 후, 실제 모바일 환경에서 프록시 서버에 연결한 다음 광운대학교 도서관 어플리케이션에서 집현전 리스트를 조회하는 과정을 분석하여 FastAPI로 사용할 수 있게 제작하였습니다.


### Request (사용자 → 광운대 도서관 서버)
```bash
POST /mobile/MA/xml_Study_Room_Map.php HTTP/1.1
Host: mobileid.kw.ac.kr
Content-Type: application/x-www-form-urlencoded
Connection: keep-alive
Accept: */*
User-Agent: kw/2.2.5 (iPhone; iOS 26.1; Scale/3.00)
Accept-Language: ko-KR;q=1, en-KR;q=0.9
Accept-Encoding: gzip, deflate, br
Content-Length: 36

room_seat_no=4a&search_date=20260506
```
|parameter|비고|
|------------|----|
|room_seat_no|4a(4인실 4,5,6,7실), 4b(4인실 8,9,10,11실), 6인실(2,3,12실), 10인실(1,13실)|
|search_date|조회하는 날짜(yyyymmdd)|

### Response (광운대 도서관 서버 → 사용자)
```bash
HTTP/1.1 200 OK
Content-Type: text/html
Server: Microsoft-IIS/8.5
X-Powered-By: PHP/5.3.16
Date: Tue, 05 May 2026 05:24:35 GMT
Content-Length: 6086

<?xml version='1.0' encoding='utf-8'?>
<root><item><room_no_0><![CDATA[4]]></room_no_0><room_no_1><![CDATA[5]]></room_no_1><room_no_2><![CDATA[6]]></room_no_2><room_no_3><![CDATA[7]]></room_no_3><room_name_0><![CDATA[집현 4실]]></room_name_0><room_name_1><![CDATA[집현 5실]]></room_name_1><room_name_2><![CDATA[집현 6실]]></room_name_2><room_name_3><![CDATA[집현 7실]]></room_name_3><select_day_01><![CDATA[20260505]]></select_day_01><select_day_02><![CDATA[20260506]]></select_day_02><select_day_03><![CDATA[20260507]]></select_day_03><select_day_04><![CDATA[20260508]]></select_day_04><select_day_05><![CDATA[20260509]]></select_day_05><select_day_06><![CDATA[20260510]]></select_day_06><select_day_07><![CDATA[20260511]]></select_day_07><time_list><time_period><![CDATA[09000955]]></time_period><time_period_arr_0><![CDATA[0]]></time_period_arr_0><time_period_arr_1><![CDATA[0]]></time_period_arr_1><time_period_arr_2><![CDATA[0]]></time_period_arr_2><time_period_arr_3><![CDATA[0]]></time_period_arr_3><time_period_arr_4><![CDATA[]]></time_period_arr_4><time_period_arr_5><![CDATA[]]></time_period_arr_5></time_list><time_list><time_period><![CDATA[10001055]]></time_period><time_period_arr_0><![CDATA[5]]></time_period_arr_0><time_period_arr_1><![CDATA[0]]></time_period_arr_1><time_period_arr_2><![CDATA[5]]></time_period_arr_2><time_period_arr_3><![CDATA[0]]></time_period_arr_3><time_period_arr_4><![CDATA[]]></time_period_arr_4><time_period_arr_5><![CDATA[]]></time_period_arr_5></time_list><time_list><time_period><![CDATA[11001155]]></time_period><time_period_arr_0><![CDATA[5]]></time_period_arr_0><time_period_arr_1><![CDATA[0]]></time_period_arr_1><time_period_arr_2><![CDATA[5]]></time_period_arr_2><time_period_arr_3><![CDATA[5]]></time_period_arr_3><time_period_arr_4><![CDATA[]]></time_period_arr_4><time_period_arr_5><![CDATA[]]></time_period_arr_5></time_list><time_list><time_period><![CDATA[12001255]]></time_period><time_period_arr_0><![CDATA[5]]></time_period_arr_0><time_period_arr_1><![CDATA[0]]></time_period_arr_1><time_period_arr_2><![CDATA[0]]></time_period_arr_2><time_period_arr_3><![CDATA[5]]></time_period_arr_3><time_period_arr_4><![CDATA[]]></time_period_arr_4><time_period_arr_5><![CDATA[]]></time_period_arr_5></time_list><time_list><time_period><![CDATA[13001355]]></time_period><time_period_arr_0><![CDATA[5]]></time_period_arr_0><time_period_arr_1><![CDATA[5]]></time_period_arr_1><time_period_arr_2><![CDATA[5]]></time_period_arr_2><time_period_arr_3><![CDATA[5]]></time_period_arr_3><time_period_arr_4><![CDATA[]]></time_period_arr_4><time_period_arr_5><![CDATA[]]></time_period_arr_5></time_list><time_list><time_period><![CDATA[14001455]]></time_period><time_period_arr_0><![CDATA[5]]></time_period_arr_0><time_period_arr_1><![CDATA[5]]></time_period_arr_1><time_period_arr_2><![CDATA[5]]></time_period_arr_2><time_period_arr_3><![CDATA[5]]></time_period_arr_3><time_period_arr_4><![CDATA[]]></time_period_arr_4><time_period_arr_5><![CDATA[]]></time_period_arr_5></time_list><time_list><time_period><![CDATA[15001555]]></time_period><time_period_arr_0><![CDATA[5]]></time_period_arr_0><time_period_arr_1><![CDATA[5]]></time_period_arr_1><time_period_arr_2><![CDATA[5]]></time_period_arr_2><time_period_arr_3><![CDATA[5]]></time_period_arr_3><time_period_arr_4><![CDATA[]]></time_period_arr_4><time_period_arr_5><![CDATA[]]></time_period_arr_5></time_list><time_list><time_period><![CDATA[16001655]]></time_period><time_period_arr_0><![CDATA[0]]></time_period_arr_0><time_period_arr_1><![CDATA[5]]></time_period_arr_1><time_period_arr_2><![CDATA[5]]></time_period_arr_2><time_period_arr_3><![CDATA[5]]></time_period_arr_3><time_period_arr_4><![CDATA[]]></time_period_arr_4><time_period_arr_5><![CDATA[]]></time_period_arr_5></time_list><time_list><time_period><![CDATA[17001755]]></time_period><time_period_arr_0><![CDATA[5]]></time_period_arr_0><time_period_arr_1><![CDATA[0]]></time_period_arr_1><time_period_arr_2><![CDATA[0]]></time_period_arr_2><time_period_arr_3><![CDATA[0]]></time_period_arr_3><time_period_arr_4><![CDATA[]]></time_period_arr_4><time_period_arr_5><![CDATA[]]></time_period_arr_5></time_list><time_list><time_period><![CDATA[18001855]]></time_period><time_period_arr_0><![CDATA[5]]></time_period_arr_0><time_period_arr_1><![CDATA[0]]></time_period_arr_1><time_period_arr_2><![CDATA[5]]></time_period_arr_2><time_period_arr_3><![CDATA[5]]></time_period_arr_3><time_period_arr_4><![CDATA[]]></time_period_arr_4><time_period_arr_5><![CDATA[]]></time_period_arr_5></time_list><time_list><time_period><![CDATA[19001955]]></time_period><time_period_arr_0><![CDATA[5]]></time_period_arr_0><time_period_arr_1><![CDATA[0]]></time_period_arr_1><time_period_arr_2><![CDATA[5]]></time_period_arr_2><time_period_arr_3><![CDATA[5]]></time_period_arr_3><time_period_arr_4><![CDATA[]]></time_period_arr_4><time_period_arr_5><![CDATA[]]></time_period_arr_5></time_list><time_list><time_period><![CDATA[20002055]]></time_period><time_period_arr_0><![CDATA[0]]></time_period_arr_0><time_period_arr_1><![CDATA[0]]></time_period_arr_1><time_period_arr_2><![CDATA[0]]></time_period_arr_2><time_period_arr_3><![CDATA[5]]></time_period_arr_3><time_period_arr_4><![CDATA[]]></time_period_arr_4><time_period_arr_5><![CDATA[]]></time_period_arr_5></time_list><time_list><time_period><![CDATA[21002155]]></time_period><time_period_arr_0><![CDATA[0]]></time_period_arr_0><time_period_arr_1><![CDATA[0]]></time_period_arr_1><time_period_arr_2><![CDATA[0]]></time_period_arr_2><time_period_arr_3><![CDATA[5]]></time_period_arr_3><time_period_arr_4><![CDATA[]]></time_period_arr_4><time_period_arr_5><![CDATA[]]></time_period_arr_5></time_list><time_list><time_period><![CDATA[22002255]]></time_period><time_period_arr_0><![CDATA[0]]></time_period_arr_0><time_period_arr_1><![CDATA[0]]></time_period_arr_1><time_period_arr_2><![CDATA[0]]></time_period_arr_2><time_period_arr_3><![CDATA[0]]></time_period_arr_3><time_period_arr_4><![CDATA[]]></time_period_arr_4><time_period_arr_5><![CDATA[]]></time_period_arr_5></time_list></item></root>
```



## API 응답 예시

광운대학교 도서관 서버에서 제공하는 응답(XML)을 파싱하여 JSON으로 리턴합니다.

```json
{
  "date": "20260518",
  "total_rooms_count": 13,
  "schedule": [
    {
      "time": "09:00~09:55",
      "availability": {
        "집현 4실": "예약가능",
        "집현 5실": "예약가능",
        "집현 6실": "예약가능",
        "집현 7실": "예약가능",
        "집현 8실": "예약가능",
        "집현 9실": "예약가능",
        "집현 10실": "예약가능",
        "집현 11실": "예약가능",
        "집현 2실": "예약가능",
        "집현 3실": "예약가능",
        "집현 12실": "예약가능",
        "집현 1실": "예약가능",
        "집현 13실": "예약가능"
      }
    },
    {
      "time": "10:00~10:55",
      "availability": {
        "집현 4실": "예약가능",
        "집현 5실": "예약가능",
        "집현 6실": "예약가능",
        "집현 7실": "예약가능",
        "집현 8실": "예약가능",
        "집현 9실": "예약가능",
        "집현 10실": "예약가능",
        "집현 11실": "예약가능",
        "집현 2실": "예약가능",
        "집현 3실": "예약가능",
        "집현 12실": "예약가능",
        "집현 1실": "예약가능",
        "집현 13실": "예약가능"
      }
    },
    {
      "time": "11:00~11:55",
      "availability": {
        "집현 4실": "예약가능",
        "집현 5실": "예약가능",
        "집현 6실": "예약가능",
        "집현 7실": "예약가능",
        "집현 8실": "예약가능",
        "집현 9실": "예약가능",
        "집현 10실": "예약가능",
        "집현 11실": "예약불가",
        "집현 2실": "예약가능",
        "집현 3실": "예약가능",
        "집현 12실": "예약가능",
        "집현 1실": "예약가능",
        "집현 13실": "예약가능"
      }
    },
    {
      "time": "12:00~12:55",
      "availability": {
        "집현 4실": "예약불가",
        "집현 5실": "예약불가",
        "집현 6실": "예약가능",
        "집현 7실": "예약가능",
        "집현 8실": "예약가능",
        "집현 9실": "예약불가",
        "집현 10실": "예약가능",
        "집현 11실": "예약불가",
        "집현 2실": "예약가능",
        "집현 3실": "예약가능",
        "집현 12실": "예약가능",
        "집현 1실": "예약가능",
        "집현 13실": "예약가능"
      }
    },
    {
      "time": "13:00~13:55",
      "availability": {
        "집현 4실": "예약불가",
        "집현 5실": "예약불가",
        "집현 6실": "예약불가",
        "집현 7실": "예약가능",
        "집현 8실": "예약가능",
        "집현 9실": "예약불가",
        "집현 10실": "예약가능",
        "집현 11실": "예약불가",
        "집현 2실": "예약가능",
        "집현 3실": "예약가능",
        "집현 12실": "예약가능",
        "집현 1실": "예약가능",
        "집현 13실": "예약가능"
      }
    },
    {
      "time": "14:00~14:55",
      "availability": {
        "집현 4실": "예약가능",
        "집현 5실": "예약불가",
        "집현 6실": "예약불가",
        "집현 7실": "예약가능",
        "집현 8실": "예약불가",
        "집현 9실": "예약가능",
        "집현 10실": "예약불가",
        "집현 11실": "예약불가",
        "집현 2실": "예약불가",
        "집현 3실": "예약불가",
        "집현 12실": "예약가능",
        "집현 1실": "예약가능",
        "집현 13실": "예약불가"
      }
    },
    {
      "time": "15:00~15:55",
      "availability": {
        "집현 4실": "예약불가",
        "집현 5실": "예약불가",
        "집현 6실": "예약불가",
        "집현 7실": "예약불가",
        "집현 8실": "예약불가",
        "집현 9실": "예약불가",
        "집현 10실": "예약불가",
        "집현 11실": "예약불가",
        "집현 2실": "예약불가",
        "집현 3실": "예약불가",
        "집현 12실": "예약불가",
        "집현 1실": "예약가능",
        "집현 13실": "예약불가"
      }
    },
    {
      "time": "16:00~16:55",
      "availability": {
        "집현 4실": "예약불가",
        "집현 5실": "예약불가",
        "집현 6실": "예약불가",
        "집현 7실": "예약불가",
        "집현 8실": "예약가능",
        "집현 9실": "예약불가",
        "집현 10실": "예약불가",
        "집현 11실": "예약불가",
        "집현 2실": "예약가능",
        "집현 3실": "예약불가",
        "집현 12실": "예약불가",
        "집현 1실": "예약가능",
        "집현 13실": "예약가능"
      }
    },
    {
      "time": "17:00~17:55",
      "availability": {
        "집현 4실": "예약가능",
        "집현 5실": "예약불가",
        "집현 6실": "예약불가",
        "집현 7실": "예약가능",
        "집현 8실": "예약불가",
        "집현 9실": "예약불가",
        "집현 10실": "예약불가",
        "집현 11실": "예약가능",
        "집현 2실": "예약불가",
        "집현 3실": "예약불가",
        "집현 12실": "예약불가",
        "집현 1실": "예약가능",
        "집현 13실": "예약가능"
      }
    },
    {
      "time": "18:00~18:55",
      "availability": {
        "집현 4실": "예약불가",
        "집현 5실": "예약가능",
        "집현 6실": "예약불가",
        "집현 7실": "예약불가",
        "집현 8실": "예약불가",
        "집현 9실": "예약가능",
        "집현 10실": "예약불가",
        "집현 11실": "예약불가",
        "집현 2실": "예약불가",
        "집현 3실": "예약가능",
        "집현 12실": "예약불가",
        "집현 1실": "예약불가",
        "집현 13실": "예약가능"
      }
    },
    {
      "time": "19:00~19:55",
      "availability": {
        "집현 4실": "예약불가",
        "집현 5실": "예약가능",
        "집현 6실": "예약불가",
        "집현 7실": "예약불가",
        "집현 8실": "예약가능",
        "집현 9실": "예약가능",
        "집현 10실": "예약가능",
        "집현 11실": "예약불가",
        "집현 2실": "예약가능",
        "집현 3실": "예약가능",
        "집현 12실": "예약가능",
        "집현 1실": "예약불가",
        "집현 13실": "예약가능"
      }
    },
    {
      "time": "20:00~20:55",
      "availability": {
        "집현 4실": "예약가능",
        "집현 5실": "예약가능",
        "집현 6실": "예약가능",
        "집현 7실": "예약가능",
        "집현 8실": "예약가능",
        "집현 9실": "예약가능",
        "집현 10실": "예약불가",
        "집현 11실": "예약불가",
        "집현 2실": "예약가능",
        "집현 3실": "예약가능",
        "집현 12실": "예약가능",
        "집현 1실": "예약가능",
        "집현 13실": "예약가능"
      }
    },
    {
      "time": "21:00~21:55",
      "availability": {
        "집현 4실": "예약가능",
        "집현 5실": "예약가능",
        "집현 6실": "예약가능",
        "집현 7실": "예약가능",
        "집현 8실": "예약가능",
        "집현 9실": "예약가능",
        "집현 10실": "예약불가",
        "집현 11실": "예약불가",
        "집현 2실": "예약가능",
        "집현 3실": "예약가능",
        "집현 12실": "예약가능",
        "집현 1실": "예약가능",
        "집현 13실": "예약가능"
      }
    },
    {
      "time": "22:00~22:55",
      "availability": {
        "집현 4실": "예약가능",
        "집현 5실": "예약가능",
        "집현 6실": "예약가능",
        "집현 7실": "예약가능",
        "집현 8실": "예약가능",
        "집현 9실": "예약가능",
        "집현 10실": "예약가능",
        "집현 11실": "예약가능",
        "집현 2실": "예약가능",
        "집현 3실": "예약가능",
        "집현 12실": "예약가능",
        "집현 1실": "예약가능",
        "집현 13실": "예약가능"
      }
    }
  ]
}
```
