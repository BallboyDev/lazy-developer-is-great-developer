def service(fileData):
    content = '''package '''+fileData['path']+'''service.impl;

import java.util.List;

import org.springframework.stereotype.Service;

import egovframework.rte.fdl.cmmn.EgovAbstractServiceImpl;
import klago.log.service.KlagoLog;
import '''+fileData['path']+'''mapper.I'''+fileData['menuCodeU']+'''Mapper;
import '''+fileData['path']+'''service.I'''+fileData['menuCodeU']+'''Service;

/**
 * Name : '''+fileData['menuCodeU']+'''Service
 * Title :
 * 
 * <pre>
 * <b>History :</b>
 * </pre>
 * 
 * @author :
 * @date : 
 * @return
 */
@Service
public class '''+fileData['menuCodeU']+'''Service extends EgovAbstractServiceImpl implements I'''+fileData['menuCodeU']+'''Service{
	
	private I'''+fileData['menuCodeU']+'''Mapper mapper;
	
	/* App Builder Continue */

}'''

    service = open('./'+fileData['menuCodeL']+'/service/impl/'+fileData['menuCodeU'] + 'Service.java', 'w',  encoding='UTF8')
    service.write(content)
    service.close()
