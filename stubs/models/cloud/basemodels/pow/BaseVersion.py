#
#
# This file was autogenerated by python_on_wheels.
# But YOU CAN EDIT THIS FILE SAFELY
# It will not be overwtitten by python_on_wheels
# 


from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import delete

import sys,os

sys.path.append( os.path.abspath(os.path.join( os.path.dirname(os.path.abspath(__file__)), "../lib" )))
import powlib
from PowAppObject import PowAppObject

x = PowAppObject()

Base = declarative_base(bind=x.__engine__, metadata = x.__metadata__)
Base.metadata.reflect()

class BaseVersion(Base):
    __table__ = Base.metadata.tables['versions']
    pao = x
    #__mapper_args__ = {}
    session = x.getSession()
    
    def __init__(self):
        self.session = self.pao.getSession()

    def update(self):
        self.session.merge(self)
        self.session.commit()
    
    def delete(self, id):
        s = delete(self.__table__, self.__table__.columns.id==id)
        self.session.execute(s)
        self.session.commit()
    
    def find_by(self, att, val, first=True):
        mstr = "self.session.query(Base" + self.__class__.__name__ +").filter_by(" + str(att) + "=val)"
        if first == True:
            mstr += ".first()"
        #print mstr
        res= eval(mstr)
        #res.__init__()
        return res
            
    def find_all(self):
        mstr = "self.session.query(Base" + self.__class__.__name__ + ").all()"
        #print mstr
        res= eval(mstr)
        for elem in res:
            elem.__init__()
        return res
    
    def get(self, name):
        return eval("self.get_"+ str(name)+"()")
    
    def set(self,name,val):
        #eval("self.set_"+ str(name)+"("+val + ")" )
        eval("self.set_"+ str(name)+"(\""+str(val) + "\")" )