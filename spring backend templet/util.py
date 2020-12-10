import os
from files.controller import controller
from files.mapper import imapper
from files.service.impl import service
from files.service.impl import junit
from files.service import iservice
from files.query import common
from files.query import mariadb

def makePath(moduleCd, menuCd):
	return f"klago.{moduleCd}.{menuCd[:3].lower()}.{menuCd[:5].lower()}00.{menuCd.lower()}."
	
def makeDirtory(fileData):
    os.makedirs('./'+fileData["menuCodeL"]+'/controller')
    os.makedirs('./'+fileData["menuCodeL"]+'/model')
    os.makedirs('./'+fileData["menuCodeL"]+'/mapper')
    os.makedirs('./'+fileData["menuCodeL"]+'/query/common')
    os.makedirs('./'+fileData["menuCodeL"]+'/query/mariadb')
    os.makedirs('./'+fileData["menuCodeL"]+'/query/oracle')
    os.makedirs('./'+fileData["menuCodeL"]+'/service/impl')

def makeFiles(fileData):
    # controller
    controller.controller(fileData)
    
    # mapper
    imapper.imapper(fileData)

    # service
    service.service(fileData)
    iservice.iservice(fileData)

    # query
    common.common(fileData)
    mariadb.mariadb(fileData)
    # query.oracle(fileData)

    # junit Test
    junit.junit(fileData)