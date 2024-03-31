import os

# 현 file이 위치한 디렉터리를 가져오고...
BASE_DIR = os.path.dirname(__file__)

# format의 값을 {}에 추가한다, 순서대로 적용됨.

# SQLALCHEMY_DATABASE_URI => 데이터베이스 접촉 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))

# SQLALCHEMY_TRACK_MODIFICATIONS => SQLALCHEMY 이벤트 처리 옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False

"""
 sqlite는 소규모 프로젝트에서 사용되는 가벼운 파일 기반 데이터베이스
 SQLite로 프로젝트를 빠르게 개발하고 대규모 데이터베이스를 적용하여 운영 시스템에 반영한다.
"""