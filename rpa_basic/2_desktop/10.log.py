# import logging

# logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")  
#%(asctime)s 시간정보, [%(levelname)s] 레벨 수준, %(message)s 메세지.
# 시간 [로그레벨] 메세지 형태로 로그 작성
# INFO라고 되어 있어서 INFO까지의 레벨만 뜬다  ( info < warning < error < critical )

# 레벨의 수준  # debug < info < warning < error < critical
# logging.debug("아 이거 누가 짠거야~~")     # 개발자만 보는창
# logging.info("자동화 수행 준비")        # 정보 프로그램 쓰는 사람 PC에 보임
# logging.warning("이 스크립트는 조금 오래 되었습니다. 실행상에 문제가 있을 수 있습니다.")  # 경고 문구를 준다
# logging.error("에러가 발생하였습니다. 에러 코드는 ...")    #동작하다가 실패하는 에러문구
# logging.critical("복구가 불가능한 심각한 문제가 발생했습니다...")

# 터미널과 파일에 함께 로그 남기기
import logging
from datetime import datetime
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")  # logFormatter 변수 만들기, #시간 [로그레벨] 메시지 형태로 로그를 작성
logger = logging.getLogger()
logger.setLevel(logging.DEBUG) #로그 레벨 설정

# 스트림 (터미널)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log") # mylogfile_20201010141011.log   # from datetime import datetime 사용
# %Y%m%d%H%M%S : 년월일 시간 데이터
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남겨보는 테스트를 진행합니다.")