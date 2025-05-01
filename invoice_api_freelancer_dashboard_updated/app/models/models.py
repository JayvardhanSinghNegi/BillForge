from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from app.database.database import Base
from datetime import datetime

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    company = Column(String, index=True)
    projects = relationship("Project", back_populates="client")

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    hourly_rate = Column(Float)
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Client", back_populates="projects")
    timelogs = relationship("TimeLog", back_populates="project")

class TimeLog(Base):
    __tablename__ = "timelogs"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    date = Column(DateTime, default=datetime.utcnow)
    hours = Column(Float)
    project = relationship("Project", back_populates="timelogs")
