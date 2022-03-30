FROM python:3.8
RUN mkdir -p /home/usr/Automation
COPY .  /home/usr/Automation
WORKDIR /home/usr/Automation/Tests
COPY req.txt .
RUN  pip3 install -r req.txt
CMD ["python3","-m", "test_wave_login.py"]