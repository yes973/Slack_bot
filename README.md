# 개요

업무자동화를 위해 사용하는 Slack Bot의 예시 코드입니다.

슬랙 App 등록과 설정 등에 대해서는 [Python으로 Slack 챗봇 시작하기](https://medium.com/bothub-studio-ko/python%EC%9C%BC%EB%A1%9C-slack-%EC%B1%97%EB%B4%87-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-d8632c5add42) 등을 참고하시면 좋습니다.

# 설명

* Command_bot

  별도의 서버 상에서 계속 Slack 메시지를 수신하고 있다가, 특정 채널의 특정 키워드가 감지되면 메시지를 응답하는 봇입니다
  
* Database_report

  Crontab과 연동시켜 정해진 시간마다 DB를 조회해 특정 통계량이나 KPI를 산출하고 리포팅하는 봇입니다
  
* Youtube_report

  Crontab과 연동시켜 정해진 시간마다 한국 유튜브 인기탭 상위 10개 컨텐츠의 정보를 크롤링 / 리포팅하는 봇입니다
