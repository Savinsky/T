from sqlalchemy import Column, Integer, String, Float, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///orm.sqlite', echo=False)
Base = declarative_base()
class HH(Base):
    __tablename__ = 'HH'
    id = Column(Integer, primary_key=True)
    vacancy = Column(Text)
    city = Column(Text)
    salary = Column(Float)
    skills = Column(Text)

    def __init__(self, vacancy, city, salary, skills):
        self.vacancy = vacancy
        self.city = city
        self.salary = salary
        self.skills = skills

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.vacancy, self.city, self.salary, self.skills)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()



