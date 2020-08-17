0. 환경
- 클라우데라 6.3.1

 

 

1. mysql driver 설치
클라우데라 환경에서 postgre db는 디폴트로 드라이버를 제공하지만 mysql은 드라이버를 제공하지 않는다.  아래 링크를 이용해서 파일을 다운로드 한다.

 wget http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.28.tar.gz
 

 

 

다운로드한 mysql jdbc 드라이버 압축을 푼다.

tar xvf mysql-connector-java-5.1.28.tar.gz
 

 

압축을 풀고 디렉토리에 접근하면 jdbc 파일을 찾을 수 있다. (확장자는 .jar ) 
해당 파일을  /opt/cloudera/parcels/CDH/lib/sqoop/lib   로 복사한다. (postger db jdbc 드라이버가 있는 디렉토리다)

 

2. sqoop import 명령어
(1) import MySQL -> HDFS
sqoop import --connect jdbc:mysql://localhost:3306/db_name --username root --P --table table_name -m 1
 
(2) imort 파일 확인하기
hdfs dfs -ls
위 명령어를 사용하면 전체 hdfs 파일을 확인할 수 있다.

 

 
hdfs dfs -ls table_name
table_name이란 테스트용 테이블을 가져왔으므로 위와 같이 테이블 명으로 디렉토리에 접근할 수 있다.

 


hdfs dfs -cat table_name/part-m-00000
해당 디렉토리에는 part-m-00000 이란 파일이 생겼다. 해당 파일을 열어서 RDB에서 읽어온 데이터가 제대로 저장되었는지 확인한다.
