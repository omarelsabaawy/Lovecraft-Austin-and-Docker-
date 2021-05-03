FROM python
COPY . /AssignmentOne
WORKDIR  /AssignmentOne
RUN pip install beautifulsoup4
RUN command 
CMD python pyfile.py