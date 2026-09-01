# This begins with a Java Image

FROM eclipse-temurin:17-jdk-jammy

# This installs Python & Maven(JavaApp)

RUN apt-get update && apt-get install -y python3 python3-pip maven

# This sets the directory in the cloud container

WORKDIR /app

# This copies github files in the container

COPY . .

# This installs python dependencies

RUN pip3 install --no-cache-dir flask==3.0.3 requests==2.32.3 gunicorn==22.0.0

# This builds a Java app into runnable file

RUN mvn clean package -DskipTests -f backend-java/pom.xml

# This exposes the Python frontend 

EXPOSE 5000

# Run both apps at the same time 
# Java builds into backend/target-1.0.jar while Python is app.py

CMD java -jar target/*.jar & flask run --host=0.0.0.0 --port=5000
