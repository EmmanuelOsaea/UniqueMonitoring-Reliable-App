# Start with a Java Image

FROM eclipse-temurin:17 jdk jammy

RUN apt get update && apt-get install -y python3 python3 pip maven

WORKDIR /app

COPY . .

RUN pip 3 install --no-cache-dir --break-system-packages -r requirements.txt

RUN mvn clean package -DskipTests

EXPOSE 5000

CMD java -jar target/*.jar & python3 app.py
