"""===========================================
파일이름 : make bizcubeX back templet.py
기    능 : - bizcubeX 개발의 백엔드 초기 템플릿을 자동 제작
           - moduleName, menuCode, path를 입력함으로써 controller, dao, service, mapper, model을 자동 생성
최초개발 : 2020/03/20
최종수정 : 2020/07/16
개 발 자 : Franciscus S.W.Yang
Copyleft ○ 2020 All Wrongs Reserved
==========================================="""

import sys
import os
from files.controller import controller
from files.mapper import imapper
from files.service.impl import service
from files.service.impl import junit
from files.service import iservice
from files.query import common
from files.query import mariadb


def setMenuData():
    menuCode = input('menuCode: ')

    moduleName = input('ModuleName (default : financial): ')
    moduleName = 'financial' if moduleName == '' else moduleName
    
    path = input('(klago.' + moduleName + '.' + menuCode[:3].lower() + '.' + menuCode[:5].lower() + '00.' + menuCode.lower() + '.) ? ')
    path = ('klago.' + moduleName + '.' + menuCode[:3].lower() + '.' + menuCode[:5].lower() + '00.' + menuCode.lower() + '.') if path == '' else path

    

    return {
        'moduleName': moduleName,
        'menuCodeU': menuCode.upper(),
        'menuCodeL': menuCode.lower(),
        'path': path if path[-1] == '.' else path + '.'
    }


def makeDirtory(menuCode):
    os.makedirs('./'+menuCode+'/controller')
    os.makedirs('./'+menuCode+'/model')
    # os.makedirs('./'+menuCode+'/dao/impl')
    os.makedirs('./'+menuCode+'/mapper')
    os.makedirs('./'+menuCode+'/query/common')
    os.makedirs('./'+menuCode+'/query/mariadb')
    os.makedirs('./'+menuCode+'/query/oracle')
    os.makedirs('./'+menuCode+'/service/impl')

def makeFiles(fileData):
    # controller
    controller.controller(fileData)
    # controllerModel.controllerModel(fileData)

    # dao
    # dao.dao(fileData)
    # idao.idao(fileData)
    # daoModel.daoModel(fileData)

    # mapper
    imapper.imapper(fileData)

    # service
    service.service(fileData)
    iservice.iservice(fileData)

    # query
    common.common(fileData)
    mariadb.mariadb(fileData)
    # query.mariadb(fileData)

    # junit Test
    junit.junit(fileData)

if __name__ == "__main__":
    fileData = setMenuData()

    print(fileData)
    print('moduleName : ' + fileData['moduleName'])
    print('menuCodeU : ' + fileData['menuCodeU'])
    print('menuCodeL : ' + fileData['menuCodeL'])
    print('path : ' + fileData['path'])
    

    makeDirtory(fileData['menuCodeL'])
    makeFiles(fileData)
