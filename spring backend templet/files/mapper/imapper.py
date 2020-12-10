def imapper(fileData):
    content = '''package '''+fileData['path']+'''mapper;

import java.util.List;

import egovframework.rte.psl.dataaccess.mapper.Mapper;

/**
 * Name : '''+fileData['menuCodeU']+'''Mapper
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
@Mapper("'''+fileData['path']+'''maper.I'''+fileData['menuCodeU']+'''Mapper")
public interface I'''+fileData['menuCodeU']+'''Mapper {
	
    /* App Builder Continue */

}'''

    imapper = open('./'+fileData['menuCodeL']+'/mapper/I'+fileData['menuCodeU'] + 'Mapper.java', 'w',  encoding='UTF8')
    imapper.write(content)
    imapper.close()
